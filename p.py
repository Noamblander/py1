import os
def menu():
    print("1 - MULT")
    print("2 - MINUS")
    print("3 - ADD")
    print("4 - DIVIDE")
    print("X - EXIT")
    print("Z - CLEAN")
    return input("your selection: ")




if __name__ == "__main__":
    calc_done = False
    while (not calc_done):
        user_selection = menu()
        if str.isdigit(user_selection):
            num = int(user_selection)
            if num < 5:
                num1 = input("enter first number- ")
                num2 = input("enter second number- ")
                if num == 1:
                    print(f"{num1} * {num2} ={int(num1) * int(num2)}")
                if num == 2:
                    print(f"{num1} - {num2} ={int(num1) - int(num2)}")
                if num == 3:
                    print(f"{num1} + {num2} ={int(num1) + int(num2)}")
                if num == 4:
                    print(f"{num1} : {num2} ={int(num1) % int(num2)}")    

                calc_done = True
            else:
                print(" u r an idiot")
        elif user_selection == "x":
            calc_done = True
        elif user_selection == "z":
               os.system('cls' if os.name == 'nt' else 'clear') 
        else: print ("please type a number")     

    
             
