```python
#설정변경코드
#변수 명이 두번 이상 출력되어도 모두 콘솔에서 보여줄 것
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"

# InteractiveShell.ast_node_interactivity : 'all' | 'last' | 'last_expr' | 'none' (기본값은 'last_expr')
```


```python
# 모듈 import
import numpy as np
import pandas as pd
```





# pandas 데이터처리 및 변환 관련 함수



### 데이터 개수 세기

- 가장 간단한 분석은 데이터의 개수를 세는 것임
- `count()` 함수 사용
    
    - NaN 값은 세지 않는다
    
      


```python
# 시리즈에서 개수 세기
s = pd.Series(range(10))
s[3] = np.nan
s
```


    0    0.0
    1    1.0
    2    2.0
    3    NaN
    4    4.0
    5    5.0
    6    6.0
    7    7.0
    8    8.0
    9    9.0
    dtype: float64


```python
s.count()
# NaN 값을 제외하고 세서 총 9개로 출력
```


    9





### 난수
- 난수 : seed(값) 라는 함수를 사용할 수 있음
- seed의 의미 : 난수 알고리즘에서 사용하는 기본 값
    - 시드값이 같으면 동일한 난수가 발생함
    
      


```python
np.random.seed(3)  # 난수값을 고정하기 위해 seed() 함수 사용
# 데이터프레임 예제 생성 시 원소값을 고정하기 위해 쓰는 것임
np.random.randint(5, size=4)
# seed(), 난수발생함수를 동시에 사용해야 난수 데이터를 고정할 수 있음
```


    array([2, 0, 1, 3])




```python
np.random.randint(5, size=4)
# seed() 함수가 같이 실행되지 않기 때문에 실행시마다 다른 결과가 반환됨
```


    array([0, 2, 1, 2])




```python
# 예제 데이터프레임 생성
# 데이터 0-4범위의 난수 발생, 4행4열, 실수형데이터로 생성
# np.random.seed(3)
# df = pd.DataFrame(np.random.randint(5,size=(4,4)),dtype=float)
# 전체 데이터타입을 float으로 설정함 (dtype = float)
# 기본값은 정수
# df

np.random.seed(3)
df1=pd.DataFrame(np.random.randint(5,size=(4,4))) #기본 정수

df1.iloc[2,3] =np.nan
df1
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 데이터프레임의 count()는 각 열에 대한 연산을 진행 - 각 열의 유효한 원소의 개수를 반환
# NaN 값은 제외
# 일반적으로 데이터에 결측값의 유무를 확인하기 위해 사용하는 함수임

df1.count()
```


    0    4
    1    4
    2    4
    3    3
    dtype: int64





### count 함수 사용 예제 (titanic 데이터 활용)

- 타이타닉 승객 데이터 사용
    - seaborn 패키지 내에 data로 존재
    - 데이터셋 읽어오기 : 패키지명.load_dataset("data명")



```python
import seaborn as sns  # 그래프 패키지

titanic = sns.load_dataset('titanic')
titanic.head(10) # head는 기본값이 5개의 데이터만 반환
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>8.4583</td>
      <td>Q</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Queenstown</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>1</td>
      <td>male</td>
      <td>54.0</td>
      <td>0</td>
      <td>0</td>
      <td>51.8625</td>
      <td>S</td>
      <td>First</td>
      <td>man</td>
      <td>True</td>
      <td>E</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>2.0</td>
      <td>3</td>
      <td>1</td>
      <td>21.0750</td>
      <td>S</td>
      <td>Third</td>
      <td>child</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>27.0</td>
      <td>0</td>
      <td>2</td>
      <td>11.1333</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1</td>
      <td>2</td>
      <td>female</td>
      <td>14.0</td>
      <td>1</td>
      <td>0</td>
      <td>30.0708</td>
      <td>C</td>
      <td>Second</td>
      <td>child</td>
      <td>False</td>
      <td>NaN</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
# titanic 데이터프레임의 각 열의 원소 개수를 산출 - count() 함수 이용
titanic.shape   # (891,15) 승객 891명
titanic.count() # 시리즈 반환 - 전체 행에 대해 값 차이가 나는 열은 결측치가 있다는 의미
# 각 열의 유효한 원소의 개수 반환
```


    (891, 15)


    survived       891
    pclass         891
    sex            891
    age            714
    sibsp          891
    parch          891
    fare           891
    embarked       889
    class          891
    who            891
    adult_male     891
    deck           203
    embark_town    889
    alive          891
    alone          891
    dtype: int64

