# Pandas - 교재 237쪽

- __series, DataFrame등의 자료구조를 활용한 데이터분석 기능을 제공해주는 라이브러리__
    - 라이브러리 구성
        - 여러종류의 클래스와 다양한 함수로 구성
        - 시리즈와 데이터 프레임의 자료 구조 제공
        - 시리즈(1차원 배열) 데이터프레임(2차원 배열)
    - 아나콘다(데이터 분석을 위한 툴)에 기본으로 설치되어 있음
    - 써드파티 패키지임

#### 판다스의 목적
- 서로 다른 유형의 데이터를 공통된 포맷으로 정리하는 것
    ex) 학번과 성적, 이름
- 행과 열로 이루어진 2차원 데이터프레임을 처리 할 수 있는 함수제공 목적
- 실무 사용 형태 : 데이터 프레임



### 구조적 데이터 생성하기 - Series / DataFrame (자료구조의 한 종류)


#### Series(교재 pp 237~240)
  - pandas의 기본 객체 중 하나 (물리적으로는 파이썬의 리스트와 비슷하고, 논리적으로는 딕셔너리와 비슷함)

  - numpy의 ndarray를 기반으로 인덱싱을 기능을 추가하여 1차원 배열을 나타냄

  - index를 지정하지 않을 시, 기본적으로 ndarray와 같이 0-based 인덱스 생성

  - 지정할 경우 명시적으로 지정된 index를 사용

  - 중요!!! __같은 타입__의 0개 이상의 데이터를 가질 수 있음
      - _반드시 같은 타입의 데이터여야 함_
      
  - 함수 대소문자 구분에 주의!!!

      


1. 자료구조: 시리즈
    - 데이터가 순차적으로 나열된 1차원 배열 형태
    
    - 인덱스(index)와 데이터 값(value)이 일대일로 대응
    
    - 딕셔너리와 비슷한 구조 : {key(index):value}
    
      
    
2. 시리즈의 인덱스
    - 데이터 값의 위치를 나타내는 이름표 역할
    
    - 시리즈는 원래 순서가 없으므로 인덱스를 명시하여 인덱스의 순서대로 순서를 지정할 수 있다
    
      
    
3. 시리즈 생성 : 판다스 내장함수인 Series()이용
    - 리스트로 시리즈 만들기
    - 딕셔너리로 시리즈 만들기
    - 튜플로 시리즈 만들기



```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"
# 출력 전체를 다 보여줌
# 마지막 것만 출력하고 싶을 때 : 기본값은 'last_expr' 옵션 넣기
```


```python
# pandas 패키지(모듈) import
# 대부분의 코드에서 pandas pd 라는 별칭으로 사용
import pandas as pd

# numpy 패키지 import
import numpy as np
```



# Series 생성하기

- data로만 생성하기
    - index 명시하지 않으면 0부터 자동 생성


```python
# 문법 : 변수 = pd.Series()
blank_s = pd.Series()
blank_s  # dtype(datatype): float64)

```

    Series([], dtype: float64)




```python
s0 = pd.Series(1) # 인덱스 명시하지 않고, 데이터 1개로 생성함 - 인덱스는 0부터 시작하는 0-based 인덱스 생성
s0
```


    0    1
    dtype: int64




```python
s0[0] # 원소값 접근
```


    1




```python
# 2개 이상의 원소값을 갖는 시리즈 생성 시 - 리스트, 튜플, 딕셔너리 등을 활용
s1=pd.Series([1,2,3])
s1
# 왼쪽 열: 인덱스, 오른족 열: 원소값 의미
```


    0    1
    1    2
    2    3
    dtype: int64




```python
# 서로 다른 데이터 타입의 원소를 갖는 리스트를 이용하여 시리즈 생성
s1_1 = pd.Series([1,2.0,3.5]) # float64 형태의 시리즈로 자동적으로 바뀐다
s1_1
```


    0    1.0
    1    2.0
    2    3.5
    dtype: float64




```python
s1_2 = pd.Series(['a',1,5.0]) # dtype: object ㅡ 숫자와 문자가 혼용되면 문자형태로 시리즈를 만듦
s1_2
```


    0      a
    1      1
    2    5.0
    dtype: object




