x=int(input("Enter the data = "))
y=input("Enter to quit :")
if((x<5 or x>9) or y!='quit'):
    raise ValueError("The data you entered is not valid")