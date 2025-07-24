# %% [code]
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# %% [code]
# === Read the date
df_train = pd.read_csv("train_data.csv",  dtype={"id": str})
df_test = pd.read_csv("test_data.csv",  dtype={"id": str})

print(df_train)
print(df_test)

# %% [code]
df_train["parsed_pixels"] = df_train["pixels"].apply(lambda x: [float(i.strip()) for i in x[1:-1].split(",")])

df_test["parsed_pixels"] = df_test["pixels"].apply(lambda x: [float(i.strip()) for i in x[1:-1].split(",")])

print(df_train["parsed_pixels"])
print(df_test["parsed_pixels"])

# %% [code]
imglist = []
for i in df_train["parsed_pixels"]:
    imglist.append(np.array(i))

print(imglist)

# %% [code]
imgarray = np.array(imglist)
print(imgarray)

# %% [code]
global_mean_vector = imgarray.mean(axis=0)
print(global_mean_vector)

# %% [code]
subtask1_rows = []
for i in imglist:
    current_row = np.array(i)
    centered_row = current_row - global_mean_vector
    subtask1_rows.append(centered_row)

print(subtask1_rows)

# %% [code]
subtask1 = pd.DataFrame(data={
    "subtaskID": [1] * len(df_train),
    "datapointID": df_train["id"],
    "answer": subtask1_rows
})

print(subtask1)

# %% [code]
model = RandomForestClassifier(max_depth=100, n_estimators=1400)

# %% [code]
model.fit(imgarray, df_train["class"].values)

# %% [code]
X_test = (np.vstack(df_test["parsed_pixels"].values) - global_mean_vector)
y_pred = model.predict(X_test) # values

print(y_pred)

subtask2_rows = []
for pred in y_pred:
    subtask2_rows.append(pred)

print(subtask2_rows)

# %% [code]
# === Final submission
submission_rows = subtask1_rows + subtask2_rows

subtask2 = pd.DataFrame(data={
    "subtaskID": [2] * len(df_test),
    "datapointID": df_test["id"],
    "answer": subtask2_rows
})

submission = pd.concat([subtask1, subtask2], axis=0)
print(submission)

submission.to_csv("submission.csv", index=False)