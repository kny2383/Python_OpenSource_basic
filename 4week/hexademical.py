import random # 임의의 수 랜덤 생성 하기 위한 모듈 사용

## 전역 변수 선언 ##
hexList = [] # 16진수 저장할 리스트
i,j=0,0 # for문에서 사용할 변수


#2021041059 김나영

## 메인 코드 ##
if __name__ == "__main__" :
    for i in range(0,10) : # 임의의 16진수 10개 생성
        data = hex(random.randrange(0,100000)) #hex() : 매개변수 x에 정수 값을 입력 받아서 16진수로 변환하여, 변환한 값을 반환하는 함수
        hexList.append(data) # append() : 리스트의 마지막에 인자로 전달된 data를 추가한다.

    print('정렬 전 데이터 : ', end = '') # -end= "" : print 문을 이용해 출력을 완료한 뒤의 내용 수정 가능

    # 리스트 컴프리헨션 :
        # numbers = []
        # for n in range(1, 10+1) :
            # numbers.append(n)
        #이러한 코드를 컴프리헨션으로 표기하면
        # [x for x in range(10)] 이와 같다.

    [print(num, end = ' ') for num in hexList] # 리스트 컴프리헨션을 이용해 출력

    # 선택정렬
    for i in range(0, len(hexList) -1) : 
        for j in range ( i+1, len(hexList)) :
            if int(hexList[i], 16) > int (hexList[j], 16) :
                data = hexList[i]
                hexList[i] = hexList[j]
                hexList[j] = data

    print('\n정렬 후 데이터 : ' , end = '')
    [print(num, end= ' ') for num in hexList] # 리스트 컴프리헨션을 이용해 출력
    
