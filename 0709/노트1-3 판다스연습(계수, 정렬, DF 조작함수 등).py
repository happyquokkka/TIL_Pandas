#!/usr/bin/env python
# coding: utf-8

# In[1]:


#설정변경코드
#변수 명이 두번 이상 출력되어도 모두 콘솔에서 보여줄 것
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"

# InteractiveShell.ast_node_interactivity : 'all' | 'last' | 'last_expr' | 'none' (기본값은 'last_expr')


# In[2]:


# 모듈 import
import numpy as np
import pandas as pd


# ### pandas 데이터처리 및 변환 관련 함수

# ### 데이터 개수 세기
# - 가장 간단한 분석은 데이터의 개수를 세는 것임
# - count() 함수 사용
#     - NaN 값은 세지 않는다

# In[6]:


# 시리즈에서 개수 세기
s = pd.Series(range(10))
s[3] = np.nan
s


# In[8]:


s.count()
# NaN 값을 제외하고 세서 총 9개로 출력


# ### 난수
# - 난수 : seed(값) 라는 함수를 사용할 수 있음
# - seed의 의미 : 난수 알고리즘에서 사용하는 기본 값으로
#     - 시드값이 같으면 동일한 난수가 발생함

# In[33]:


np.random.seed(3)  # 난수값을 고정하기 위해 seed() 함수 사용
# 데이터프레임 예제 생성 시 원소값을 고정하기 위해 쓰는 것임
np.random.randint(5, size=4)
# seed(), 난수발생함수를 동시에 사용해야 난수 데이터를 고정할 수 있음


# In[39]:


np.random.randint(5, size=4)
# seed() 함수가 같이 실행되지 않기 때문에 실행시마다 다른 결과가 반환됨


# In[4]:


# 예제 데이터프레임 생성
# 데이터 0-4범위의 난수 발생, 4행4열, 실수형데이터로 생성
# np.random.seed(3)
# df=pd.DataFrame(np.random.randint(5,size=(4,4)),dtype=float)
# 전체 데이터타입을 float으로 설정함 (dtype = float)
# 기본값은 정수
# df

np.random.seed(3)
df1=pd.DataFrame(np.random.randint(5,size=(4,4))) #기본 정수

df1.iloc[2,3] =np.nan
df1


# In[5]:


# 데이터프레임의 count()는 각 열에 대한 연산을 진행 - 각 열의 유효한 원소의 개수를 반환
# NaN 값은 제외
# 일반적으로 데이터에 결측값의 유무를 확인하기 위해 사용하는 함수임

df1.count()


# ##### count 함수 사용 예제 (titanic 데이터 활용)

# - 타이타닉 승객 데이터 사용
#     - seaborn 패키지 내에 data로 존재
#     - 데이터셋 읽어오기 : 패키지명.load_dataset("data명")
# 

# In[8]:


import seaborn as sns  # 그래프 패키지

titanic = sns.load_dataset('titanic')
titanic.head(10) # head는 기본값이 5개의 데이터만 반환


# In[10]:


# titanic 데이터프레임의 각 열의 원소 개수를 산출 - count() 함수 이용
titanic.shape   # (891,15) 승객 891명
titanic.count() # 시리즈 반환 - 전체 행에 대해 값 차이가 나는 열은 결측치가 있다는 의미


# ## __의식적으로라도 count()와 info() 함수를 사용해서__ 
# ## __데이터의 정보를 보여주는 것이 좋음__

# ###  카테고리 값 세기
# - 시리즈의 값이 정수,문자열 등 카테고리 값인 경우에
# - 시리즈.value_counts()메서드를 사용해 각각의 값이 나온 횟수를 셀 수 있음
# - 파라미터 normalize=True 를 사용하면 각 값 및 범주형 데이터의 비율을 계산
#     - 시리즈.value_counts(normalize=True)
# 

# In[13]:


np.random.seed(1)
s2 = pd.Series(np.random.randint(6, size = 100))
s2.head(10)
s2.tail()


# In[15]:


s2.value_counts() # 0, 1, 2, 3, 4, 5 각 값이 몇 번 나왔는지 결과 반환
# 왼쪽 줄은 인덱스, 오른쪽 줄은 실제 값에 해당


# ### 범주형 데이터에 value_counts() 함수 적용
# - 범주형 데이터 : 관측 별과가 몇개의 범주 또는 항목의 형태로 나타나는 자료
#     - ex. 성별(남,여), 선호도(좋다, 보통, 싫다), 혈액형(A,B,O,AB) 등
# 