```python
# 튜플로 시리즈 만들기 ㅡ 리스트와 동일
s1_3 = pd.Series((1,2,3))
s1_3
```


    0    1
    1    2
    2    3
    dtype: int64





- 시리즈 값 생성할 때 정수의 범위 내에서 난수 생성 - `range()/np.arange() `
- `np.arange()` 함수는 넘피 패키지 안의 함수임


```python
s = pd.Series(range(10,14)) 
# 10부터 13(14-1)까지의 난수 무작위 생성
s
```


    0    10
    1    11
    2    12
    3    13
    dtype: int64




```python
s = pd.Series(np.arange(200))
s
# 데이터 정수 하나하나의 크기가 32비트(200개나 되어서)
```


    0        0
    1        1
    2        2
    3        3
    4        4
          ... 
    195    195
    196    196
    197    197
    198    198
    199    199
    Length: 200, dtype: int32





- 결측값을 포함해서 시리즈를 만들기
    - 결측값은 NaN 으로 표시됨 : numpy라는 모듈의 nan 속성을 통해서 생성 가능 -> np.nan


```python
s = pd.Series([1,2,3, np.nan, 6,8])
# 일부러 결측값을 만들었음
s
# 결측값이 들어가면 float 으로 처리됨
```


    0    1.0
    1    2.0
    2    3.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64





- 인덱스 명시해서 시리즈 만들기
    - 숫자 인덱스 지정/ 문자 인덱스 지정
    - 변수 = pd.Series([값1, 값2, ...],index=[인덱스1,인덱스2, ...])


```python
# 인덱스 명시해서 시리즈 생성(수치 인덱스)
s = pd.Series([10,20,30], index=[1,2,3])
s
# 인덱스 명시하지 않으면 인덱스가 0부터 시작함
```


    1    10
    2    20
    3    30
    dtype: int64




```python
s.index
# s라는 시리즈의 index 반환 - 정수이기 때문에 int64의 데이터타입 가짐
```


    Int64Index([1, 2, 3], dtype='int64')




```python
# 인덱스 명시해서 시리즈 생성(문자 인덱스)
s = pd.Series([10,20,30], index=['홍길동', '이몽룡', '성춘향'])
s
```


    홍길동    10
    이몽룡    20
    성춘향    30
    dtype: int64





- 인덱스 활용 :
    - 시리즈의 index는 __index 속성__ 으로 접근


```python
# 시리즈명.index
s.index
```


    Index(['홍길동', '이몽룡', '성춘향'], dtype='object')





- 시리즈.index.name 속성
    - 시리즈의 인덱스에 이름을 붙일 수 있음
    - 가독성을 높이기 위해서 사용!


```python
s
```


    홍길동    10
    이몽룡    20
    성춘향    30
    dtype: int64


```python
s.index.name = '이름'
s
```


    이름
    홍길동    10
    이몽룡    20
    성춘향    30
    dtype: int64





* 예제 df 생성


```python
s= pd.Series([9904312,3448737,289045,2466052],
            index=["서울","부산","인천","대구"]) #dtype='object' datatype = '문자열 객체'
s.index
```


    Index(['서울', '부산', '인천', '대구'], dtype='object')




```python
s.index.name = '도시'
s
```


    도시
    서울    9904312
    부산    3448737
    인천     289045
    대구    2466052
    dtype: int64



* 시리즈의 실제 값 추출 -> __시리즈.values__  속성 사용


```python
s.values # array 구조로 반환 ㅡ 서로 다른 데이터 타입을 원소로 가질 수 없음
```


    array([9904312, 3448737,  289045, 2466052], dtype=int64)





- __시리즈.name__  속성
    - 시리즈 데이터(values)에 이름을 붙일 수 있다
    - name 속성은 _값의 의미 전달에 사용_


```python
s.name = '인구'
s
```


    도시
    서울    9904312
    부산    3448737
    인천     289045
    대구    2466052
    Name: 인구, dtype: int64





### 딕셔너리로 시리즈 만들기

