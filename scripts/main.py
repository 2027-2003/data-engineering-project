import requests
import pandas as pd

# 1. جلب البيانات من API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

# 2. تحويلها إلى DataFrame
df = pd.DataFrame(data)

# 3. عرض أول 5 صفوف
print(df.head())


df.to_csv("posts.csv", index=False)
print("Data saved successfully")