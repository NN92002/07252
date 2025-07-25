import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\AN515\Desktop\清\2\HW2\dataset.csv")
X = data[['Runtime']]  # 特徵矩陣
y = data['faults']     # 目標變量

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)# 創建線性回歸模型實例

model = LinearRegression()

# 擬合模型
model.fit(X_train, y_train)

# 預測測試集的結果
y_pred = model.predict(X_test)

# 計算性能指標
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 打印性能指標
print("斜率（權重）w:", model.coef_)
print("截距 b:", model.intercept_)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# 繪製觀測值
plt.scatter(X_test, y_test, color='black', label='Actual faults')

# 繪製預測值
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Predicted faults')

# 設定圖標題和軸標籤
plt.title('Linear Regression for Fault Prediction')
plt.xlabel('Runtime')
plt.ylabel('Faults')

# 顯示圖例
plt.legend()

# 顯示圖表
plt.show()