- `Series({key:value,key1:value1....})`

- 인덱스  ->  딕셔너리의 key

- 값  ->  딕셔너리의 value

- key가 인덱스로 처리되므로 __명시적으로 인덱스를 설정하게 됨__

  


```python
scores = {'홍길동':96, '이몽룡':100, '성춘향':88}
s = pd.Series(scores)
s
# scores 딕셔너리의 key인 '홍길동', '이몽룡', '성춘향'은 s 시리즈의 인덱스가 되며
# scores 딕셔너리의 value인 96, 100, 88은 s 시리즈의 값(원소)이 된다
```


    홍길동     96
    이몽룡    100
    성춘향     88
    dtype: int64




```python
city = {'서울': 9631482, '부산': 3393191, '인천':2632035, '대전':1490158}
s = pd.Series(city)
s
```


    서울    9631482
    부산    3393191
    인천    2632035
    대전    1490158
    dtype: int64





#### * 딕셔너리의 원소는 순서를 갖지 않는다.

- 딕셔너리로 생성된 시리즈의 원소도 _순서가 보장되지 않는다._
- 만약 순서를 보장하고 싶으면 __인덱스를 리스트로 지정해야__ 한다.



```python
s2 = pd.Series(city,index=['부산','인천','서울','대전'])
s2
```


    부산    3393191
    인천    2632035
    서울    9631482
    대전    1490158
    dtype: int64





### 인덱싱
* 데이터에서 특정한 데이터를 추출하는 것을 의미

  

#### 시리즈의 인덱싱 종류

1. __정수형 위치 인덱스(integer position)__

2. __인덱스 이름(index name)__ 또는  __인덱스 라벨(index label)__

    - 인덱스 별도 지정하지 않으면 0부터 시작하는 정수형 인덱스가 지정됨

      

#### 원소 접근
* 정수형 인덱스 : 숫자 s[0]
* 문자형 인덱스 : 문자 s['인천']


```python
print(s.index)
s
```

    Index(['서울', '부산', '인천', '대전'], dtype='object')

    서울    9631482
    부산    3393191
    인천    2632035
    대전    1490158
    dtype: int64




```python
# 위치 인덱스
s[0]   # 서울의 값을 반환
```


    9631482




```python
# 라벨 인덱스
s['서울']
```


    9631482




```python
### 확인 예제
s_1 = pd.Series([1,2,3],index=[1,2,3])
s_1
```


    1    1
    2    2
    3    3
    dtype: int64


```python
s_1.index
# s_1[0] # 인덱스 타입이 정수면 위치 인덱스 사용 불가능
```


    Int64Index([1, 2, 3], dtype='int64')




```python
# 한 줄에 위치 인덱스, 문자 인덱스를 동시에 접근
print(s)
s[3], s['대전'] # 튜플 형태로 값 반환(튜플 생성됨)
```

    서울    9631482
    부산    3393191
    인천    2632035
    대전    1490158
    dtype: int64

    (1490158, 1490158)





#### 리스트 이용 인덱싱

* 자료의 순서를 바꿔 반환하거나 특정 자료 여러 개를 선택할 때 사용

* 시리즈명[[인덱스1, 인덱스2, ...]]

  


```python
s
s[[0,3,2,1]] # 리스트 s의 순서 바꿔서 출력
```


    서울    9631482
    부산    3393191
    인천    2632035
    대전    1490158
    dtype: int64


    서울    9631482
    대전    1490158
    인천    2632035
    부산    3393191
    dtype: int64




```python
s[['서울','인천']]
```


    서울    9631482
    인천    2632035
    dtype: int64



#### 시리즈 슬라이싱을 이용한 인덱싱

- _정수형 위치 인덱스_ 를 사용한 슬라이싱
    - 시리즈[start:stop+1]
    
- _문자(라벨)인덱스_ 이용 슬라이싱
    - 시리즈['시작라벨':'끝라벨']  : 표시된 라벨 범위 모두 추출



```python
s
```


    서울    9631482
    부산    3393191
    인천    2632035
    대전    1490158
    dtype: int64




