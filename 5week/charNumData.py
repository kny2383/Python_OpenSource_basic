import random

##2021041059_김나영
##함수 선언##
def getNumber(strData) : # 문자열을 넘겨받아서 숫자만 추출하고 결과로 반환하는 함수
    numStr = ''
    for ch in strData :
        if ch.isdigit() : # 숫자인지 확인하는 과정
            numStr += ch
    return int(numStr)

## 전역 변수 선언 ##
data = []
i, k = 0, 0

## 메인 코드 ##
if __name__ == "__main__" :
    for i in range(0,10) :
        tmp = hex(random.randrange(0,100000))
        tmp = tmp[2:] # 16진수 앞에 붙은 0x 제거
        data.append(tmp)

    print('정렬 전 데이터 : ', end = '')
    [print(num, end= ' ') for num in data]

    for i in range(0, len(data)-1) :
        for k in range(i+1, len(data)):
            if getNumber(data[i]) > getNumber(data[k]) :
                tmp = data[i]
                data[i] = data[k]
                data[k] = tmp

    print('\n정렬 후 데이터 : ', end = '')
    [print(num, end= ' ') for num in data]
