
#Program of Maximum of three numbers
def my_fun():#creating a  function,function name is my_fun
    if a > b :#comparing the two variables(a and b),if b is max,then it doesn't print the statement a is max,it goes to the next line.
        print("a is max") #Print is a function,it prints whatever is present inside the double quotes
    elif b > c :#compares b and c,if b is max then,it prints b is max
        print("b is max")
    else:#if both the conditions are wrong then it moves to the else condition,c is max is printed
        print("c is max")
a = 2  #initializing a as a  variable and assigning a value 2
b = 3  #initializing b as a variable and assigning a value 3
c = 4  #initializing c as avariable and assigning a value 4
my_fun()#calling a defined  function