```python
# 위치 인덱스를 이용한 슬라이싱
s[1:3]
```


    부산    3393191
    인천    2632035
    dtype: int64




```python
# 문자 인덱스를 이용한 슬라이싱
s['부산':'대전']
```


    부산    3393191
    인천    2632035
    대전    1490158
    dtype: int64




```python
### 슬라이싱 예제 ㅡ 명시적으로 설정한 정수 인덱스를 슬라이싱하면 위치 슬라이싱이 적용됨 ㅡ 주의!!!!
s_test = pd.Series([1,2,3,4], index=[1,3,5,7])
s_test
```


    1    1
    3    2
    5    3
    7    4
    dtype: int64




```python
### 문자 인덱스인 경우에는 . (dot 연산자)를 이용해서 접근할 수 있음
s
```


    서울    9631482
    부산    3393191
    인천    2632035
    대전    1490158
    dtype: int64




```python
s.서울
```


    9631482




```python
s.인천
```


    2632035




```python
s_test
```


    1    1
    3    2
    5    3
    7    4
    dtype: int64


```python
# s_test. 1
# 연산자 이용한 원소 접근은 문자 인덱스만 가능
```



#### 인덱싱을 통한 데이터 업데이트

- 시리즈명[인덱스] = 데이터값


```python
s
```


```python
서울    9631482
부산    3393191
인천    2632035
대전    1490158
dtype: int64
```



```python
s['서울'] = 10000000
s
```


    서울    10000000
    부산     3393191
    인천     2632035
    대전     1490158
    dtype: int64



#### 인덱스 재사용 가능


```python
s.index
s1 = pd.Series(np.arange(4), s.index)
# s 시리즈의 인덱스를 s1 시리즈의 인덱스에 재사용 할 수 있음
s1
```


    Index(['서울', '부산', '인천', '대전'], dtype='object')


    서울    0
    부산    1
    인천    2
    대전    3
    dtype: int32







# 시리즈 연산




```python
# 예제 시리즈
s
# 서울    10000000
# 부산     3393191
# 인천     2632035
# 대전     1490158
# dtype: int64
```


    서울    10000000
    부산     3393191
    인천     2632035
    대전     1490158
    dtype: int64



#### 벡터화 연산

- numpy 배열처럼 pandas의 시리즈도 벡터화 연산 가능 
- 벡터화 연산이란 __집합적 자료형의 원소 각각을 독립적으로 계산하는 것__
    - 단, 연산은 시리즈의 값에만 적용되며 _인덱스 값은 변경 불가_



```python
pd.Series([1,2,3]) + 4
```


    0    5
    1    6
    2    7
    dtype: int64




```python
# s 시리즈의 값을 1/1000000 로 변환
s/1000000
```


    서울    10.000000
    부산     3.393191
    인천     2.632035
    대전     1.490158
    dtype: float64




```python
# 벡터화 인덱싱 ㅡ 인덱싱에 조건식 부여 가능
# 시리즈 s의 원소 값 중 250000(250e4) 보다 크고 5000000(500e4) 보다 작은 원소를 추출
# 시리즈명[조건식] - 모든 원소의 값을 각각 조건식으로 확인해서 결과가 true인 원소만 추출

s[(s > 250e4) & (s < 500e4)]
```


    부산    3393191
    인천    2632035
    dtype: int64





#### **Boolean selection** (기법의 한 종류)
  - boolean Series가 []와 함께 사용되면 True 값에 해당하는 값만 새로 반환되는 Series객체에 포함
  - 다중조건의 경우, &(and), |(or)를 사용하여 연결 가능



```python
s0 = pd.Series(np.arange(10), np.arange(10)+1)
s0
```


    1     0
    2     1
    3     2
    4     3
    5     4
    6     5
    7     6
    8     7
    9     8
    10    9
    dtype: int32




```python
s0 > 5
# 조건식 검사
```


    1     False
    2     False
    3     False
    4     False
    5     False
    6     False
    7      True
    8      True
    9      True
    10     True
    dtype: bool




```python
s0[s0>5] 
```


    7     6
    8     7
    9     8
    10    9
    dtype: int32




