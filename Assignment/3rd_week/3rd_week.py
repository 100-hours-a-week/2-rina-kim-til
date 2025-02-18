# -*- coding: utf-8 -*-
"""3rd_week.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lx2pUd9Zs81-ov3c3Z1TU_hPuD5L3WAH

### 1. 데이터 리모델링과 처리

- 주어진 데이터를 pandas DataFrame으로 만들고,

**groupby**

기능을 이용해 Year별 총 Sales를 구하세요.
- 구한 결과를 바탕으로, Year별 총 매출을 Total_Sales라는 새로운 컬럼으로 추가한 DataFrame을 출력하세요.
  - 데이터:

    ```
        Year | Quarter | Sales
        ----------------------
        2023 | Q1      | 200

        2023 | Q2      | 300

        2023 | Q3      | 250
    ```
"""

import pandas as pd

# 데이터 생성
data = {
    'Year': [2023, 2023, 2023],
    'Quarter': ['Q1', 'Q2', 'Q3'],
    'Sales': [200, 300, 250]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# groupby 활용하여 Year별 총 Sales를 Total_Sales 컬럼으로 추가
df['Total_Sales'] = df.groupby('Year')['Sales'].transform('sum') # transform을 이용하여 총 매출 계산
df

"""### 2. 정형 데이터와 비정형 데이터 처리

[**정형 데이터 처리]**

- 주어진 데이터를 DataFrame으로 만들고, Age가 30세 이상(>= 30), Salary가 5만 이상(>= 50000)인 직원만 필터링한 DataFrame을 만드세요.
- 필터링된 결과에서, 직원의 **Name, Age, Department** 컬럼만 출력하세요(또는 필요한 컬럼만).
- 데이터:

  ```
      data = {
          "ID": [1, 2, 3, 4, 5],
          "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
          "Age": [25, 32, 45, 29, 40],
          "Department": ["HR", "Finance", "IT", "Marketing", "IT"],
          "Salary": [48000, 52000, 60000, 45000, 70000]
      }

  ```

"""

# 데이터 생성
data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 32, 45, 29, 40],
    "Department": ["HR", "Finance", "IT", "Marketing", "IT"],
    "Salary": [48000, 52000, 60000, 45000, 70000]
}

# 데이터 프레임 생성
df = pd.DataFrame(data)
df

# 나이 30세 이상, 연봉 5만 이상인 직원 필터링
filtered = df[(df['Age'] >= 30) & (df['Salary'] >= 50000)]
filtered

# 이름, 나이, 직무 컬럼만 출력
result = filtered[['Name', 'Age', 'Department']]
result

"""**[비정형 데이터 처리]**

- API에서 JSON 데이터를 가져와 DataFrame으로 변환 후 아래 필드를 추출해 새로운 DataFrame을 만드세요.
  - id → ID
  - name → Name
  - username → Username
  - email → Email
  - address.city → City
  - company.name → Company
- City가 "Lebsackbury" 또는 "Roscoeview"에 해당하는 사용자만 필터링하세요.
- 필터링된 DataFrame을 CSV 파일로 저장하세요.

**API:** https://jsonplaceholder.typicode.com/users
"""

import requests

# API에서 JSON 데이터 가져오기
api_url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(api_url) # request.get사용하여 API 요청
data = response.json() # 데이터를 json 형식으로 변환

# DataFrame으로 변환
df = pd.DataFrame(data)
df.head()

# 새로운 데이터프레임 생성
new_df = pd.DataFrame({
    'ID': df['id'], # 컬럼 이름 변경
    'Name': df['name'],
    'Username': df['username'],
    'Email': df['email'],
    'City' : df['address'].apply(lambda x: x['city']), # lambda 사용하여 address의 city 추출
    'Company' : df['company'].apply(lambda x: x['name'])
})

new_df

# City가 "Lebsackbury" 또는 "Roscoeview"에 해당하는 사용자만 필터링
filtered_df = new_df[new_df['City'].isin(['Lebsackbury', 'Roscoeview'])]
filtered_df.head()

# 필터링된 데이터프레임을 CSV 파일로 저장
filtered_df.to_csv("filtered.csv", index=False)

# 저장된 CSV 파일 불러오기
df_loaded = pd.read_csv('filtered.csv')
df_loaded

"""### 3. 시각화 및 시계열 데이터 활용

- 아래 데이터를 pandas와 matplotlib를 사용해 시계열 그래프로 시각화하세요.
  - 데이터:

    Date       | Price

    2023-01-01 | 100

    2023-02-01 | 120

    2023-03-01 | 130

    2023-04-01 | 125

    2023-05-01 | 140
  - X축은 날짜, Y축은 가격으로 설정하고, 가격의 추세를 선 그래프로 나타내세요.
"""

import matplotlib.pyplot as plt

# 데이터 생성
date = pd.date_range(start='2023-01-01', periods=5, freq='MS') # MS는 월 시작 날짜를 의미(M=월 마지막 날짜)
price = [100, 120, 130, 125, 140]

# 데이터프레임 생성
df = pd.DataFrame({'Date' : date, 'Price' : price})

#시계열 데이터 생성
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Price'], data=df, color='violet', marker='o')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.title('Time Series Plot')

