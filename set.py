num={1,2,3,4}
print(type(num))

type_num = type(num)
print(type_num)  # Output: <class 'set'>

print(len(num))

num.add(5)
print(num)
num.remove(3)
print(num)