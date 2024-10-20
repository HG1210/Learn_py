print("------- CALCULATOR PART 1--------")

cal1=int(input("Enter The First Number:"))
cal2=int(input("Enter The Second Number:"))
print("Addition: ",cal1 + cal2)
print("Subtraction: ",cal1 - cal2)
print("Multiplication: ",cal1 * cal2)

print("------- CALCULATOR PART 2 --------")

cal3 = int(input("1)Enter '1' For Addition\n2)Enter '2' For Subtraction\n3)Enter '3' For Multiplication\nPress Any Key '1-3'"))
if(cal3==1):
    print("Addition: ",cal1 + cal2)
elif(cal3==2):
    print("Subtraction: ",cal1 - cal2)
elif(cal3==3):
    print("Multiplication: ",cal1 * cal2)
else:
    print("Verification Required")


budget = 200
foodExpense = int(input("Enter the value"))
if(budget - foodExpense > 50):
    print("You can still proceed with your order")
else:
    print("Check your Food Expense Value")

# Not supported in the current version
# songs = input("Enter the string")
# match songs:
#     case "Mann":
#         print("Mann Jogiya")
#     case "Abram":
#         print("Abram")
#     case _:
#         print("Access Playlist 1950s")
