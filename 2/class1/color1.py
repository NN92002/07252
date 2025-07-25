# 先安裝matplotlib
# 紅色10x10雜訊方塊
import numpy as np
import matplotlib.pyplot as plt # 載入 Matplotlib 中的 pyplot 模組，用於繪圖與顯示影像
one = np.random.randint(0, 255, size=(10, 10), dtype=np.uint8)
# 建立一個 10x10 的二維陣列，內容是隨機整數，範圍從 0 到 254（不含 255）
# 使用 dtype=np.uint8 表示使用 8 位元無號整數，常見於影像像素資料
# 這個陣列可以想像成一張灰階隨機圖片，每個像素值代表灰階亮度
zero = np.zeros((10, 10), dtype=np.uint8)
# 建立一個 10x10 的二維陣列，所有值都是 0（純黑）
# 雖然這行沒在後續程式碼中使用，但通常會用來建立空白或遮罩圖層
r = np.random.randint(0, 255, size=(10, 10), dtype=np.uint8)
g = np.random.randint(0, 255, size=(10, 10), dtype=np.uint8)
b = np.random.randint(0, 255, size=(10, 10), dtype=np.uint8)

img = np.stack((r, g, b), axis=-1)
# 將同一個 one 陣列堆疊三次，變成一張 RGB 彩色影像
# 第一個 one 作為 R（紅色）通道
# 第二個 one 作為 G（綠色）通道
# 第三個 one 作為 B（藍色）通道
# axis=-1 表示沿著最後一個維度堆疊，所以 shape 從 (10, 10) 變成 (10, 10, 3)
# 因為三個通道的內容一樣，畫面會呈現灰色調（灰階圖像，但格式為彩色）
#要變彩色要用rgb
plt.imshow(img)
plt.show()
# 是綠色 img = np.stack((zero, one, zero), axis=-1)
# 是藍色 img = np.stack((zero, zero, one), axis=-1)
# (r,g,b)
# 數值0~255

