
print("Input lengths of the triangle sides: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
def value(a, b, c):  
      
   
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True        
  


if value(a, b, c): 
    print("Valid")  
else: 
    print("Invalid") 

