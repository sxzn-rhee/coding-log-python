# 2026-01-14 
03 - control folw (조건/반복/흐름 제어)

## 0. 배우는 것 
- **if**: 조건에 따라 실행할 코드를 나눈다
- **for**: 정해진 자료(리스트/범위)를 순서대로 반복한다
- **while**: 조건이 True인 동안 계속 반복한다
- **break/continue**: 파이썬에서 "블록(묶음)"을 만드는 규칙

--- 

## 1. 들여쓰기(Indentation) 규칙
- 파이썬은 '{}' 대신 **들여쓰기**로 "여기부터 여기까지가 같은 묶음(블록)"임을 표시한다
- ':'(콜론) 다음 줄부터 **한 단계 들여쓰기**가 시작된다
- 블록이 끝나면 **다시 들여쓰기 밖으로** 나온다. 
```bash 
if True:
    print("이 줄은 if 블록 안")
print("이 줄은 if 블록 밖")
```
---
## 2. if (조건문)

### 2-1) 기본 형태
if 조건: 
    조건이 True일 때 실행

### 2-2) else/elif
if 조건 A: 
    A가 True일 때
elif 조건 B: 
    A는 False이고 B가 True일 때
else: 
    위가 전부 False 일 때

### 2-3) 비교 연산자
- == 같다
- != 다르다
- > 크다 , < 작다 
- >= 이상, <= 이하
---
## 3. for (반복문)

### 3-1) 리스트를 반복
```bash
nums = [3, 5, 10]
for n in nums: 
    print(n)
```
- nums에서 값을 하나씩 꺼내서 n에 넣고 블록을 실행한다. 
- 블록 안의 코드는 요소 개수만큼 반복된다. 

### 3-2) range()로 반복
```bash
for i in range(5):
    print(i)
```
- range(5)는 0,1,2,3,4를 만든다 (5는 포함 안함)
```bash
for i in range(2, 6):
    print(i)
```
- range(2, 6)는 2,3,4,5

### 3-3) for 블록 안/밖의 차이
- for 블록 안에 있으면: 반복할 때마다 실행
- for 블록 밖에 있으면: 반복이 끝난 뒤 1번만 최종적으로 실행
```bash
nums = [1, 2, 3]
total = 0
for n in nums 
    total += n 
print("합계:", total)
- total += n 은 반복마다 실행돼야 하니까 for 안 
- print(합계)는 최종 결과 1번만 찍으면 되니까 for 밖
``` 
---
## 4. while (조건 반복)

### 4-1) 기본 형태 
```bash 
n = 1 
while n <= 5:   
    print(n)
    n += 1 
```
- while 은 조건이 True인 동안 블록을 반복한다. 
- n += 1 이 없으면 n이 안변해서 무한 반복이 될 수 있다. 

### 4-2) while True (무한 반복 형태)
```bash
n=1 
while True: 
    if n == 4: 
        break
    print("break 전:", n)
    n += 1 
```
- while True 는 조건이 항상 True라 기본적으로 무한 반복
- break를 만나면 반복문이 즉시 종료됨
- n += 1은 매 반복마다 실행되면서 n을 변화시킴 (순서는 위에서 아래로 한줄씩 실행)

### 4-3) break / continue
- **break**: 반복문 즉시 종료(탈출)
- **continue**: 이번 반복은 건너뛰고 다음 반복으로 넘어감 
```bash
for i in range(1,6)
    if i == 3: 
        continue
    print(i)
```
-> 3일 때는 print를 건너뛰고 다음 반복으로 넘어간다.

---

## 실행 방법 (레포 루트)
```bash 
python3 snippets/03_control_flow/01_if.py
python3 snippets/03_control_flow/02_for_range.py
python3 snippets/03_control_flow/03_while_break_continue.py
```

--- 

### 헷갈렸던 포인트 체크리스트
```bash
n = 1
while True:
    if n == 4:
        break
    print("break 전:", n)
    n += 1
```
- 만약 n += 1을 if 안에 넣으면 앞에 break 때문에 뒤에 절대 실행 안됨 (n 은 계속 1이라서 print1만 계속 찍힘)
- print가 break 아래에 있으면 
  1. 조건이 True일 때는 break가 먼저 실행돼서 print까지 도달 못하고
  2. 조건이 False일 때는 if 블록 자체를 통째로 건너뛰니까 print도 실행이 안됨 -> 그래서 항상 실행 불