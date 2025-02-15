# -*- coding: utf-8 -*-
"""2주차 과제_rina.kim.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15TNLtIi6an_J2eXrvp0H50JyKpdAI_pX

# 1. NumPy 배열 생성 및 연산
- NumPy를 사용해 3x3 정수 배열(1부터 9까지)과 2x5 실수 배열(0~1 사이 난수)을 생성하세요. 생성한 배열의 합계와 평균을 각각 계산하고, 두 배열을 곱한 결과를 출력하세요.
"""

import numpy as np

# 배열 생성
arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.random.rand(2, 5)
print(arr1)
print(arr2)

# 각 배열의 합
print(np.sum(arr1))
print(np.sum(arr2))

# 각 배열의 평균
print(np.mean(arr1))
print(np.mean(arr2))

# 두 배열의 곱
rashaped_arr1 = arr1.reshape(9, 1)
reshaped_arr2 = arr2.reshape(1, 10)
print(np.dot(rashaped_arr1, reshaped_arr2))

"""# 2. Pandas를 활용한 데이터 처리
- 아래 데이터를 DataFrame으로 생성하세요.
Name: [Alice, Bob, None, Charlie]
Age: [25, None, 28, 35]
City: [New York, None, Chicago, None]

- 누락된 이름은 "Unknown"으로, 나이는 평균 나이로 채우고 수정된 DataFrame을 출력하세요.
"""

import pandas as pd

# DataFrame 생성
data = {
    'Name': ['Alice', 'Bob', None, 'Charlie'],
    'Age': [25, None, 28, 35],
    'City': ['New York', None, 'Chicago', None]
}

df = pd.DataFrame(data)
print(df)

print('\n')

# 누락 이름 : Unknown, 나이 : 평균 나이로 채움
df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)

"""# 3. HTTP 통신을 활용한 데이터 읽기 및 저장
- [https://jsonplaceholder.typicode.com/todos에서](https://jsonplaceholder.typicode.com/todos%EC%97%90%EC%84%9C)

JSON 데이터를 가져오세요.
데이터를 파일로 저장한 뒤, "title" 키의 값을 출력하세요.
"""

import json
import requests

url = f'https://jsonplaceholder.typicode.com/todos'

# JSON 데이터 가져오기
requestData = requests.get(url)
data = requestData.json()

# 데이터 파일로 저장하기
file_path = 'todos.json'
with open(file_path, 'w') as f:
  json.dump(data, f)

# title 키 값 출력
with open('todos.json', 'r') as f:
  todos = json.load(f)
  for k in todos:
    print(k['title'])