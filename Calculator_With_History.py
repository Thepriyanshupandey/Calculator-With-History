def write(userinput, result):
    with open("history.txt", "a") as f:
        f.write(f"{userinput} = {result}\n")
def show():
     f = open("history.txt")
     lines = f.readlines()
     for i in lines:
         print(i)
     
     f.close()
def clear():
     f= open("history.txt", "w")
     f.write("")
     f.close
def calculation(userinput):
        parts = str(userinput).split()
        if len(parts) != 3:
            print("Enter Vaild Equation")
            return


        num1  = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
        result = ""


        if op == "+":
            result = num1+num2

        elif op == "-":
            result = num1-num2
        
        elif op == "*":
            result = num1*num2
        
        elif op == "/":
            result = num1/num2
        else:
            print("Invaild")
        print(f"{userinput} = {result}")
        result = str(result)
        write(userinput, result)
def main():
    print("------WELCOME TO CALCULATOR------")
    while True:
        userinput = input("Give command (+ - * /) or Command his clear exit: ")
        if userinput.lower() == "exit":
            print("Thank you for using our calculator")
            break
        elif userinput.lower() == "his":
            show()
        elif userinput.lower() == "clear":
            clear()
        else:
            calculation(userinput)
         
main()