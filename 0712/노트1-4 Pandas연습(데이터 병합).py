#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 필요 모듈 호출
import pandas as pd
import numpy as np
import random


# In[3]:


# 여러 변수 출력 코드
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# ### 데이터프레임 병합 / 연결
# - Pandas는 두 개 이상의 데이터프레임을 하나로 합치는
#     - 병합(Merge)와 연결(Concate)을 지원함

# #### merge 명령을 사용한 데이터 프레임 병합
# - Merge : 
#     - 두 개의 데이터 프레임의 공통 열이나 인덱스를 __기준__으로
#     - 두 개의 데이터프레임을 합친다.
#     - 이 때 기준이 되는 열 데이터를 key라고 부른다.
# 

# #### 형식
# - df.merge(df1) : 두 df를 병합시켜 준다.
# - 기본은 inner join : 양쪽에 동일하게 존재하는 키만 표시
# - __key : 병합의 기준이 되는 열을 의미__
#     -  실제 데이터 컬럼이나 행 인덱스 일 수 있다.
# - 병합 방식
#     - left join : 왼쪽 df에만 존재하는 키 데이터는 모두 표시, 오른쪽 df는 키가 중복 되면 표시
#     - right join : 오른쪽 df에만 존재하는 키 데이터는 모두 표시, 왼쪽 df는 키가 중복 되면 표시
#     - inner join :  양쪽 df에서 모두 키가 존재하는 data만표시
#     - outer join :  한쪽에만 키가 존재해도 data를 표시
#     - 병합 방식을 설정 : how = inner / how = outer (생략 가능)

# ![](join_all.png)

# ![](join_inout.png)

# In[9]:


#예시 df 생성 - 고객 정보를 담고 있는 df
df1 =pd.DataFrame({
    '고객번호' : [1001,1002,1003,1004,1005,1006,1007],
    '이름' : ['둘리','도우너','또치','길동','희동','마이콜','영희']
        },
    columns=['고객번호','이름'])
df1

#예제 df 생성 - 예금 정보 df
df2 = pd.DataFrame({
    '고객번호':[1001,1001,1005,1006,1008,1001],
    '금액' : [10000,20000,15000,5000,100000,30000]
},columns=['고객번호','금액'])
df2


# ### merge 명령으로 두 df를 병합하는 문법
#  - 모든 인수 생략(병합 df를 제외한) 공통 이름을 갖고 있는 열
#      - 따라서, '고객번호'가 키가 됨
#  - 양쪽에 모두 존재하는 키의 data만 보여주는 inner join 방식을 사용
# 

# In[10]:


df1.head(1)
df2.head(1)


# In[11]:


# 방법 0 : df1.merge(df2)
# 이 경우에는 기준 데이터프레임이 df1

# 방법 1 : pd.merge(df1, df2) 
# 이 경우에는 기준 데이터프레임이 왼쪽 (df1)

df1.merge(df2)  # inner join 과 양쪽 df에서 열 이름이 같은 열을 키로 설정
# df1, df2의 고객번호 열에서 중복되는 데이터만 출력됨


# In[12]:


df1
df2


# - __outer join__ 방식은 키 값이 한 쪽에만 있어도 데이터를 보여 줌
#     - _pd.merge(df1,df2, how = 'outer')_
#     - 어느 한 df에 데이터가 존재하지 않으면 NaN으로 표시됨

# In[14]:


pd.merge(df1,df2, how = 'outer')
# df1.merge(df2, how = 'outer') 이렇게 표기할 수도 있음


# #### how = inner/outer/left/right
# - how=left : 왼쪽 df에 있는 모든 키의 데이터는 표시
# - how=right : 오른쪽 df 에 있는 모든 키의 데이터는 표시

# In[15]:


pd.merge(df1,df2, how='left')


# In[16]:


pd.merge(df1,df2, how='right')


# - 동일한 키 값이 있는 경우
#     - 키값이 같은 데이터가 여러개 있는 경우에는 있을 수 있는 모든 경우의 수를 따져서 조합을 만들어 낸다.
# 

# In[17]:


#예제 df 생성 
#열: 품종, 꽃잎길이
df1 = pd.DataFrame({
    '품종':['setosa','setosa','virginica','virginica'],
    '꽃잎길이':[1.4,1.3,1.5,1.3]
}, columns=['품종','꽃잎길이'])
df1

#열 : 품종, 꽃잎너비
df2 = pd.DataFrame({
    '품종': ['setosa','virginica','virginica','ersicolor'],
    '꽃잎너비':[0.4,0.3,0.5,0.3]
},columns=['품종','꽃잎너비'])
df2


