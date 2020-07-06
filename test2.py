def dec1(func):  
    print("1111")  
    def one():  
        print("2222")  
        func()  
        print("3333")  
    print("4444")
    return one  
  
def dec2(func):  
    print("aaaa")  
    def two():  
        print("bbbb")  
        func()  
        print("cccc") 
    print("dddd")
    return two  
 
@dec1  
@dec2  
def test():  
    print("test test")  
  
test()  
