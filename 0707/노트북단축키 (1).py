#!/usr/bin/env python
# coding: utf-8

# 0. 셀 실행
#     - ctrl + enter : 현재 셀 실행
#     
#     - shift + enter : 현재 셀 실행 후 포커스를 다음 셀로 이동(다음셀이 없으면 빈 셀을 하나 추가)

# 1. 셀 선택 모드
#     - [esc] 또는 [ctrl]+m을 눌러서 셀 테두리가 파란색이 된 상태(선택모드)
#     
#     - 위로 셀 추가 : a
#     
#     - 아래로셀 추가 : b  
#     
#     - 선택 셀 삭제 : dd  d키를 두번 누름
#     
#     - 선택 셀 잘라내기 : x
#     
#     - 선택 셀 복사 : c  붙여넣기 : p
#     
#     - 선택셀과 아래 셀 합치기: shift + m
#     
#     - 실행결과 열기 / 닫기 : o
#     
#     - MarkDown으로 변경 : m    
#     
#     - code로 변경 : y
#     
#     - 파일 저장 : ctrl + s 
#     
#     - 선택된 셀의 입력모드로 돌아가기 enter
#     

# 2. 편집 모드
# 
#     - enter키를 눌러(셀 내부 클릭) 셀 테두리가 초록색이 된 상태
#     
#     - 선택 셀의 전체 코드 선택 : ctrl + a
#     
#     - 선택 셀 내 실행 취소 : ctrl + z
#     
#     - 선택 셀 내 다시 실행 : ctrl + y
#     
#     - 커서 위치 주석 처리 : ctrl + /
#     
#     - 선택 셀 코드 실행 : ctrl + enter
#     
#     - 선택 셀 코드 실행 후 다음 cell로 이동(없으면 새로추가):shift+enter
#     
#     - 커서위치에서 셀을 둘로 나누기
#     
#     - shift+ctrl + [-]

# # 마크다운 제목(headline) 기호
# # A head1#
# ## A head2##
# ### A head3###
# #### A head4####
# ##### A head5#####
# 

# - 노트북 파일 다운로드(.ipynb - .py)
#     - 메뉴 file - 다운로드 - 종류.py 선택

# In[1]:


a = 'hello'
print(a)


# In[2]:


a