# - df1과 df2 를 병합
#     - 위 데이터에서 키 값 setosa에 대해
#         - df1에는 1.4와 1.3 2개의 데이터가 있고
#         - df2에는 0.4라는 1개의 데이터가 있으므로
#     - 병합 데이터에는 setosa가 (1.4,0.4)(1.3,0.4)의 2 경우가 표현된다.
#         
# 
#     - 키값 virginica의 경우에는 df1에 2개 df2에 2개의 데이터가 있으므로
#     - 2개와 2개의 조합에 의해 4개의 데이터가 표현된다.
# 

# In[18]:


pd.merge(df1,df2)


# #### 병합(merge) 시 key에 대한 설명
# - 두 데이터프레임에서 열 이름(컬럼명)이 같은 모든 컬럼은 Key가 될 수 있음
# - 이름이 같아도 키로 설정하지 않아야 하는 열이 있으면 기준열 명시
#     - __on__ 파라미터의 인수를 설정

# In[19]:


# 예제 df
df1 = pd.DataFrame({
    '고객명':['춘향','춘향','몽룡'],
    '날짜' : ['2018-01-01','2018-01-02','2018-01-01'],
    '데이터':[20000,30000,100000]
})
df1

df2 = pd.DataFrame({
    '고객명':['춘향','몽룡'],
    '데이터':['여자','남자']
})
df2

# df1과 df2에 동일한 컬럼명이 존재('고객명', '데이터')
# 그 중 데이터 컬럼은 원소의 의미가 다름(키로 사용하면 안 됨!!!)
# 병합 시 직접 key(기준 열)을 명시해야 함


# - 기준열을 직접 지정 : __on = 기준열 이름__
#     - 반환 결과 키가 아닌 열에 동일 필드명이 있을 경우에는 필드명_x, 필드명_y로 필드명을 변경해서 표현

# In[20]:


# pd.merge(df1, df2)
# 데이터 타입도 다르고, 키도 2개가 나타나기 때문에 에러 발생

pd.merge(df1, df2, on = '고객명')


# - 키가 되는 기준열이 두 데이터 프레임에서 _다르게 나타나면_
#     - __left_on, right_on 인수를 사용해서 기준열을 명시해야 함__

# In[21]:


df1=pd.DataFrame({
    '이름' :['영희','철수','철수'],
    '성적' :[90,80,80]
})
df2 = pd.DataFrame({
    '성명' :['영희','영희','철수'],
    '성적2':[100,80,90]
})
df1.head(1)
df2.head(1)


# In[23]:


pd.merge(df1, df2, left_on='이름', right_on='성명')
# 여기서 left에 해당하는 데이터프레임은 df1

# 양쪽에서 기준이 되는 열의 이름이 다르기 때문에 on인수를 두 번 사용
# 출력결과는 양쪽 df의 기준 열 이름이 다르기 때문에 기준 열이 모두 나타난다.


# - 일반 데이터 열이 아닌 인덱스를 기준으로 merge 할 수 도 있음
#     - 인덱스를 기준열로 사용하려면
#         - left_index = True 또는
#         - right_index = True 설정을 하게 됨

# In[25]:


# 예제 데이터프레임

df1 = pd.DataFrame({
    '도시': ['서울','서울','서울','부산','부산'],
    '연도': [2000,2005,2010,2000,2005],
    '인구':[9853972,9762546,9631482,3655437,3512547]    
})
df2=pd.DataFrame(
    np.arange(12).reshape((6,2)),
    index=[['부산','부산','서울','서울','서울','서울'],
          [2000,2005,2000,2005,2010,2015]],
    columns=['데이터1','데이터2']
)
# df2 는 다중인덱스 소유

df1
df2


# In[26]:


pd.merge(df1,df2, left_on = ['도시', '연도'], right_index = True)
# 왼쪽의 df1는 '도시'와 '연도'열이 기준열, 오른쪽의 df2는 인덱스를 기준으로 병합


# - 양쪽 데이터프레임의 key(기준열)가 모두 인덱스인 경우
#     - right_index = True, left_index = True 로 설정 가능

# In[27]:


df1 = pd.DataFrame(
[[1.,2.],[3.,4.],[5.,6.]],
index=['a','c','e'],
columns=['서울','부산'])
df1

df2=pd.DataFrame(
[[7.,8.],[9.,10.],[11.,12.],[13.,14.]],
    index=['b','c','d','e'],
columns=['대구','광주'])
df2


