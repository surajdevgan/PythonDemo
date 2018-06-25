person = dict(Name = "Suraj", Age = 24, Roll = 1455455)  # mutable
print(person["Name"])
person["Name"] = "Suraj Devgan"
person["Sex"] = "Male"
print(person)
del person["Age"]
print(person)