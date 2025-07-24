n, k = map(int, input().split())

heights = []
width = []
area = 0
f = open(r"C:\Users\CY O\Documents\DOCS 2023\coding stuff\MCC\rectangles.txt", "w")


for i in range(n):
    h, w = map(int, input().split())
    heights.append(h)
    width.append(w)
    area += (w*h)

f.write(str(heights))
f.close()
print("max height", max(heights))
print("max height index", heights.index(max(heights)))
print("next max height", sorted(heights, reverse = True)[1])
print("next max height index", heights.index(sorted(heights, reverse = True)[1]))
print("width", sum(width))
print("width until next max height index", sum(width[:heights.index(max(heights))]))
print(area)