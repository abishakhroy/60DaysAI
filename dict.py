student ={"name":"Abi","age":30,"courses":["Math","CompSci"]}
print(type(student))
print(student["name"])

student["location"] = "Hatton"
print(student)

student["age"]=29
print(student)

student.pop("age")
print(student)  # Output: {'name': 'Abi', 'courses': ['Math', 'CompSci'], 'location': 'Hatton'}

print(len(student))  # Output: 3
print(student.keys())  # Output: dict_keys(['name', 'courses', 'location'])
print(student.values())  # Output: dict_values(['Abi', ['Math', 'CompSci
print(student.items())  # Output: dict_items([('name', 'Abi'), ('courses', ['Math', 'CompSci']), ('location', 'Hatton')])
print(student.get("name"))  # Output: Abi
print(student.get("age", "Not Found"))  # Output: Not Found
print(student.setdefault("age", 25))  # Output: 25
print(student)  # Output: {'name': 'Abi', 'courses': ['Math',
# 'CompSci'], 'location': 'Hatton', 'age': 25}
print(student.clear())  # Output: None
print(student)  # Output: {}
student.update({"name":"Abi","age":30,"courses":["Math","CompSci"]})
print(student)  # Output: {'name': 'Abi', 'age': 30,
print(student["courses"][1])  # Output: CompSci
# 'courses': ['Math', 'CompSci']}
student["colour"]="green","blue","white"
print(student)  # Output: {'name': 'Abi', 'age': 30,
print(student["colour"][2])