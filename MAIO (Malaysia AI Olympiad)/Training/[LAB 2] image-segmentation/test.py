from PIL import Image
import matplotlib.pyplot as plt

image_path = "modified-leaf-segmentation-dataset/test/images/plant (1).png"
mask_path = "modified-leaf-segmentation-dataset/test/masks/plant (1).png"

image = Image.open(image_path)
mask = Image.open(mask_path)

plt.subplot(1,2,1)
plt.imshow(image)
plt.title("Image")
plt.subplot(1,2,2)
plt.imshow(mask, cmap='gray')
plt.title("Mask")
plt.show()

print(f"Image size: {image.size}, Mask size: {mask.size}")

import random
from pathlib import Path
from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader

train_image_dir = Path("modified-leaf-segmentation-dataset/trainval/images")
train_mask_dir = Path("modified-leaf-segmentation-dataset/trainval/masks")

filenames = list(train_image_dir.glob("*"))
filenames = [f for f in filenames if f.is_file()] #ensure we only have files

random.shuffle(filenames)

#80/20 split
split = int(0.8 * len(filenames))
train_files = filenames[:split]
val_files = filenames[split:]

class LeafDataset(torch.utils.data.Dataset):
    def __init__(self, files, image_dir, mask_dir, image_size=(512, 512)):
        self.files = files
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.resize = transforms.Resize(image_size)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        img_path = self.image_dir / self.files[idx].name
        mask_path = self.mask_dir / self.files[idx].name

        image = Image.open(img_path).convert("RGB")
        mask = Image.open(mask_path).convert("L")  #grayscale

        image = self.resize(image)
        mask = self.resize(mask)

        #convert to tensors
        image = transforms.ToTensor()(image)
        mask = transforms.ToTensor()(mask)

        return image, mask

train_dataset = LeafDataset(train_files, train_image_dir, train_mask_dir)
val_dataset = LeafDataset(val_files, train_image_dir, train_mask_dir)

train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=4, shuffle=False)

batch_X, batch_y = next(iter(train_loader))
print(batch_X.shape, batch_y.shape)

import torch
from torch import nn
import torchvision.models as models

class FCN(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        backbone = models.resnet34(pretrained=True)
        self.backbone = nn.Sequential(*list(backbone.children())[:-2])  #remove avgpool and fc (last 2 layers)
        self.conv1x1 = nn.Conv2d(512, num_classes, kernel_size=1, bias=False)
        self.upsample = nn.Upsample(scale_factor=32, mode='bilinear', align_corners=False)

    def forward(self, x):
        original_size = x.shape[2:]
        x = self.backbone(x)
        x = self.conv1x1(x)
        x = self.upsample(x)  #upsample to original input size
        
        if x.shape[2:] != original_size:
            x = nn.functional.interpolate(x, size=original_size, mode='bilinear', align_corners=False)
        return x
    
model = FCN(num_classes=1).to("cuda")

input_tensor = torch.randn(4, 3, 512, 512).to("cuda")
output = model(input_tensor)

print(output.shape)

print(model(next(iter(train_loader))[0].to("cuda")).shape)

from torchvision import transforms

test_image_dir = Path("modified-leaf-segmentation-dataset/test/images")
test_mask_dir = Path("modified-leaf-segmentation-dataset/test/masks")
test_files = list(test_image_dir.glob('*'))
test_dataset = LeafDataset(test_files, test_image_dir, test_mask_dir, image_size=(512, 512))
test_loader = DataLoader(test_dataset, batch_size=4, shuffle=False)

model.eval()

baseline_iou = 0.0
count = 0

with torch.no_grad():
    for images, masks in test_loader:
        images, masks = images.to("cuda"), masks.to("cuda")
        outputs = model(images)
        probs = torch.sigmoid(outputs)
        preds = (probs > 0.5).float()
        
        for pred, mask in zip(preds, masks):
            intersection = (pred * mask).sum()
            union = (pred + mask).sum() - intersection
            iou = (intersection + 1e-6) / (union + 1e-6)
            baseline_iou += iou.item()
            count += 1

mean_iou = baseline_iou / count
print(f"Test Mean IoU: {mean_iou:.4f}")

from torch import optim

criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-4)

