import matplotlib.pyplot as plt
import numpy as np

# 設置隨機種子以確保結果可重現
np.random.seed(0)

# 生成10張隨機的三通道影像
images = np.random.randint(0, 256, size=(64, 64, 3), dtype=np.uint8)
# 生成一張 64x64 的彩色影像（RGB 通道）

# 轉換為灰階
gray_images = np.mean(images, axis=2).astype(np.uint8)
# 將 RGB 彩色影像轉換為灰階影像（取通道平均）

# 顯示選中的灰階影像
plt.figure(figsize=(6, 6))
plt.imshow(gray_images, cmap='gray') # cmap='gray' 才會是真正的灰階
plt.title(f"Gray Image")
plt.axis('off') # 移除座標軸
plt.show()

# 顯示選中的彩色影像
plt.figure(figsize=(6, 6))
plt.imshow(images) # 不加 cmap，保留彩色
plt.title(f"Color Image")
plt.axis('off')
plt.show()

fig, axes = plt.subplots(1, 2, figsize = (12, 6)) # 1行2圖 大小12*6
axes[0].imshow(gray_images, cmap='gray') #第一張圖
axes[0].set_title('Gray Image') #第一張圖標題
axes[1].imshow(images)
axes[1].set_title('Color Image')
plt.show()