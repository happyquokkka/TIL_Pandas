#!/usr/bin/env python
# coding: utf-8

# # 데이터프레임

# ![](./dataframe.png)
# 
# - 진한 부분 : 각각 column name(열 제목), row name(행 제목 = 인덱스)
# 
# 
# - Pandas 라이브러리에서 기본적으로 데이터를 다루는 단위는 DataFrame : spreadsheet와 같은 개념
# 
# 
# - 이러한 형태의 데이터는 __Structured Data 또는 Panel Data 또는 Tabular Data라고 부름__ (이름만 다를 뿐임)
# 
# 
# - pandas를 공부한다는 것은 결국 dataframe의 사용법을 익히고 활용하는 방법을 배운다는 것과 같다
# 
# 
# - pandas를 잘 활용하면 대부분의 structured data를 자유자재로 다룰 수 있게 됨
# 

# ### 데이터 프레임
# - ★ 2차원 행렬 데이터에 인덱스를 붙인 것 ★
# 
# 
# - 열을 뜯어내면 array가 됨 (array의 특성들 사용 가능하게 됨)
# 
# 
# - 행과 열로 만들어지는 2차원 배열 구조
# 
# 
# - R의 데이터 프레임 에서 유래
# 
# 
# - 데이프레임의 _각 열은 시리즈로 구성되어 있음_ 
#   ㅡ __각 열의 데이터 타입은 동일!!!__
# 
# 
# - DataFrame()함수를 사용해서 생성
# 

# ![](./pandas_files.png)

# ## 데이터프레임 생성

# #### 리스트로 데이터 프레임 만들기
# 
# - DataFrame([[list1],[list2]]) ㅡ 보통 2개 이상의 열을 가짐
# 
# 
# - 각 list는 한 행으로 구성됨
# 
# 
# - 행의 원소 개수가 다르면 None 값으로 저장
# 

# In[92]:


import pandas as pd
import numpy as np


# In[5]:


# 1차원 리스트를 이용해서 df 생성 - 원소가 각 행으로 맵핑
df = pd.DataFrame(['a','b','c'])
print(df)
# 2차원 리스트를 이용해서 df 생성 - 하위 리스트가 각 행으로 맵핑
df = pd.DataFrame([['a','b','c'], ['a','a','g']])
df


# In[7]:


# 하위 리스트의 원소의 개수가 서로 다른 경우 - None 값을 저장하게 됨
# 파이썬 내 자료형인 리스트에 저장된 None 값이 출력되는 것임

df = pd.DataFrame([['a','b','c'], ['a','a','g'], ['a','a']])
df


# ### 딕셔너리로 데이터 프레임 생성
# - dict의 key 값 -> Column Name으로 들어감
# - dict item 은 데이터프레임의 column 으로 정의
# - 열의 순서, 행의 순서는 큰 의미를 갖지 않음

# In[9]:


df1= pd.DataFrame({'A':[90,80,70],
                   'B':[85,98,75],
                   'C':[88,99,77],                   
                   'D':[87,89,86]},
                 index=[0,1,2])
df1


# In[28]:


# df의 값을 위한 dict

data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2000002],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율":[0.0283, 0.0163, 0.0982,0.0141]
}

#열방향 인덱스(컬럼명) columns=
columns = ['지역','2015','2010','2005','2000','2010-2015 증가율']

#행방향 인덱스 index =
index=['서울','부산','인천','대구']

# pd.DataFrame(데이터, index = , columns = ,)
# 파라미터(매개변수)의 순서는 바뀌어도 되지만 데이터는 무조건 맨 앞에 위치

df3 = pd.DataFrame(data, index = index, columns = columns)
df3


# ### 시리즈로 데이터 프레임 생성
# - pd.DataFrame(시리즈) : 시리즈를 열로 정의 -> 1개의 시리즈가 전달
# - 여러 개의 시리즈를 이용해서 데이터 프레임 생성 : 리스트로 묶어서 전달
#     - pd.DataFrame([시리즈1, 시리즈2 ...]) 
#        : 리스트 원소 시리즈 1개가 한 행으로 정의
#        - 시리즈의인덱스 => 컬럼명

# In[12]:


a = pd.Series([100, 200, 300], ['a', 'b', 'd'])
b = pd.Series([101, 201, 301], ['a', 'b', 'k'])
c = pd.Series([110, 210, 310], ['a', 'b', 'c'])