train_metrics, val_metrics = [], []

for epoch in range(10):
    model.train()
    for batch_idx, (images, masks) in enumerate(train_loader):
        images, masks = images.to("cuda"), masks.to("cuda")
        outputs = model(images)
        loss = criterion(outputs, masks)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        #every 10 batches
        if (batch_idx + 1) % 10 == 0:
            model.eval()
            with torch.no_grad():
                #compute metrics on current batch (training)
                probs = torch.sigmoid(outputs)
                preds = (probs > 0.5).float()
                train_iou = (preds * masks).sum() / (
                    (preds + masks).sum() - (preds * masks).sum() + 1e-6
                )
                train_dice = (2 * (preds * masks).sum()) / (
                    preds.sum() + masks.sum() + 1e-6
                )
                
                #compute val metrics
                val_loss_total = 0
                val_iou_total = 0
                val_dice_total = 0
                cnt = 0
                for v_images, v_masks in val_loader:
                    v_images, v_masks = v_images.to("cuda"), v_masks.to("cuda")
                    v_out = model(v_images)
                    v_loss = criterion(v_out, v_masks)
                    
                    v_probs = torch.sigmoid(v_out)
                    v_preds = (v_probs > 0.5).float()
                    v_iou = (v_preds * v_masks).sum() / (
                        (v_preds + v_masks).sum() - (v_preds * v_masks).sum() + 1e-6
                    )
                    v_dice = (2 * (v_preds * v_masks).sum()) / (
                        v_preds.sum() + v_masks.sum() + 1e-6
                    )
                    
                    val_loss_total += v_loss.item()
                    val_iou_total += v_iou.item()
                    val_dice_total += v_dice.item()
                    cnt += 1
                
                avg_val_loss = val_loss_total / cnt
                avg_val_iou = val_iou_total / cnt
                avg_val_dice = val_dice_total / cnt
                
                train_metrics.append({
                    'loss': loss.item(),
                    'iou': train_iou.item(),
                    'dice': train_dice.item()
                })
                val_metrics.append({
                    'loss': avg_val_loss,
                    'iou': avg_val_iou,
                    'dice': avg_val_dice
                })
                print("Train Metrics:")
                print(train_metrics[-1])
                print("Val Metrics:")
                print(val_metrics[-1])
                print("\n")
            model.train()

torch.save(model.state_dict(), "fcn_model.pth")

model.eval()
with torch.no_grad():
    images, masks = next(iter(test_loader))
    outputs = model(images.to("cuda"))
    probs = torch.sigmoid(outputs).cpu()
    preds = (probs > 0.5).float()

    # Plot first image in batch
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(images[0].permute(1, 2, 0))
    axes[0].set_title("Image")
    axes[1].imshow(masks[0][0], cmap='gray')
    axes[1].set_title("Ground Truth")
    axes[2].imshow(preds[0][0], cmap='gray')
    axes[2].set_title("Prediction")
    plt.show()

test_image, test_mask = test_dataset[0]
plt.subplot(1, 2, 1); plt.imshow(test_image.permute(1, 2, 0))
plt.subplot(1, 2, 2); plt.imshow(test_mask[0], cmap='gray'); plt.show()

print(test_image.shape, test_mask.shape)

test_iou = 0.0
count = 0

with torch.no_grad():
    for images, masks in test_loader:
        images, masks = images.to("cuda"), masks.to("cuda")
        outputs = model(images)
        probs = torch.sigmoid(outputs)
        preds = (probs > 0.5).float()
        
        for pred, mask in zip(preds, masks):
            intersection = (pred * mask).sum()
            union = (pred + mask).sum() - intersection
            iou = (intersection + 1e-6) / (union + 1e-6)
            test_iou += iou.item()
            count += 1

mean_iou = test_iou / count
print(f"Test Mean IoU: {mean_iou:.4f}")