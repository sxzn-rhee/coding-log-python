#실습1- if/elif/else (조건문) + 논리(and/or/not)

def main(): 
    x = 7 
    print("x =", x)
#def = 함수 정의(만들기) 시작 
#main = 함수 이름(임의로 지은 이름), :을 치면 "다음 줄부터 이 함수 안"이라는 뜻
#여기서부터 들여쓰기 4칸
#x는 변수 이름, =대입(넣겠다는 의미, 같다는게 아님), 7(정수,int)
#print()-화면에 출력하겠다, "x ="문자열(string), ,x-쉼표로 값을 여러 개 넣으면 자동으로 띄어쓰기 포함해서 출력됨

    if x > 10: 
        print("10보다 큼") #if 조건문 시작, 비교 연산 -> 결과는 Trune/False
                         # 다음 줄부터 if 블록(조건이 True일 때 실행될 부분) 시작 -> 위 조건이 True 일 때만 실행
    elif x == 10: 
        print("10이랑 같음") #elif: 앞 if가 False 이면 그 다음 조건 검사, ==: (비교) =(대입)vs==(비교)
    else: 
        print("10보다 작음")

    is_even = (x % 2 == 0)
    if is_even and x < 100:     
        print("짝수 & 100 미만")
    if (not is_even) or (x == 7): 
        print("홀수이거나 7이다")

if __name__ == "__main__": 
    main()
    #이 파일을 직접 실행했을 떄만 아래를 실행해라
    #나중에 다른 파일에서 이 파일을 import 했을때 자동 실행되면 곤란하니까
