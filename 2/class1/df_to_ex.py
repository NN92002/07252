import numpy as np
import pandas as pd
# 生成線性數列
sequence_1 = np.linspace(1, 3, 10) 
# 使用 linspace 產生從 1 到 3 的 10 個等距數值，例如：1.0, 1.22, ..., 3.0

sequence_2 = np.linspace(1, 10, 10)
# 產生從 1 到 10 的 10 個等距數值，例如：1.0, 2.0, ..., 10.0

# 寫成字典型態，後面可以是 list 或 numpy array
d = {'s1': sequence_1, 
     's2': sequence_2,
    }
# 將兩個數列組成一個字典，key 是欄位名稱，value 是資料（list 或 array 都可以）

# 以字典型態寫入xlsl檔案
df = pd.DataFrame(data=d)
# 將字典轉成 pandas DataFrame，也就是表格格式（像 Excel）
df.to_excel(f'test.xlsx')
#df.to_excel("C:/Users/AN515/Desktop/test.xlsx") #指定路徑
# 將 DataFrame 存成 Excel 檔案，檔名為 test.xlsx
# 注意：這行需要安裝 openpyxl 套件（pandas 存 .xlsx 會自動用它當引擎）