# In[15]:


print(pd.DataFrame(a)) # 시리즈를 열로 정의 -> 1개의 시리즈가 전달

pd.DataFrame([a]) # 리스트 원소 시리즈 1개가 한 행으로 정의


# In[17]:


pd.DataFrame([a,b,c])
# numpy의 array에서 확장된 시리즈 내 저장된 NaN 값이 나타냄
# None 값이나 NaN 값이나 모두 결측값에 해당


# #### csv 데이터로부터 Dataframe 생성
#  - 데이터 분석을 위해, dataframe을 생성하는 가장 일반적인 방법
#  - 데이터 소스로부터 추출된 csv(comma separated values) 파일로부터 생성
#  - pandas.read_csv() 함수 사용
# 

# In[49]:


# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('../data/train.csv')
print(train_data.shape)
train_data.head()  # df의 처음 5행을 출력
train_data.head(10)
train_data.tail()  # df의 마지막 5행을 출력


# #### read_csv 함수 파라미터
#  - _sep_ - 각 데이터 값을 구별하기 위한 구분자(separator) 설정 
#  - _header_ - header를 무시할 경우, None 설정
#  - _index_col_ - index로 사용할 column 설정
#  - _usecols_ - 실제로 dataframe에 로딩할 columns만 설정
# 

# In[22]:


train_data = pd.read_csv('../data/train.csv', index_col = 'PassengerId', usecols=['PassengerId', 'Survived', 'Pclass', 'Name'])
train_data


# In[24]:


train_data.columns  # 어떤 열들이 있는지를 확인


# In[25]:


train_data.index  # 데이터 내 index를 확인


# #### 인덱스와 컬럼의 이해
# 
# 1. 인덱스(index) = 행(row) = 레코드(record)
#  - index 속성
#  - 각 아이템을 특정할 수 있는 고유의 값을 저장
#  - 복잡한 데이터의 경우, 멀티 인덱스로 표현 가능
#  
#  
# 2. 컬럼(column)
#  - columns 속성
#  - 각각의 특성(feature)을 나타냄
#  - 복잡한 데이터의 경우, 멀티 컬럼으로 표현 가능
# 

# In[29]:


df3


# In[30]:


# df의 컬럼명(열 인덱스) 확인 - columns 속성 사용
df3.columns


# In[31]:


# df의 인덱스(행 인덱스) 확인 - index 속성 사용
df3.index


# #### 행/열 인덱스 이름 설정
# - index.name
# - columns.name

# In[32]:


df3.index.name = '도시'
df3.columns.name = '특성'
df3


# In[34]:


# 데이터프레임의 data 값만 추출하려면 values 속성 사용
# numpy의 array에 인덱스를 붙인 게 시리즈
# 시리즈에 인덱스를 붙인 게 데이터프레임

df3.values  # np의 array 형태로 구성
df3.values[0]


# ### dataframe 데이터 파악하기
# - shape 속성 (row, column)
#  - describe() : 숫자형 데이터의 통계치 계산
#  - info() : 데이터 타입, 각 아이템의 개수 등 출력
#  - ★ info()는 데이터 처리 전 외부 데이터 가져올 때 반드시 하기 ★

# In[35]:


df3


# In[37]:


# data 전체 양 확인 - df.shape : (row, column) 으로 반환 일어남
df3.shape


# In[39]:


# DataFrame 개요 정보 출력
df3.info()


# In[43]:


# 판다스 실수 출력 형식 변경 코드
pd.options.display.float_format = '{:.2f}'.format # 일반 실수 표현 (소수점 이하 둘째자리까지 표현)


# In[45]:


# DataFrame의 기본 통계량 출력 - df.describe()
df3.describe()


# In[46]:


pd.reset_option('display.float_foramt') # 기본 형태 출력 설정 변경 코드(지수표현)


# In[47]:


train_data


# In[48]:


train_data.info()


# In[50]:


train_data.info()


# ### 데이터프레임 전치
# - 판다스 데이터프레임은 전치를 포함해서 Numpy 2차원 배열에서 사용할 수 있는 특성이나 메서드를 대부분 지원함
# - 전치: 행과 열을 바꿈
#     관련 속성: df.T

# In[52]:


df3


# In[56]:


print(type(df.T)) # 전치해도 DataFrame 속성을 유지
df3.T # 원본 데이터에 반영되지 않는다


# In[54]:


