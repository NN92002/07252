import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 設置隨機種子
np.random.seed(0)

# 產生 10 張隨機 RGB 圖片，大小為 64x64
images = np.random.randint(0, 256, size=(10, 64, 64, 3), dtype=np.uint8)

# 轉換為灰階（取三通道平均）
gray_images = np.mean(images, axis=3).astype(np.uint8)  # shape: (10, 64, 64)

# 儲存統計資訊
stats = []

# 建立圖表
fig, axes1 = plt.subplots(2, 5, figsize=(15, 6))  # 2行5列
axes1 = axes1.flatten()  # 轉為一維方便用 for 迴圈 
# 把 2x5 的子圖陣列攤平成 1 維陣列，方便 for 迴圈使用

for i in range(10):
    img = images[i]

    # 顯示圖片
    axes1[i].imshow(img)
    axes1[i].axis('off')
    axes1[i].set_title(f'Image {i}', fontsize=10) #fontsize字形大小

# 自動排版避免重疊
#plt.tight_layout()
plt.show()

fig, axes2 = plt.subplots(2, 5, figsize=(15, 6))  # 2行5列
axes2 = axes2.flatten()  # 轉為一維方便用 for 迴圈
for i in range(10):
    img_gray = gray_images[i]
    max_val = np.max(img_gray)
    min_val = np.min(img_gray)
    mean_val = round(np.mean(img_gray), 2)
    std_val = round(np.std(img_gray), 2)

    # 儲存統計數據
    stats.append({
        'Max': max_val,
        'Min': min_val,
        'Mean': mean_val,
        'Std': std_val
    })

    # 顯示圖片
    axes2[i].imshow(img_gray,cmap = 'gray')
    axes2[i].axis('off')
    axes2[i].set_title(f'Image {i}', fontsize=10)

# 自動排版避免重疊
#plt.tight_layout()
plt.show()

# 儲存統計資料為 Excel
df = pd.DataFrame(stats)
df.to_excel(r"C:\Users\AN515\Desktop\清\2\HW1\gray_image_stats.xlsx")


