
try:
    c = 10/0
    print(c)
except:
    print("Error occured")
finally:
    a=4
    b=5
    print(a+b)
    
try:
    c = 10/0
    print(c)
except Exception as x:
    raise x

finally:
    a=4
    b=5
    print(a+b)
    