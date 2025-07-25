import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Read data
df = pd.read_csv("C:/Users/AN515/Desktop/清/2/class2/salesdata.csv")  # <-- update path if needed

# Map day numbers to names
weekday_map = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

df['Weekday Name'] = df['DayOfWeek'].map(weekday_map)

# Calculate average sales per weekday
avg_sales = df.groupby('Weekday Name')['Sales'].mean().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)

# Linear regression
linear_model = LinearRegression()
linear_model.fit(df[['DayOfWeek']], df['Sales'])

# Polynomial regression (degree = 3)
degree = 3
poly_model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
poly_model.fit(df[['DayOfWeek']], df['Sales'])

# Predict sales for next 7 weekdays
future_days = pd.DataFrame({'DayOfWeek': range(1, 8)})
future_days['Weekday Name'] = future_days['DayOfWeek'].map(weekday_map)
future_days['Linear Predicted'] = linear_model.predict(future_days[['DayOfWeek']])
future_days['Polynomial Predicted'] = poly_model.predict(future_days[['DayOfWeek']])
future_days['Actual Average'] = avg_sales.values

# Print prediction table
print(future_days)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(future_days['Weekday Name'], future_days['Actual Average'], marker='o', label='Actual Average Sales', color='black')
plt.plot(future_days['Weekday Name'], future_days['Linear Predicted'], marker='o', label='Linear Regression Prediction', color='blue')
plt.plot(future_days['Weekday Name'], future_days['Polynomial Predicted'], marker='o', label='Polynomial Regression (deg=3)', color='red')

plt.title('Weekly Sales Comparison: Actual vs Linear vs Polynomial')
plt.xlabel('Day of Week')
plt.ylabel('Sales Amount')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
