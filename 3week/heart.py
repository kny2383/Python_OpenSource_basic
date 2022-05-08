## 변수 선언  ##
num = "" # 숫자 입력 받는 문자열 변수
i, k = 0, 0 # 반복문 변수 초기화
heartNum = 0 # 하트 개수 변수
ch = "" # 입력한 숫자를 담는 변수
heartStr = "" # 하트를 heartStr에 누적한다

## 메인 코드 ##
if __name__ == "__main__" :
    num = input("숫자를 여러 개 입력하세요 : ")
    print("")
    ch = num[i] # 처음엔 ch = num[0] 
    while True:
        heartNum = int(ch)
        heartStr = ""
        for k in range(0, heartNum) :
            heartStr += "\u2665"
            k += 1
        print(heartStr)
# 2021041059_김나영
        i+=1
        if (i > len(num) -1) :
            break

        ch = num[i] # num[0]에서 i +=1을 통해 입력한 그 다음 숫자로 넘어가 ch에 담아준다
