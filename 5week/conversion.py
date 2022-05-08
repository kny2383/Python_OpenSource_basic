def base2(n, base): # 2진수 출력
    T = "0123456789ABCDEF"
    q, r = divmod(n, 2)
    if q == 0:
        return T[r]
    else:
        return base2(q, 2) + T[r]

def base8(n, base): # 8진수 출력
    T = "0123456789ABCDEF"
    q, r = divmod(n, 8)
    if q == 0:
        return T[r]
    else:
        return base8(q, 8) + T[r]

def base16(n, base): # 16진수 출력
    T = "0123456789ABCDEF"
    q, r = divmod(n, 16)
    if q == 0:
        return T[r]
    else:
        return base16(q, 16) + T[r]
    
if __name__ == "__main__" :
    ten = int(input("10진수 입력 -->"))
    
    print (base2(ten, 2)) # 2진수 출력
    print (base8(ten, 8)) # 8진수 출력
    print (base16(ten, 16)) # 16진수 출력
    #2021041059_김나영