# In[16]:


titanic.head(2)


# In[18]:


# alive 열 : 생존여부가 yes/no 로 표시되어 있음
titanic['alive'].dtype  # dtype('0') -> Object type(문자열)이라는 뜻!
titanic['alive'].value_counts()


# In[20]:


# 생존자/ 사망자 비율 계산
titanic['alive'].value_counts(normalize=True)
titanic['alive'].value_counts(normalize=True) * 100


# ##### 데이터프레임에 value_counts() 함수 사용
# - 행을 하나의 value로 정의해서 동일한 행이 몇 번 나타났는지를 반환함
# - 행 데이터의 경우가 인덱스로 설정됨
#     - ex) MultiIndex([(4, 0), (2, 2), (6, 0)], 
# - 계수된 값이 value로 표시되는 series로 반환됨

# In[21]:


# 예제 df
df = pd.DataFrame({'num_legs': [2, 4, 4, 6],
                   'num_wings': [2, 0, 0, 0]},
                  index=['falcon', 'dog', 'cat', 'ant'])
df


# In[24]:


df.value_counts().index
# 동일한 값을 가지는 행의 개수를 반환 (제일 오른쪽 줄에 출력)
df.value_counts()


# In[25]:


# 예제 df
df1


# In[26]:


df1.value_counts() # 행 원소로 NaN값이 있는 필드는 계수하지 않음


# In[28]:


df1.value_counts().shape
df1.value_counts().sort_index().index


# ### 데이터 정렬 - 정렬 함수 사용
# - sort_index() : 인덱스를 기준으로 정렬
# - sort_value() : 데이터 값을 기준으로 정렬

# #### 시리즈 정렬
#     - ascending = True/False : True는 오름차순, False는 내림차순 정렬
#     - 생략하면 오름차순 정렬 진행

# In[30]:


# 예제 시리즈
s2


# In[35]:


s2.value_counts() # 반환 값을 기준으로 정렬된 시리즈
# 값에 따라 인덱스가 나타나게 됨
s2.value_counts().sort_index() # 인덱스 기준 정렬 : 오름차순 정렬이 기본
s2.value_counts().sort_index(ascending=False) # 인덱스 기준 내림차순 정렬


# In[37]:


s2.value_counts().sort_values(ascending=True) # 원소값을 기준으로 오름차순 정렬
s2.value_counts().sort_values(ascending=False) # 원소값을 기준으로 내림차순 정렬


# In[39]:


s2.sort_values()  # 0부터 5까지의 원소값을 기준으로 오름차순 정렬


# ### 데이터 프레임 정렬
# 
# - df.sort_values() : 특정열 값 기준 정렬
#     - 데이터프레임은 2차원 배열과 동일하기 때문에
#         - 정렬시 기준열을 줘야한다. __by 인수 사용 : 생략 불가__
#         - _by = 기준열, by=[기준열1,기준열2] (복수로 사용 가능/ 1번 기준열에서 동일한 행만 2번 기준열을 사용해서 한번 더 그 부분만 정렬!)_
#     - 오름차순/내림차순 : ascending = True/False (생략하면 오름차순)
# - df.sort_index() : DF의 INDEX 기준 정렬
#     - 오름차순/내림차순 : ascending = True/False (생략하면 오름차순)
# 

# In[40]:


# 예제 df1
df1


# In[41]:


# df1.sort_values() / 에러 발생 (by 인수 생략해서)


# In[42]:


df1.sort_values(by = 0, ascending=True) # 0번 열을 기준으로 오름차순 정렬


# In[ ]:


df1.sort_values(by = 0, ascending=False) # 0번 열을 기준으로 내림차순 정렬


# In[44]:


df1.sort_values(by = [0,1], ascending = True)
# 0번 열에서 같은 데이터는 1번 열을 기준으로 재정렬
# 0번 열에서 2라는 데이터가 중복으로 등장하므로 그 값을 갖는 행의 1번 열을 오름차순으로 재정렬


# In[46]:


# df 확인
df


# - 데이터프레임의 index 를 기준으로 정렬

# In[48]:


df.sort_index()
# 기본값이 오름차순이므로 a, b, c... 의 순서대로 정렬됨
df.sort_index(ascending=False) # 인덱스 기준으로 내림차순 정렬


# # 데이터프레임 조작 함수 정리

