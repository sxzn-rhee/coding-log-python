#02_for_range.py (for / range/ 누적 total / +=) 
#반복

def main():
    nums = [3, 5, 10, -2, 7] #리스트: 순서 있는 값의 묶음
    total = 0 #누적 합계 시작값을 0으로 잡은 것
    for n in nums: #for = 반복문, n= 반복할 때마다 리스트에서 꺼낸 값이 들어가는 변수(임의), nums를 돌면서 각 값을 n에 넣어라
        total = total + n #누적의 기본형, 현재 total에 n을 더해서 다시 total 에 저장
    print("합계:", total) #반복문 끝나면 합계 출력
    total2 = 0  
    for n in nums: #축약 누적, 자주 쓰는 누적 문법:+=
        total2 += n 
    print("합계2:", total2) #만약 print를 들여쓰면 합계가 누적되는 과정이 매 반복마다 계속 출력됨

    for i in range(5): #range(5) = 0,1,2,3,4(끝 5는 포함 안 함) 파이썬 range는 끝은 미포함이 기본 규칙임
        print("i =", i) #목적이 반복문이 돌 때마다 값이 바뀌는 반복용 변수를 매번 출력하려고 print를 안으로 들여 씀

    for i in range(2, 6): #range(2, 6)=2,3,4,5
        print("2~5:", i)
    for i in range(0, 11, 2): #range(시작, 끝, 증가)
        print("짝수:", i)

if __name__ == "__main__":
    main()
