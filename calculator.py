#function for addition
def add(num1,num2):
    return num1+num2

#function for substraction
def substration(num1,num2):
    return num1-num2

#function for multiplication
def multiplication(num1,num2):
    return num1 * num2

#function for division

def division(num1,num2):
    if num2==0:
        return "cannot divide by zero"
    return num1/num2
# function for average
def average(num1,num2):
    return (num1+num2)/2

print("please select operation -\n"\
      "1. Add\n" \
      "2. substrat\n" \
      "3. multiplation\n" \
      "4. division\n" \
      "5. average")

select=int(input("select number to perform opration 1,2,3,4,5: "))

number1=int(input("enter your first number: "))
number2=int(input("enter your second number: "))

if select==1:
    print(number1,"+",number2,"=",add(number1,number2))
elif select==2:
    print(number1,"-",number2,"=",substration(number1,number2))
elif select==3:
    print(number1,"*",number2,"=",multiplication(number1,number2))
elif select==4:
    print(number1,"/",number2,"=",division(number1,number2))
elif select==5:
    print("(",number1,"+",number2,")","/","2","=", average(number1,number2))