# ### 행/열 합계
# - df.sum() 함수 사용
# - 행과 열의 합계를 구할때는 sum(axis=0/1) - axis는 0이 기본
# 
# 
# - 각 열의 합계를 구할때는 sum(axis=0)
# - 각 행의 합계를 구할때는 sum(axis=1)
# 

# In[50]:


# 예제 DF 생성
#4행 8열의 데이터프레임 작성, 난수를 발생시키고
#0-9범위에서 매번 같은 난수 발생되어 반환되도록 설정

np.random.seed(1)
df2=pd.DataFrame(np.random.randint(10,size=(4,8)))
df2


# In[53]:


# df2 의 각 열의 합계 = df.sum(axis=0) 함수 사용
df2.sum(axis=0)  # 시리즈 반환
# 0열의 합계, 1열의 합계 ... 7열의 합계까지 시리즈로 반환

df2.sum()  # axis 의 기본값은 0 -> 각 열의 합계 구할 수 있음


# In[55]:


# df2 의 각 행의 합계
df2.sum(axis=1) # 각 행의 합계


# - 데이터프레임 기본 함수 확인

# In[65]:


# 평균/최대/최소값을 구하는 함수 : 각 열이나 또는 행 단위로 연산을 진행

df2.mean()
df2.max()
df2.min()
# axis 생략 -> 각 열의 평균/최댓값/최소값

df2.mean(axis=1)
df2.max(axis=1)
df2.min(axis=1)
# 각 행의 평균/최댓값/최소값 반환


# ### df 의 새로운 행과 열 추가 예제
# 
# - 새로운 열 추가 : 기본 인덱싱 사용
#     - ex) df['새로운 열 이름'] = 값
#     
#     
# - 새로운 행 추가 : loc 인덱서 사용
#     - ex) df.loc['새로운 행 인덱스'] = 값

# In[56]:


df2


# In[60]:


# 위 데이터프레임에 각 열의 합계를 구해서 마지막 행으로 추가하시오.
# 새로운 행 추가 -> 인덱싱 이용 (loc 인덱서 사용이 가장 간단함. 행 우선 인덱싱이어서)
# 행 이름 : CalTotal

df2.sum()
df2.loc['CalTotal'] = df2.sum()
df2


# In[61]:


# df2 데이터프레임에 각 행의 합계를 구해서 마지막 열로 추가하시오.
# 새로운 열 추가
# 열 이름 : RowSum

df2.sum(axis=1)
df2['RowSum'] = df2.sum(axis=1) # 원본 반영


# In[62]:


df2


# ### 행/열 삭제 - 데이터프레임의 drop() 사용 예제
# 
# - df.drop('행 이름', 0) : 행삭제 
#     - 행 삭제 후 df로 결과를 반환
# - df.drop('열 이름', 1) : 열 삭제
#     - 열 삭제 후 df로 결과를 반환
#     
#     
# - 원본에 반영되지 않으므로  원본 수정하려면 저장해야 함
# 
# 
# - del 명령어는 삭제 명령어이며 원본을 변경함

# In[67]:


df2


# In[69]:


df2.drop('CalTotal',0) # 행 삭제 후 결과를 반환
df2 # 원본 데이터에는 반영되지 않는다


# In[71]:


df2.drop('RowSum',1) # 해당 열 삭제한 결과를 반환
df2 # 원본에는 반영되지 않는다


# ### NaN 값 처리 함수
# 
# - df.dropna(axis=0/1)
#     - NaN 값이 있는 열 또는 행을 삭제
#     - 원본에는 반영되지 않음
#     
#     
# - df.fillna(채우려는 값)
#     - NaN 값을 정해진 값으로(숫자/문자) 채움
#     - 원본에는 반영되지 않음

# In[76]:


# df2 에 결측값 적용
df2.iloc[0,0] = np.nan
df2.iloc[2,7] = np.nan
df2


# In[77]:


# NaN이 포함된 모든 행 삭제
df2.dropna()
df2 # 원본 반영 되지 않음


# In[75]:


# NaN이 포함된 모든 열 삭제
df2.dropna(axis=1)
df2 # 원본 반영 되지 않음


# In[78]:


df2


# In[80]:


df2.fillna(0)
df2
df2.fillna(5)


# In[82]:


df2.fillna('a')[0].dtype # dtype('O') = object type


# In[83]:


# df 의 원소 dtype 변경 함수
# df.astype(자료형) int/float

df2.fillna(0).astype(int)
df2
df2.fillna(5).astype(float)