# df3 전치
df3.T['서울'] # df3.T['서울']


# ### 데이터프레임 내용 변경 :
# - 열추가/열삭제, 내용갱신

# In[57]:


# 사용 예제
df3


# ### 해당열이 있으면 내용 갱신, 열이 없으면 추가
# - 열추가 : df[열이름(key)]=values
# - 열 내용 갱신 : df[열이름(key)]=values

# In[59]:


# 열 내용 갱신
# 2010-2015 증가율 변경
df3['2010-2015 증가율'] = df3['2010-2015 증가율'] * 100
# df3['2010-2015 증가율'] 자체가 시리즈이므로 벡터화 연산이 진행되어 원소값마다 * 100 연산 진행됨
df3


# In[67]:


# 새로운 열 추가
# df3['2005-2015 증가율'] 
df3['2005-2015 증가율'] = ((df3['2015']-df3['2005']) / df3['2005'] * 100).round(2)


# In[68]:


df3


# In[69]:


del df3['2010-2015 증가율'] # 원본에 반영되기 때문에 두 번 이상 실행하면 에러 발생


# In[70]:


df3


# ## 데이터프레임 기본 인덱싱
# 1. 열인덱싱
# 2. 인덱서를 사용하지않는 행 인덱싱
# - []기호를 이용해서 인덱싱할때 주의점 : []기호는 열 위주 인덱싱이 원칙
# 

# In[71]:


# 사용예제
df3


# ### 1. 열 인덱싱
# - 열 라벨(컬럼명)을 키값으로 생각하고 인덱싱한다.
#     - 인덱스로 라벨값을 하나 넣으면 시리즈 객체가 반환
#     - 라벨의 배열이나 리스트를 넣으면 부분적 df 가 반환
# 

# In[77]:


# 인덱스로 라벨 값 1개 사용 - 열 위주 인덱싱
print(type(df3['지역']))
df3['지역']  # 시리즈 형태로 반환


# In[78]:


# 열 1개 접근할 때는 .(dot) 연산자 사용 가능 : df.컬럼명
df3.지역  # 시리즈 형태로 반환


# In[85]:


# 열 추출할 때 데이터프레임으로 반환받고자 하면 컬럼명을 리스트형태로 사용하면 됨
print(type(df3[['지역']]))
df3[['지역']]


# In[86]:


# 여러개의 열을 추출 - [] 리스트 사용
df3[['2010','2015']] # dataframe을 반환


# ### 판다스 데이터프레임에 열이름(컬럼명)이 문자열일 경우에는
# - 수치 인덱스를 사용할 수 없음
# - 열 인덱싱 - 위치 인덱싱 기능을 사용할 수 없다. : keyerror 발생
# - 데이터프레임을 사용할 때는 위치 인덱싱 고려하지 않음

# In[87]:


try :
    df3[0]
except Exception as e :
    print(type(e))


# - 위치 인덱싱처럼 보이는 예제

# In[90]:


np.arange(12)
np.arange(12).reshape(3,4) # np.adarray.reshape(행, 열) - 요소의 배치를 변경


# In[94]:


df5 = pd.DataFrame(np.arange(12).reshape(3,4))
df5


# In[98]:


df5[[1,2]]  # 위치 인덱싱이 아닌 컬럼명이 숫자로 되어있는 df의 인덱싱을 진행한 것


# In[102]:


# df5[[0:3]] / 슬라이싱 불가
# SyntaxError: invalid syntax


# ## 행 단위 인덱싱
# - 행단위 인덱싱을 하고자 하면 인덱서라는 특수 기능을 사용하지 않는 경우 슬라이싱을 해야 함(인덱서는 바로 뒤에 배움)
# - 인덱스 값이 문자(라벨)면 문자슬라이싱도 가능하다
# 

# In[100]:


df3


# In[101]:


# 1 행 추출 [:1] - 슬라이싱 사용
df3[:1]


# In[104]:


df3[1:3]  # [시작위치 : 끝위치 + 1]
# 1-2번째 행 추출


# In[106]:


df3['서울':'부산'] # 행 인덱스 서울부터 부산까지 추출


# - 개별요소 접근[열][행]
# ★ 순서에 주의 ★ (열, 행의 순서!!!!)

# In[107]:


df3['2015']['서울']


# In[109]:


type(df3['2015']['서울']) # 원소값의 형태 출력 - 정수