```python
s0[1] + 1
# s0 시리즈의 두 번째 원소값에 + 1을 해라 (벡터화 연산이 아님)
```


    1




```python
# s0 시리즈의 원소 값 중 짝수 원소 값을 추출하시오
s0 % 2 == 0  # 짝수 판별
s0[s0 % 2 == 0]  # 짝수 추출 - 조건식으로 인덱싱
```


    1      True
    2     False
    3      True
    4     False
    5      True
    6     False
    7      True
    8     False
    9      True
    10    False
    dtype: bool


    1    0
    3    2
    5    4
    7    6
    9    8
    dtype: int32




```python
s0.index > 5  # s0의 인덱스 값을 추출해서 벡터화 연산 진행
# 인덱스 값이 6 이상부터 True 값 반환
```


    array([False, False, False, False, False,  True,  True,  True,  True,
            True])




```python
s0[s0.index > 5]  # s0의 인덱스 값이 5를 초과하는 원소를 출력해라
```


    6     5
    7     6
    8     7
    9     8
    10    9
    dtype: int32




```python
(s0 >= 7)
(s0 >= 7).sum() # 각 원소에 대하여 조건식을 만족하는 데이터의 개수를 세어 줌
```


    1     False
    2     False
    3     False
    4     False
    5     False
    6     False
    7     False
    8      True
    9      True
    10     True
    dtype: bool


    3




```python
s0[s0>=7]
s0[s0>=7].sum() # 각 원소에 대해 대입한 조건식의 결과값이 True인 원소들의 합
```


    8     7
    9     8
    10    9
    dtype: int32


    24





#### 두 시리즈 간의 연산

* 시리즈간의 연산은 같은 인덱스를 찾아서 진행됨

* 따라서 동일하지 않은 인덱스는 연산처리 불가 -> NaN 값(결측값) 처리됨

  


```python
num_s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
num_s2 = pd.Series([5,6,7,8], index=['b','c','d','a'])
num_s1
num_s2
```


```python
a    1
b    2
c    3
d    4
dtype: int64
```


```python
b    5
c    6
d    7
a    8
dtype: int64
```


```python
num_s1 + num_s2 # 시리즈 간의 연산은 같은 인덱스를 찾아 진행
```


    a     9
    b     7
    c     9
    d    11
    dtype: int64




```python
num_s3 = pd.Series([1,2,3,4], index=['e','b','f','g'])
num_s4 = pd.Series([5,6,7,8], index=['b','c','d','a'])
num_s3
num_s4
```


    e    1
    b    2
    f    3
    g    4
    dtype: int64


    b    5
    c    6
    d    7
    a    8
    dtype: int64


```python
num_s3 + num_s4
# 동일한 인덱스는 b밖에 없음
# 두 시리즈의 인덱스가 다르면 동일한 인덱스끼리는 연산을 진행하고
# 나머지 인덱스는 연산처리가 불가 -> NaN값 처리
```


    a    NaN
    b    7.0
    c    NaN
    d    NaN
    e    NaN
    f    NaN
    g    NaN
    dtype: float64


```python
num_s4.values - num_s3.values
# values 속성을 사용하면 시리즈의 형태가 사라지므로 동일한 위치 원소들끼리 연산
# 시리즈의 values는 array 형태를 반환
```


    array([4, 4, 4, 4], dtype=int64)





#### 딕셔너리 와 시리즈의 관계

- 시리즈 객체는 라벨(문자)에 의해 인덱싱이 가능
    - 실질적으로는 라벨을 key로 가지는 딕셔너리 형과 같다고 볼 수 있음
- 딕셔너리에서 제공하는 대부분의 연산자 사용 가능
    - in 연산자 : T/F
    - for 루프를 통해 각 원소의 key와 value에 접근 할 수 있음


- in연산자/for구문 사용 가능


```python
s
```


    서울    9631482
    부산    3393191
    인천    2632035
    대전    1490158
    dtype: int64




```python
# s 시리즈에 인덱스가 서울인 원소가 시리즈에 있는지 확인
'서울' in s # True - 인덱스가 서울인 원소가 s 시리즈에 있음
```


    True