# ### 열 또는 행에 동일한 연산 반복 적용할 때 : apply() 함수
# - apply() 함수는 DataFrame의 행이나 열에 복잡한 연산을 vectorizing(벡터화)할 수 있게 해주는 함수로 매우 많이 활용되는 함수임
# 
# 
# - 동일한 연산을 모든 열에 혹은 모든 행에 반복 적용하고자 할때 사용
# 
# 
# 
# - apply(반복적용할 함수, axis=0/1)
#     - 0 : 열마다 반복
#     - 1 : 행마다 반복 
#     - 생략시 기본값 : 0
# 

# In[84]:


# 예제 df 생성
df3 = pd.DataFrame({
    'a':[1,3,4,3,4],
    'b':[2,3,1,4,5],
    'c':[1,5,2,4,4]
})
df3


# In[86]:


# df3 의 각 열에 대해 np.sum 이라는 함수를 반복 적용하는 코드를 생성하시오

df3.apply(np.sum)


# In[88]:


# df3 의 각 행에 대해 np.sum 이라는 함수를 반복 적용하는 코드를 생성하시오

df3.apply(np.sum, 1)


# In[89]:


df3.sum(axis=0) # 각 열 단위 합계 벡터화 연산
df3.sum(axis=1) # 각 행 단위 합계 벡터화 연산
# 위 코드와 같은 결과를 반환


# - 데이터프레임의 기본 집계함수(sum, min, max, mean 등)들은 행/열 단위 벡터화 연산을 수행함
#     - apply() 함수를 사용할 필요가 없음
# 

# - 일반적으로 apply() 함수 사용은 복잡한 연산을 해결하기 위한 lambda 함수나 사용자 정의 함수를 각 열 또는 행에 일괄 적용시키기 위해 사용
# 

# ##### 1회성 함수인 lambda 함수를 apply() 에 사용하는 예제

# In[94]:


# 집합 데이터(시리즈)의 최댓값과 최소값의 차이를 구하는 연산을 lambda 함수로 정의
df3
diff = lambda x: x.max()-x.min()


# In[93]:


# df3의 a열의 최댓값과 최소값의 차이를 위에서 생성한 lambda  함수를 이용해서 구하시오

diff(df3['a'])


# In[96]:


# apply 함수를 이용하여 위에서 생성한 lambda diff를 df3의 모든 열에 반복 적용하여 
# 모든 열의 최대값과 최소값의 차이를 구하시오

df3.apply(diff,0)


# In[97]:


# apply 함수를 이용하여 위에서 생성한 lambda diff를 df3의 모든 행에 반복 적용하여 
# 모든 행의 최대값과 최소값의 차이를 구하시오

df3.apply(diff,1)


# In[99]:


# 다른 방법 : 직접 연산

# df3 각 행에 대하여 최댓값과 최소값의 차이를 구하시오
df3.max(axis=1) - df3.min(axis=1)


# In[104]:


# df3의 각 열의 데이터에 대해서 카테고리 세기를 수행하시오. 
df3

# apply() 함수를 사용해서 value_counts() 적용 test
df3.apply(pd.value_counts)
# 반복되는 원소값 1~5를 인덱스로 만들고 반복되는 값의 횟수를 count


# In[105]:


# df3의 각 열의 데이터에 대해서 카테고리 세기를 수행하고 NaN 값은 0으로 변환 후
# 반환되는 전체 데이터의 타입을 정수로 변환하시오.

df3.apply(pd.value_counts).fillna(0).astype(int)


# #### 관측 데이터 값을 범주형(카테고리) 값으로 변환
#  - 값의 크기를 기준으로 하여 카테고리 값으로 변환하고 싶을 때
#      - cut(data, bins, label) 함수 사용
#      
#      
#      - data : 구간을 나눌 실제 관측 값
#      - bins : 구간 경계값
#      - label : 구간을 지칭할 카테고리 값
#     

# In[109]:


ages = [0, 0.5, 4, 6, 4, 5, 2, 10, 21, 37, 15, 38, 31, 61, 20, 41, 31, 100]


# In[110]:


#label : 카테고리 명
labels=['영유아','미성년자','청년','중년','장년','노년']

# bins : 구간 경계값 설정
bins = [0, 4, 15, 25, 35, 60, 100]

# 라벨과 빈스의 순서는 동일해야 함
# 최소값을 초과하고 최댓값보다 작거나 같다는 의미를 갖게 됨

# 0 < 영유아 <= 4
# 4 < 미성년자 <= 15


# In[116]:


# 함수 적용해서 카테고리 생성
cats = pd.cut(ages, bins=bins, labels=labels)
cats
type(cats)


