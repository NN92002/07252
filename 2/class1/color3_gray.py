import numpy as np
import matplotlib.pyplot as plt
# 設置隨機種子
np.random.seed(0) # 設定亂數種子為 0，確保每次執行產生相同的隨機資料（方便重現結果）

# 隨機生成三通道影像
images = np.random.randint(0, 255, size=(64, 64, 3), dtype=np.uint8)
# 產生一張隨機 RGB 彩色圖片，大小為 64x64 像素，三個通道
# 像素值為 0～254 的整數（uint8 格式）
# shape 是 (64, 64, 3)

# 轉換為灰階並計算統計數據
gray_images = np.mean(images, axis=2).astype(np.uint8)
# 將 RGB 三通道的平均值當作灰階像素
# axis=2 表示在 R、G、B 三通道方向取平均 → 得到 shape 為 (64, 64)
# 再轉換為整數類型（uint8）方便顯示

# 計算統計數據
max_values = np.max(gray_images, axis=1)
# 計算每一列（橫列）的最大灰階值
# 回傳陣列長度為 64（對應 64 列），每個值是該列最亮的像素

# show出統計結果
print(max_values)
plt.imshow(images)    # 隨機三通道影像(彩色圖片)
plt.show()
plt.imshow(gray_images, cmap='gray')    # 灰階圖片
#cmap='',viridis預設值可不寫,gray灰階,hot熱度
plt.show()    # 隨機三通道影像(彩色圖片)
