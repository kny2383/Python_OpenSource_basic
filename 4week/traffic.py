import operator #파이썬의 내장 연산자에 해당하는 효율적인 함수 집합

## 전역 변수 선언 ##

#2021041059 김나영
#수송량 
traffic = [('토마스', 5), ('헨리', 8), ('에드워드', 9), ('에밀리', 5), ('토마스', 4),
         ('헨리', 7), ('토마스',3), ('에밀리',8),('퍼시',5), ('고든',13)]

trainDic, trainList = {}, [] 
tmpTup = None # 딕셔너리를 만들고자 하는 변수
totalRank, equalRank = 1, 1 # 순위 변수

## 메인 코드 ##
if __name__ == "__main__" :
    for tmpTup in traffic :
        trainName = tmpTup[0]
        trainWeight = tmpTup[1]
        if trainName in trainDic : # 딕셔너리로 만드는 과정
            trainDic[trainName] += trainWeight # 누적
        else :
            trainDic[trainName] = trainWeight # 새로운 값 등록
    print('기차 수송량 목록 =>', traffic)
    print('----------------------------')

    #sorted(정렬할 데이터, key 파라미터, reverse 파라미터)
    # 리스트.sort() vs sorted(리스트)
        # 전자는 본체의 리스트를 정렬해서 변환하는 것
        # 후자는 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환하는 것
    trainList =  sorted(trainDic.items(), key = operator.itemgetter(1),
                        reverse = True)
                        # operator.itemgetter() : 다중 수준의 정렬을 가능하게 해주는 모
                        #operator.itemgetter(1) : 첫번째 요소로 정렬하겠다는 의미
                        
    print('기차\t총 수송량\t순위')
    print('----------------------------')
    print(trainList[0][0], '\t', trainList[0][1], '\t', equalRank) # 첫번째 기차
    for i in range(1, len(trainList)) : # 두번째 기차부터 출력
        totalRank += 1
        if trainList[i][1] == trainList[i-1][1] : # 앞 기차와 수송량이 같을 경우
            pass # 건너뛰고 출력
        else : 
            equalRank = totalRank 
        print(trainList[i][0], '\t', trainList[i][1], '\t', equalRank)
    
            