# In[29]:


pd.merge(df1, df2, how='outer', left_index=True, right_index=True)


# - merge 함수 대신 join 사용 가능

# In[30]:


df1.join(df2)


# ### concat 명령을 사용한 데이터 연결
# 
#      pd.concat(objs,  # Series, DataFrame, Panel object  
#         axis=0,  # 0: 위+아래로 합치기, 1: 왼쪽+오른쪽으로 합치기   
#         join='outer', # 'outer': 합집합(union), 'inner': 교집합(intersection)  
#         ignore_index=False,  # False: 기존 index 유지, True: 기존 index 무시 
#         keys=None, # 계층적 index 사용하려면 keys 튜플 입력) 
#         
# 
# - concat 명령을 사용하면 기준열 없이 데이터를 연결한다.
# - 기본은 위 아래로 데이터 행 결합(row bind)  axis 속성을 1로 설정하면 열 결합(column bind)을 수행한다
# 
# - 단순히 두 시리즈나 데이터프레임을 연결하기 때문에 _인덱스 값이 중복될 수 있다._

# #### pd.concat([df1,df2],axis=0) 행 결합
# ![](join_inout_row.png)

# #### pd.concat([df1,df2],axis=1) 열 결합
# ![](./concat_column.png)

# In[31]:


# 예제 시리즈
#두 시리즈 데이터 연결
s1=pd.Series([0,1],index=['A','B'])
s2=pd.Series([2,3,4],index=['A','B','C'])
s1
s2


# In[32]:


pd.concat([s1,s2])


# ##### 데이터프레임 결합

# In[34]:


# concat 연결 예제 df
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'E': ['C4', 'C5', 'C6', 'C7'],
                    'F': ['D4', 'D5', 'D6', 'D7']},
                   index=[0, 1, 2, 3])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'O': ['D8', 'D9', 'D10', 'D11']},
                   index=[1,2,3,4])
df1
df2
df3


# In[37]:


# concat() : join 인수 생략은 'outer'와 같다

result = pd.concat([df1, df2])
result = pd.concat([df1, df2], axis=0, join = 'outer') # axis=0, join='outer'가 기본값
result


# In[38]:


# result 데이터프레임의 인덱스가 중복되어 있음 : 행 인덱싱을 수행하면?

result.loc[0] # 인덱스가 0인 모든 행을 추출


# In[40]:


# 인덱스가 중복되므로 기본 인덱스로 재설정
# reset_index(drop=True) - 기존 인덱스 제거
result = result.reset_index(drop=True)
result


# - join = 'inner' : 공통열만 표현

# In[41]:


result0 = pd.concat([df1, df2], join = 'inner') # 두 df의 공통 열만 추출
result0


# - ignore_index = True : 기존 인덱스 제거 후 제로베이스 인덱스 설정

# In[42]:


result0 = pd.concat([df1, df2], join = 'inner', ignore_index = True)
result0


# - keys=[상위인덱스1, 상위인덱스2, ...] : 상위레벨 인덱스 설정하는 파라미터

# In[45]:


result1 = pd.concat([df1, df2, df3], keys=['df1','df2','df3'])
result1


# - 다중인덱스인 경우 데이터 접근 : 다트 연산자(.)를 이용한 체인 인덱싱

# In[47]:


result1.loc['df1']


# In[48]:


result1.loc['df1'].loc[1:2]
# df1 데이터프레임에서 1번부터 2번 인덱스(라벨 인덱스)를 가진 행들을 추출


# #### concate를 이용한 열 결합
#     - axis=1 설정
#     - pd.concat([df1,df2],axis=1,join='inner/outer')
#     - 데이터프레임들의 열을 결합한다 -> 모든 열을 다 표시함
#     - 모든행을 표시하고 해당 행의 데이터가 없는 열의 원소는 NaN으로 표시된다 : 기본설정(join='outer')
#     - 병합하는 데이터프레임에 중복되는 인덱스의 행만 표시한다 : join='inner'
# 

# In[49]:


# 예제 df 생성

df1=pd.DataFrame(
    np.arange(6).reshape(3,2),
    index=['a','b','c'],
    columns=['데이터1','데이터2']
)
df1
df2=pd.DataFrame(
    5+np.arange(4).reshape(2,2),
    index=['a','c'],
    columns=['데이터2','데이터4']
)
df2


# In[52]:


pd.concat([df1,df2], axis=1, join='outer', keys=['df1','df2'])


# In[53]:


pd.concat([df1,df2], axis=1, join='inner', ignore_index = True)