# In[117]:


list(cats)


# ##### Categorical 클래스 객체
# - 카테고리명 속성 : Categorical.categories
# - 코드 속성 : Categorical.codes 
#     - 인코딩한 카테고리 값을 정수로 갖는다.
# 

# In[120]:


type(cats)


# In[121]:


cats.categories


# In[123]:


cats.codes
# 인코딩한 카테고리 값을 정수로 반환(제일 처음 카테고리 값은 0부터 시작)
# codes의 원소가 -1 이면 카테고리를 정하지 못했음을 의미(결측값)


# In[124]:


# age 리스트를 이용해서 데이터프레임 생성

df4 = pd.DataFrame(ages, columns = ['ages'])
df4


# In[127]:


df4['연령대'] = pd.cut(df4.ages, bins=bins, labels=labels)
df4


# ##### 구간 경계선을 지정하지 않고 데이터 개수가 같도록 지정한 수의 구간으로 분할하기 :  qcut()  
# 
# - 형식 : pd.qcut(data,구간수,labels=[d1,d2....])
#     
#     
#     - 예)1000개의 데이터를 4구간으로 나누려고 한다면
#         - qcut 명령어를 사용 : 한 구간마다 250개씩 나누게 된다.
#         - 예외) 같은 숫자인 경우에는 같은 구간으로 처리한다.
# 

# In[128]:


# 랜덤정수 20개를 생성하고 생성된 정수를 4개의 구간으로 나누시오.

# 각 구간의 label은 Q1,Q2,Q3,Q4 로 설정하시오.

#랜덤정수 생성 : 범위 0-19, size =20
#seed 설정해서 재실행해도 랜덤정수가 변하지 않도록 생성

# seed 설정
np.random.seed(2)

# 랜덤 정수 생성
data = np.random.randint(20, size=20)
data


# In[129]:


qcat = pd.qcut(data, 4, labels=['Q1','Q2','Q3','Q4'])
qcat


# In[131]:


pd.value_counts(qcat)


# In[ ]:


list(qcat)


# ### 인덱스 설정 함수
# #### 데이터프레임 인덱스 설정을 위해 set_index(), reset_index()
# - set_index() : 기존 행 인덱스를 제거하고 데이터 열 중
# 하나를 인덱스로 설정해주는 함수
# - reset_index() : 기존 행인덱스를 제거하고 기본인덱스로 변경
# - 기본인덱스 : 0부터 1씩 증가하는 정수 인덱스
#     - 따로 설정하지 않으면 기존 인덱스는 데이터열로 추가 됨
# 

# In[139]:


#예제 데이터프레임 생성
df3 = pd.DataFrame({
    'a':[1,3,4,3,4],
    'b':[2,3,1,4,5],
    'c':[1,5,2,4,4]
})
df3


# In[140]:


# df3의 a 열을 인덱스로 설정하시오
df3.set_index('a') # 원본에 반영되지 않으므로 필요하면 저장해야 함
df3

df3 = df3.set_index('a')
df3


# In[143]:


# df3 의 행 인덱스를 제거하고 기본 인덱스로 설정 - reset_index()
df3.reset_index()

# 기존 index의 처리 : drop = True -> 기존 인덱스 제거
# 기존 인덱스를 명시하지 않으면 열 data로 정의

df3.reset_index(drop=True)


# ##### index 원소 변경하기 : df.rename() 사용
# - df.rename(index={현재 인덱스 : 바꿀 인덱스})

# In[145]:


df3 = df3.reset_index(drop=True)
df3


# In[150]:


# df3.rename(index={0: '1번'})
# df3.rename(columns={'b':'학생'})
df3.rename(columns={'b':'학생'}, index = {0:'1반'})
df3 # 원본 반영은 안 됨


# ### 리스트 내포 연산

# #### 리스트 내 for문의 문법
# - [표현식(연산식) for 항목 in 반복가능객체 if 조건문]
# - if 조건문은 생략 가능하다.
# - 반복가능객체 : 리스트, 튜플, 딕셔너리, range()등

# In[151]:


a = [1,2,3,4]

# 위 리스트 a 의 각 원소에 대해 2배를 한 원소값을 만들고 result라는 리스트 변수에 저장하시오.
# [1,2,3,4] * 2  # [1, 2, 3, 4, 1, 2, 3, 4]

result = []
for num in a :
    result.append(num * 2)

result


# In[153]:


# 내포 for 문 사용
result2 = [num*2 for num in a]
result2

