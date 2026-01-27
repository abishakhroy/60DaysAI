
'''
a = 65
b = 79

def marks_ave() :

    c = a+b
    return c/2

print(marks_ave())

'''

def rest():
    ab=int(input("Enter cash:"))

    if ab >= 100 :
        food =str(input("Vada or Bajji:"))
        if food == "Vada":
            print("You will get Vada")
        else:
            print("You will get Bajji")
    else:
        return "Not enough cash"

print(rest())

def bio(name, hobby):
    return f"My name is {name} and I love {hobby}."

print(bio("Abi", "coding"))