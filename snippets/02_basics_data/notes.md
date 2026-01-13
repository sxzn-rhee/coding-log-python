# 2026-01-133 - python 기초 정리 (01_import/as/ from + 02_basics_data)

## 0) 오늘 목표
- 파이썬 파일(.py)을 직접 실행해보기
- import / from / as 개념 이해 
- 실행 순서(함수/들여쓰기), 변수 대입(=), 누적(+=)
- 리스트([]) vs 딕셔너리({}) + dict.get()

---

## 1) 용어: 파일 / 폴더 / 경로
- 폴더(folder): 파일을 담는 상자
- 파일(file): 실제 내용이 들어있는 것
- 경로(path): "어디에 있는지"를 알려주는 주소
  - 예: snippets/02_basics_data/01_run_order.py
  - '/'는 폴더 안으로 들어간다는 뜻 (구분자)

--- 

## 2) 실행: 파이썬 파일(.py)을 터미널에서 실행하기 
### 실행 명령어
```bash 
python3 snippets/01_import_as_from/example.py
```
실수 주의: 파일 뒤에는 / 붙이면 안됨. 폴더로 인식하기 떄문




--- 

## 1. import/from/as (라이브러리 가져오기)

### (1) import X
```bash
import math
```
- 의미: math 라는 '모듈(기능 묶음)' 을 통쨰로 가져오기
- 사용법: math.기능이름() 형태로 사용
```bash
math.sqrt(9)
```
### (2) form X import Y
```bash
from math import sqrt
```
- 의미: math 안에서 sqrt 기능만 꺼내오기
- 사용법: sqrt() 를 바로 사용 가능
```bash
sqrt(16)
```
### (3) import X as 별명(alias) 
```bash
import datetime as dt 
```
- 의미: datetime 을 앞으로 dt라는 별명(alias)로 부르겠다
- 사용법:
```bash
dt.datetime.now()
```
### 정리 포인트
- import math -> math.sqrt() 처럼 "모듈 이름" 붙여서 사용
- from math import sqrt -> sqrt() 처럼 바로 사용
- as -> 긴 이름을 짧게 쓰기 위한 별명 

--- 

## 2. print() (화면에 출력하기)
```bash 
print("hello")
``` 
- 의미: 괄호 안 내용을 터미널(콘솔)에 보여준다

- "hello"/ 'hello' 는 문자열
- 따옴표가 없으면 파이썬은 "변수 이름"으로 이해하려고 해서 에러 날 수 있음

---

## 3. 함수 def/main()/들여쓰기
### (1) 함수 정의(def) 
```bash 
def main(): 
    print("inside main")
```
- def = 함수를 "정의"한다. (아직 실행 아님)
- 함수 안 코드는 반드시 들여쓰기(보통 4칸)해서 소속을 표시해준다. 

### (2) 함수 호출 (실행)
```bash
main()
``` 
- main 만 쓰면 "함수 그 자체(대상)" 이고, main()은 "함수를 실행하라"라는 뜻.

### (3) 실행 순서 (파일 바깥 vs 함수 안)
- 파일 바깥(들여쓰기 없음): 파일 실행하면 바로 실행됨
- 함수 안(들여쓰기): 함수를 호출해야 실행됨

ex. A(파일 바깥)-> 바로 실행, 
    B(함수 안)-> main() 호출해야 실행


---

## 4. if name == "main" : 직접 실행 안전 장치
```bash
if __name__ == "__main__": 
    main()
```
- 의미: 이 파일을 "직접 실행할 대만" main()을 실행해라. 
- 나중에 이 파일을 다른 파일에서 import로 가져오면, 자동응로 실행되면 곤란할 수 있어서 방지하는 패턴

---

## 5. 대입(=) vs 누적(+=) 
### (1) 대입(=)
```bash
total = 0
```
- 의미: total 이라는 변수에 0을 "넣는다" 

### (2) 누적(+=)
```bash
total += 10 
```
- 의미: total 에 10을 더해서 다시 total 에 저장한다. 
- total += -> total = total + 10 

---

## 6. 리스트[] vs 딕셔너리{} 
### (1) 리스트 - 순서가 있는 여러 값
```bash
fruits = ["사과", "바나나", "포도"]
# 꺼낼 때는 "몇 번쨰" 로 꺼냄 (0부터 시작)
fruits[0] #"사과" 
```

### (2) 딕셔너리 - key(이름표)로 값을 저장 
```bash 
person = {"name": "시언", "age": 26}
#꺼낼 떄는 key 로 꺼냄
person["name"]
```
- 중요한 포인트: {} 는 "딕셔너리를 만들 때" 
- []는 "리스트/딕셔너리에서 값을 꺼낼 떄" 둘 다 사용됨
ex. fruits[0] , person["name"]

---

## 7. dict.get() - 안전하게 꺼내기
```bash
sores.get("english", 0)
```
- 의미: english가 있으면 그 값, 없으면 0 꺼내라는 것.
- scores["english"]처럼 []로 꺼내면 키가 없을 때 KeyError 발생
- get 은 없을 때 기본값으로 정해놓은 값을 주니까 누적합/카운팅에 자주 씀. 
