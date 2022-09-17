

print()
print("WELCOME TO GREAT KIRIKALAN BANK \n\nInsert your card")
print()

password=1234
balance=10000
choice=0

pin=int(input("Enter your four dight pin:\n"))

if pin ==password:
    while choice !=4:
        print("\n\n**** Menu ****")
        print("1 == balance")
        print("2 == deposit")
        print("3 == withdraw")
        print("4 == cancel\n")

        choice=int(input("\nEnter you option:\n"))

        if choice==1:
            print("balance = RS ", balance)
        elif choice==2:
            dep=int(input("enter your deposit: R"))
            balance += dep
            print("\ndeposited amount: RS ",dep)
            print("balance = RS",balance)
        
        elif choice==3:
            wit=int(input("enter the amount to withdraw: R"))
            balance-=wit
            print("\nwithdrawn amount: RS ",wit)
            print("balance = RS ",balance)
        elif choice==4:
            print("\n session ended! Goodbye")
        else:
            print("\nInvalid Entry!!")
else:
    print("pin incorrect!! Try again")