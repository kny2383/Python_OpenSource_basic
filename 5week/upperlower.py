## 전역 변수 선언 ##
inStr, outStr = "", "" # inStr : 입력받은 문자열, outStr : 대소문자를 변환하는 문자열
ch = "" # ch : 문자열에서 한 글자씩 뽑아서 잠시 저장할 때 사용하는 변수
count, i = 0,0


## 2021041059_김나영

## 메인 코드 ##
if __name__ == "__main__" :
    inStr = input("문자열을 입력하세요 : ")
    count = len(inStr) # inStr의 길이 

    for i in range(0,count) : 
        ch = inStr[i] # ch에 한 글자씩 넣어준다
        if (ord(ch) >= ord("A") and ord(ch) <= ord("Z")) : # 대문자 -> 소문자
            newCh = ch.lower()
        elif (ord(ch) >= ord("a") and ord(ch) <= ord("z")) : # 소문자 -> 대문자
            newCh = ch.upper()
        else :
            newCh = ch

        outStr += newCh 

    print("대소문자 변환 결과 --> %s" % outStr)
            
        
