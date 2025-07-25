import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 讀取資料
data = pd.read_csv(r"C:\Users\AN515\Desktop\清\2\HW2\dataset.csv")
X = data[['Runtime']]
y = data['faults']

# 分割訓練與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 線性回歸
model = LinearRegression()
model.fit(X_train, y_train)
y_pred_linear = model.predict(X_test)
mse_linear = mean_squared_error(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)

print("線性回歸：")
print("斜率（權重）w:", model.coef_)
print("截距 b:", model.intercept_)
print(f'Mean Squared Error: {mse_linear}')
print(f'R^2 Score: {r2_linear}\n')

# 非線性回歸（多項式回歸）
degree = 6
polyreg = make_pipeline(PolynomialFeatures(degree), LinearRegression())
polyreg.fit(X_train, y_train)
y_pred_poly = polyreg.predict(X_test)
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print("非線性回歸（多項式）:")
print(f'Mean Squared Error: {mse_poly}')
print(f'R^2 Score: {r2_poly}')

# 視覺化：同圖顯示
plt.figure(figsize=(10, 6))

# 畫出實際觀測點
plt.scatter(X_test, y_test, color='black', label='Actual faults')

# 線性回歸曲線
plt.plot(X_test, y_pred_linear, color='blue', linewidth=2, label='Linear Regression')

# 非線性回歸曲線（用平滑的 X 值）
X_fit = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_fit_poly = polyreg.predict(X_fit)
plt.plot(X_fit, y_fit_poly, color='red', linewidth=2, label='Polynomial Regression (deg=6)')

# 圖表標題與標籤
plt.title('Linear vs Nonlinear Regression')
plt.xlabel('Runtime')
plt.ylabel('Faults')
plt.legend()
plt.grid(True)
plt.show()
