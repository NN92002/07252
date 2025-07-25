import matplotlib.pyplot as plt

# 折線線圖
x = [1, 2, 3, 4, 5] # X 軸的資料點
y = [2, 4, 0, 8, 10] # Y 軸的資料點

plt.plot(x, y,"--o") # 繪製折線圖（"--o" 表示虛線並加上圓形標記）
plt.title('Simple Line Plot') # 設定圖表標題
plt.xlabel('X-axis') # 設定 X 軸標籤
plt.ylabel('Y-axis') # 設定 Y 軸標籤
plt.show()

# 散佈圖
plt.scatter(x, y) # 繪製散佈圖，x, y 為每個點的座標
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()


