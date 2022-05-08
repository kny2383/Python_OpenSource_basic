from time import * # time module 사용
from datetime import * # datetime module 사용

## 2021041059_김나영
## 함수 선언 ##

def countDays(date1, date2) : 
    retDays = 0
    year, month, day = date1.split('/') # 숫자를 /으로 나눔
    sDay = date(int(year), int(month), int(day))
    year, month, day = date2.split('/')
    eDay = date(int(year), int(month), int(day))
    diffDays = eDay - sDay
    retDays = diffDays.days # 날짜만 추출
    return retDays

def getDay(t) :

    weeks = ['월', '화', '수', '목', '금', '토', '일']
    return weeks[t.tm_wday]

## 전역 변수 선언 ##
startDate, curDate, tm = '', '', None

## 메인 코드 부분 ##
if __name__ == "__main__" :

    startDate = input('시작 날짜(연/월/일) --> ')
    tm = localtime() # 현재 날짜 객체 반환
    curDate = str(tm.tm_year) + '/' + str(tm.tm_mon) + '/' + str(tm.tm_mday)
    print(startDate, '부터 오늘(', curDate,')까지는 ', countDays(startDate, curDate), '일이 지났습니다')
    print('그리고 오늘은', getDay(tm), '요일입니다')
