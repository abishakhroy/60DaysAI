
abish=int(input("Enter the amount: "))    

if abish == 100 :
    print("you will get vada")
else:
    print("not enough amount")

abi=int(input("Enter money :"))
if abi >= 100 :
    print("you will get bajji and tea")
elif abi <100 and abi >= 60:
    print("you will get tea or vada")
else:
    print("not enough amount")


ab=int(input("Enter cash:"))

if ab >= 100 :
    food =str(input("Vada or Bajji:"))
    if food == "Vada":
        print("You will get Vada")
    else:
        print("You will get Bajji")
else:
    print("Not enough cash")
    
