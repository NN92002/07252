import pandas as pd

# 創建 DataFrame
data = {
    'Name': ['John', 'Emma', 'Alex'],
    'Age': [28, 32, 24],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)
print(df)

# 數據選擇
print("\nSelect 'Name' column:")
print(df['Name'])
import pandas as pd

# 創建 DataFrame
data = {
    'Name': ['John', 'Emma', 'Alex'],
    'Age': [28, 32, 24],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)# 將上面的 dict 資料轉換成 DataFrame（表格）
print(df)

# 數據選擇
print("\nSelect 'Name' column:")
print(df['Name']) # 選取 "Name" 欄位（Series 格式，只會印出名字欄）

# 數據過濾
print("\nFilter age > 25:")
print(df[df['Age'] > 25]) # 篩選 Age > 25 的資料列（John 和 Emma）

# 基本數據操作
print("\nSort by Age:")
print(df.sort_values('Age')) # 根據 "Age" 欄位做升序排序（Alex 最年輕）

# 數據過濾
print("\nFilter age > 25:")
print(df[df['Age'] > 25])

# 基本數據操作
print("\nSort by Age:")
print(df.sort_values('Age'))
