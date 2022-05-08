import random # random 모듈을 사용하기 위해서 선언

## 전역 변수 선언 부분 ##
dice1, dice2, dice3, dice4, dice5, dice6 = [0]*6 # 0을 6번 쓴 것과 같은 의미
throwCount = 0 # 주사위를 던진 횟수
serialCount = 0 # 연속번호가 나온 횟수 , 둘다 초기화를 해준다

## 메인 코드 부분 ##
if __name__ == "__main__":
    while True: # 무한 반복 수행
        throwCount +=1 # while문 시작하자마자 던진 횟수를 하나 증가시킨다

        # 랜덤으로 주사위 값 배정
        dice1 = random.randrange(1,7) # random.randrange(1,7) -> 1 < = dice1 < 7 
        dice2 = random.randrange(1,7) 
        dice3 = random.randrange(1,7)
        dice4 = random.randrange(1,7)
        dice5 = random.randrange(1,7)
        dice6 = random.randrange(1,7)

        #2021041059 김나영

        if dice1 == dice2 == dice3 == dice4 == dice5 == dice6 :
            print("6개 주사위가 모두 동일한 숫자가 나옴 -->", dice1, dice2, dice3, dice4, dice5, dice6)
            break # break 문은 반복문을 빠져나간다
        elif (dice1 ==1 or dice2 == 1 or dice3 ==1 or dice4 ==1 or dice5 ==1 or dice6 ==1) and \
        (dice1 ==2 or dice2 == 2 or dice3 ==2 or dice4 ==2 or dice5 ==2 or dice6 ==2) and \
        (dice1 ==3 or dice2 == 3 or dice3 ==3 or dice4 ==3 or dice5 ==3 or dice6 ==3) and \
        (dice1 ==4 or dice2 == 4 or dice3 ==4 or dice4 ==4 or dice5 ==4 or dice6 ==4) and \
        (dice1 ==5 or dice2 == 5 or dice3 ==5 or dice4 ==5 or dice5 ==5 or dice6 ==5) and \
        (dice1 ==6 or dice2 == 6 or dice3 ==6 or dice4 ==6 or dice5 ==6 or dice6 ==6) :
            serialCount += 1 # 1~6의 연속번호가 나온 횟수를 하나씩 더해준다
             
print("6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 -->", throwCount)

print("6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수- ->", serialCount)
