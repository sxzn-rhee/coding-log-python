#03_while_break.py (while/break/continue)
#조건 반복/탈출

def main(): 
    n = 1 
    while n <= 5:   
        print("n =", n) #while = 조건이 True인 동안 계속 반복
        n += 1 #n을 1 증가 시키는 것. 이 줄이 없으면 n이 1이라서 무한 반복됨. 
    print("----- break 예시 -----")

    n = 1 
    while True: #True는 항상 True라서 무한 반복 형태, 대신 break 로 탈출할 거임
        if n == 4: #if 는 조건문이 True 일 때만 실행
            break #반복문 즉시 종료(탈출) 
        print("break 전:", n)
        n += 1 
    print("---- continue 예시 ----")

    for i in range(1, 8): 
        if i % 2 == 0: 
            continue #continue = 이번 회차는 건너뛰고 다음 반복으로 넘어감(아래 print 실행 안하고 바로 다음 i로 간다는 뜻)
        print("홀수만 출력:", i) #continue에 걸리지 않은 홀수만 출력됨


if __name__ == "__main__": 
    main()