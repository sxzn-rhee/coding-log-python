# 01. 실행 순서, 범위
# 파일 열었다고 실행되는게 아님, 함수 안은 호출해야 실행됨, 들여쓰기는 소속을 정함
print("A: 파일을 실행하면 제일 먼저 찍힘(함수 밖)")

def main(): 
    print("B: main() 함수 안 (main을 호출해야 찍힘)")

print("C: 이것도 함수 밖이라 바로 찍힘")

if __name__ == "__main__": 
    main()

# main() 호출 줄(맨 아랫 줄)을 지우고 실행하면 출력이 어떻게 될까? -> A, C만 print 되고 B는 안 나옴
# print("C...")를 함수 안으로 들여쓰기 하면 출력 순서가 어떻게 바뀔까? -> C가 메인 안으로 들어가면, 호출 될 때 찍히니까, A먼저 찍히고 B,C 순서대로 찍히게 됨.
# if __name__ == "__main__": -> 이 파일을 직접 실행했을 떄만, 아래를 실행 main()

# 02. 대입 / 누적 
# = 는 "같다" 가 아니라 "넣어라" 
# +=는 누적(합계) 만들 때 쓰는 핵심 문법 
def main():
    total = 0
    print("처음 total:", total)

    total = total + 5 
    print("total = total + 5 후:", total)

    total += 10 
    print("total += 10 후:", total)

if __name__ == "__main__": 
    main()

#total = 0 : total 이라는 상자에 0을 넣는다. 
#total = total + 5 : 기존 total 값에 5 더한 값을 다시 total 에 넣는다
#total += 10 : 기존 total 값에 10 더한 값을 다시 total 에 넣는다.



# 03. 리스트/딕셔너리 -> [] vs {} 를 각각 언제 쓸까? 
# [] 리스트 : "순서 / 여러 개"
# {} 딕셔너리 : "이름표(key)로 값 꺼내기"
# 왜 t["amount"]에서 [] 를 쓰는지 이해하기 
def main():
    #리스트: 여러 개를 순서대로 담는 통
    fruits = ["사과", "바나나", "포도"]
    print("fruits[0] =", fruits[0])
    print("fruits[2] =", fruits[2])

    #딕셔너리: 키(key)로 값을 찾는 구조 
    person = {"name": "시언", "age": 26} 
    print('person["name"] =', person["name"])
    print('person["age"] =', person["age"]) 

if __name__ == "__main__": 
    main()

#fruits = [] : 리스트 만들기 -> [] 사용
#fruits[0]: 리스트에서 0번째 꺼내기 -> 꺼낼 때도 [] 사용
#person = {} : 딕셔너리 만들기 -> {} 사용 
#person["name"]: 딕셔너리에서 "name" 의 키 값 꺼내기 -> 딕셔너리에서 값을 꺼낼 때도 [] 사용하는게 포인트!! 
# 딕셔너리 : {} 는 만들 때 사용, [] 접근/꺼낼 때 사용 


#04. get 이 왜 필요할까? 에러 방지/ 누적합
#dict["키"]는 키가 없으면 터짐(KeyError)
#dict.get("키", 기본값)은 키 없으면 기본값을 줌(에러가 나지 않고 터지지 않음)
#카테고리별 합산이 왜 get으로 되는지 감 잡기
def main(): 
    scores = {"math": 90}

    #있는 키는 둘 다 가능함
    print('scores["math"] =', scores["math"]) 
    print('scores.get("math", 0) =', scores.get("math", 0))

    #존재하지 않는 키: []는 터지고, get은 기본값을 주니까 안 터짐
    print('scores.get("english", 0) =', scores.get("english", 0))

    #print(scores["english"])는 실행하면 KeyError

if __name__ == "__main__": 
    main()
#english 가 없으니 기본값으로 설정한 0을 주니 안전. 처음 보는 카테고리 가 나오면 0부터 시작해야 누적합이 되니 중요. 
