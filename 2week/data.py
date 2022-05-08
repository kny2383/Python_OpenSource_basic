import sys

if __name__ == "__main__":
    
    tupleVar = ()
    #2021041059_김나영
    print("int형 기본 크기 --> ", sys.getsizeof(1))
    print("float형 기본 크기 --> " , sys.getsizeof(1.0))
    print("bool형 기본 크기 --> " , sys.getsizeof(True))
    print("str형 기본 크기 --> ", sys.getsizeof('')) 
    print("list형 기본 크기 --> ", sys.getsizeof([]))
    print("tuple형 기본 크기 --> ", sys.getsizeof(tupleVar))
    print("dictionary형 기본 크기 --> ", sys.getsizeof({}))
    print("set형 기본 크기 --> ", sys.getsizeof(set()))