```python
'대구' not in s
```


    True




```python
# 딕셔너리의 items() 함수 시리즈에서도 사용 가능
s.items()
list(s.items()) # 인덱스와 값(즉 아이템)이 짝을 지어 튜플로 묶여서 리스트로 출력
```


    <zip at 0x14fb9574900>


    [('서울', 9631482), ('부산', 3393191), ('인천', 2632035), ('대전', 1490158)]




```python
# 반복문을 활용해서 시리즈 각 원소를 출력하는 코드
for k,v in s.items() :
    print('%s = %d' % (k,v))
```

    서울 = 9631482
    부산 = 3393191
    인천 = 2632035
    대전 = 1490158



#### 시리즈 데이터의 갱신/ 추가/ 삭제

- 인덱싱을 사용하면 딕셔너리처럼 갱신 추가 가능



```python
s
```


    서울    9631482
    부산    3393191
    인천    2632035
    대전    1490158
    dtype: int64




```python
# s 시리즈의 부산의 인구 값을 8630000 으로 갱신
s['부산'] = 8630000
s
```


    서울    9631482
    부산    8630000
    인천    2632035
    대전    1490158
    dtype: int64




```python
# 시리즈에 새로운 데이터 추가
s['대구'] = 1875000
s
```


    서울    9631482
    부산    8630000
    인천    2632035
    대전    1490158
    대구    1875000
    dtype: int64




```python
# 시리즈의 데이터 삭제 : del 명령 사용
del s['대전']
s
```


    서울    9631482
    부산    8630000
    인천    2632035
    대구    1875000
    dtype: int64





### Series 함수

#### **Series size, shape, unique, count, value_counts 함수**
 - size 속성 : 개수 반환
 - shape 속성 : 튜플형태로 shape반환
 - unique: 유일한 값만 ndarray로 반환
 - count : NaN을 제외한 개수를 반환
 - mean: NaN을 제외한 평균 
 - ★ __value_counts__ : NaN을 제외하고 각 값들의 빈도를 반환 ★ 매우 자주 사용!



```python
s1 = pd.Series([1, 1, 2, 1, 2, 2, 2, 1, 1, 3, 3, 4, 5, 5, 7, np.NaN])
s1
```


    0     1.0
    1     1.0
    2     2.0
    3     1.0
    4     2.0
    5     2.0
    6     2.0
    7     1.0
    8     1.0
    9     3.0
    10    3.0
    11    4.0
    12    5.0
    13    5.0
    14    7.0
    15    NaN
    dtype: float64




```python
len(s1) # NaN 값 포함
```


    16




```python
s1.size # NaN 값 포함한 개수
```


    16




```python
s1.shape # 차원을 표현하기 때문에 튜플 형태로 출력
```


    (16,)




```python
s1.unique() # 중복값을 제거한 원소 값 출력
```


    array([ 1.,  2.,  3.,  4.,  5.,  7., nan])




```python
s1.count() # NaN 값을 제거한 원소의 개수 
```


    15




```python
a = np.array([2,2,2,2,2, np.NaN]) # 결측치 포함
b = pd.Series(a)
a.mean()  # numpy 패키지의 array를 평균 계산한 것이기 때문에 NaN이 포함되면 계산이 불가함 -> NaN 반환
b.mean()  # 시리즈는 기본 NaN 값을 제외하고 계산하도록 설정이 되어 있음 -> 계산 결과 반환됨
```


    nan


    2.0




```python
s1.mean()
```


    2.6666666666666665




```python
s1
```


    0     1.0
    1     1.0
    2     2.0
    3     1.0
    4     2.0
    5     2.0
    6     2.0
    7     1.0
    8     1.0
    9     3.0
    10    3.0
    11    4.0
    12    5.0
    13    5.0
    14    7.0
    15    NaN
    dtype: float64


```python
s1.value_counts() # 각 원소들은 같은 값끼리 그룹을 만들고 개수를 세서 반환
```


    1.0    5
    2.0    4
    3.0    2
    5.0    2
    7.0    1
    4.0    1
    dtype: int64