## __의식적으로라도 count()와 info() 함수를 사용해서__ 

## __데이터의 정보를 보여주는 것이 좋음!!!!!__





###  카테고리 값 세기

- 시리즈의 값이 정수,문자열 등 **카테고리 값**인 경우에
- _시리즈.value_counts()_  메서드를 사용해 <u>각각의 값이 나온 횟수</u>를 셀 수 있음
- 파라미터 **normalize=True** 를 사용하면 각 값 및 범주형 데이터의 비율을 계산
    - _시리즈.value_counts(normalize=True)_



```python
np.random.seed(1)
s2 = pd.Series(np.random.randint(6, size = 100))
s2.head(10)
s2.tail()
```


    0    5
    1    3
    2    4
    3    0
    4    1
    5    3
    6    5
    7    0
    8    0
    9    1
    dtype: int32


    95    4
    96    5
    97    2
    98    4
    99    3
    dtype: int32




```python
s2.value_counts() # 0, 1, 2, 3, 4, 5 각 값이 몇 번 나왔는지 결과 반환
# 왼쪽 줄은 인덱스, 오른쪽 줄은 실제 값에 해당
```


    1    22
    0    18
    4    17
    5    16
    3    14
    2    13
    dtype: int64





### 범주형 데이터에 value_counts() 함수 적용
- 범주형 데이터 : 관측 별과가 몇개의 범주 또는 항목의 형태로 나타나는 자료
    - ex. 성별(남,여), 선호도(좋다, 보통, 싫다), 혈액형(A,B,O,AB) 등



```python
titanic.head(2)
# 맨 위에서 두 행까지 추출
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
# alive 열 : 생존여부가 yes/no 로 표시되어 있음
titanic['alive'].dtype  # dtype('0') -> Object type(문자열)이라는 뜻!
titanic['alive'].value_counts()
type(titanic['alive'])
```


    dtype('O')


    no     549
    yes    342
    Name: alive, dtype: int64


    pandas.core.series.Series




```python
# 생존자/ 사망자 비율 계산
titanic['alive'].value_counts(normalize=True)
titanic['alive'].value_counts(normalize=True) * 100
```


    no     0.616162
    yes    0.383838
    Name: alive, dtype: float64


    no     61.616162
    yes    38.383838
    Name: alive, dtype: float64





### 데이터프레임에 value_counts() 함수 사용

- 행을 하나의 value로 정의해서 동일한 행이 몇 번 나타났는지를 반환함

- 행 데이터의 경우가 인덱스로 설정됨
    - ex) MultiIndex([(4, 0), (2, 2), (6, 0)], 
    
- 계수된 값이 value로 표시되는 series로 반환됨

    


```python
# 예제 df
df = pd.DataFrame({'num_legs': [2, 4, 4, 6],
                   'num_wings': [2, 0, 0, 0]},
                  index=['falcon', 'dog', 'cat', 'ant'])
df
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>falcon</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>cat</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>ant</th>
      <td>6</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.value_counts().index
# 동일한 값을 가지는 행의 개수를 반환 (제일 오른쪽 줄에 출력)
df.value_counts()
```


    MultiIndex([(4, 0),
                (2, 2),
                (6, 0)],
               names=['num_legs', 'num_wings'])


    num_legs  num_wings
    4         0            2
    2         2            1
    6         0            1
    dtype: int64




```python
# 예제 df
df1
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.value_counts() # 행 원소로 NaN값이 있는 필드는 계수하지 않음
```


    0  1  2  3  
    0  0  0  3.0    1
    2  0  1  3.0    1
          4  4.0    1
    dtype: int64


```python
df1.value_counts().shape
df1.value_counts().sort_index().index
```


    (3,)


    MultiIndex([(0, 0, 0, 3.0),
                (2, 0, 1, 3.0),
                (2, 0, 4, 4.0)],
               names=[0, 1, 2, 3])





