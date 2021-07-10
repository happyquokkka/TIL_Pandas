### 데이터 정렬 - 정렬 함수 사용

- `sort_index()` : 인덱스를 기준으로 정렬

- `sort_value()` : 데이터 값을 기준으로 정렬

  

#### 시리즈 정렬

* `ascending = True/False` : True는 오름차순, False는 내림차순 정렬

* 생략하면 오름차순 정렬 진행

  


```python
# 예제 시리즈
s2
```


    0     5
    1     3
    2     4
    3     0
    4     1
         ..
    95    4
    96    5
    97    2
    98    4
    99    3
    Length: 100, dtype: int32




```python
s2.value_counts() # 반환 값을 기준으로 정렬된 시리즈
# 값에 따라 인덱스가 나타나게 됨
s2.value_counts().sort_index() # 인덱스 기준 정렬 : 오름차순 정렬이 기본
s2.value_counts().sort_index(ascending=False) # 인덱스 기준 내림차순 정렬
```


    1    22
    0    18
    4    17
    5    16
    3    14
    2    13
    dtype: int64


    0    18
    1    22
    2    13
    3    14
    4    17
    5    16
    dtype: int64


    5    16
    4    17
    3    14
    2    13
    1    22
    0    18
    dtype: int64




```python
s2.value_counts().sort_values(ascending=True) # 원소값을 기준으로 오름차순 정렬
s2.value_counts().sort_values(ascending=False) # 원소값을 기준으로 내림차순 정렬
```


    2    13
    3    14
    5    16
    4    17
    0    18
    1    22
    dtype: int64


    1    22
    0    18
    4    17
    5    16
    3    14
    2    13
    dtype: int64




```python
s2.sort_values()  # 0부터 5까지의 원소값을 기준으로 오름차순 정렬
```


    57    0
    38    0
    39    0
    85    0
    28    0
         ..
    71    5
    40    5
    46    5
    11    5
    0     5
    Length: 100, dtype: int32





### 데이터 프레임 정렬

- `df.sort_values()` : 특정열 값 기준 정렬
  - 데이터프레임은 2차원 배열과 동일하기 때문에
    - <u>정렬시 기준열</u>을 줘야한다. __by 인수 사용 : 생략 불가__
    - _by = 기준열, by=[기준열1,기준열2] (복수로 사용 가능/ 1번 기준열에서 동일한 행만 2번 기준열을 사용해서 한번 더 그 부분만 정렬!)_
  - 오름차순/내림차순 : ascending = True/False (생략하면 오름차순)

- `df.sort_index()` : 데이터프레임의 인덱스 기준 정렬
  - 오름차순/내림차순 : ascending = True/False (생략하면 오름차순)



```python
# 예제 df1
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
# df1.sort_values() / 에러 발생 (by 인수 생략해서)
```


```python
df1.sort_values(by = 0, ascending=True) # 0번 열을 기준으로 오름차순 정렬
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
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
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
df1.sort_values(by = 0, ascending=False) # 0번 열을 기준으로 내림차순 정렬
```


```python
df1.sort_values(by = [0,1], ascending = True)
# 0번 열에서 같은 데이터는 1번 열을 기준으로 재정렬
# 0번 열에서 2라는 데이터가 중복으로 등장하므로 그 값을 갖는 행의 1번 열을 오름차순으로 재정렬
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
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>

</div>




```python
# df 확인
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



### 데이터프레임의 index 를 기준으로 정렬


```python
df.sort_index()
# 기본값이 오름차순이므로 a, b, c... 의 순서대로 정렬됨
df.sort_index(ascending=False) # 인덱스 기준으로 내림차순 정렬
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
      <th>ant</th>
      <td>6</td>
      <td>0</td>
    </tr>
    <tr>
      <th>cat</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>falcon</th>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>

</div>


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

