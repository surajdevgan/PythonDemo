import datetime
Dob = input("Enter your Dob: ")   # this input always take string input
CurrentYear = datetime.datetime.now().year
Age = CurrentYear-int(Dob)

if (Age>=18):

    print("Your Age is {} and you are adult".format(Age))

else:
    print("Your Age is {} and you are not adult".format(Age))

print("App End ")




