#과자가 1,500이고 아이스크림이 1,000원 일 때 과자 5개 아이스크림 7개를 샀을 때 총금액을 출력해보세요. 
과자 = 1500
아이스크림 = 1000 
total = 과자*5 + 아이스크림*7 
print(total)

#원/달러 환율이 1,290원일 때 900달러에 대한 원화를 계산
달러 = 1290
원화 = 900*달러
print(원화)

## 파이썬 문자열 
### 문자열 인덱싱
### 문자열
lang = "PYTHON3"
print(lang[0])

### 문자열 슬라이싱 
lang = "PYTHON3"
print(lang[0:7])

#<연습문제> 주민등록번호 801230-1234567에서 연월일 부분만 출력해보기
reg_num = "801230-1234567"
print(reg_num[:6])
# 다음 차량 번호에서 끝의 번호 네 자리를 출력하세요
car_num = "12가 1234"
print(car_num[4:])
#다음 코드의 실행 결과를 예측하세요
data = "ABC"
print(data[:][:][:][-1])
#연속해서 같은 문자열을 다시 슬라이스, 결국 ABC가 되고, ABC의 [-1]값인 C가 출력됨

##2.4 문자열 주요 함수
### 문자열 합치기_문자열 바인딩
year = "2026" 
month = "01"
day = "16"
date = year + "-" + month + "-" + day
print(date)

###문자열 반복
lang = "python"
print(lang * 3)
print("-" * 20)

###대문자와 소문자 -> 기존의 문자열 변경이 아님, 새로운 문자열 객체가 리턴됨
lang = "python3"
print(lang.upper())
print(lang.lower())

###문자열 분리 _ split 함수 사용
date = "2026-01-16" 
print(date.split('-'))

###문자열 변경 _ replace 함수 사용(정수, 실수, 문자열은 값을 변경할 수 없는 타입) 
lang = "Python3"
lang2 = lang.replace('3' , '4')
print(lang2)

lang = "Python3"
lang2 = lang[:6] + '4'
print(lang2)

price = "1,000,000"
price = price.replace(",", "")
print(price)

###문자열의 길이와 공백 제거 
#문자열의 길이는 len 내장함수로 알 수 있음
date = "2026-01-16"
print(len(data))
#문자열에 공백이 있는 경우
lang = "    Python3.   "
lang = lang.strip()
print(lang)

###<연습문제> 1. a라는 변수가 'hello world'라는 문자열을 바인딩하고 있을 떄 a의 값을 'hi world'로 변경하기 
a = "hello world" 
a = a.replace("hello", 'hi')
print(a)
### 2. " 2026/01/16 "에서 공백을 제거하고 '/'를 '-'로 변경하여 "2026-01-16"으로 변경해보세요
a = "2026/01/26"
a = a.strip()
a = a.replace("/", "-")
print(a)

##2.5 문자열 포매팅 
#정수: %d, 실수: %f. 문자열: %s 형식 지정 문자열에서 지정된 타입의 값이 전달됨
name = '철수'
score = 290
average = 290/3
print("%s의 총점은 %d, 평균은 %f입니다. " % (name, score,average))

#기본자릿수 10칸으로 지정, 우측 정렬: {변수: >10}
#천 단위에서 쉼표를 표시하려면 {변수: ,}

btc_symbol = "BTC/KRW"
btc_price = 28300000

doge_symbol = "DOGE/KRW" 

###f-string 
name = "철수"
score = 290
average = 290/3
print(f"{name}의 총점은 {score}, 평균은 {average}입니다.")

btc_symbol = "BTC/KRW"
btc_price = 28300000

doge_symbol = "DOGE/KRW"
doge_price = 193

print(f"암호화폐: {btc_symbol} 현재가: {btc_price}")
print(f"암호화폐: {doge_symbol}, 현재가: {doge_price}")

btc_symbol = "BTC/KRW"
btc_price = 28300000

doge_symbol = "DOGE/KRW"
doge_price = 193

print(f"암호화폐: {btc_symbol: >10} 현재가: {btc_price: >10,}")
print(f"암호화폐: {doge_symbol: >10} 현재가: {doge_price: >10,})") 


## 2.6 타입 변한 
### 파이썬: 정수, 실수, 문자열 세 가지 기본 데이터 타입 제공 (서로 다른 타입으로 변경 가능) : 타입 변환

year = "2022"
year2 = int(year)
print(year2)

money = "1,000,000"
money2 = money.replace(',', '')
int(money2)
print(money2)

###정수형을 문자열로 변환 
year = 2026 
date = str(year) + "-01-21"
print(date)
###정수와 실수를 서로 다른 타입으로 변경 
num = 10
num2 = float(num)
print(num2, type(num2))
###정수를 실수로 변경하면 소수점은 버려짐
num = 10.5 
print(int(num))

