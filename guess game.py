
#level = l
#f= first s =second r=random  a=access g=yourguess

from random import *
from math import *


a = None
l = None
f = None
s = None

l = str(input("choose your level(easy-medium-hard):"))
f = int(input("type the begining of your range:"))
s = int(input("type the last of your range:"))

e = None
d = None
d = s-f
r = randint(f,s)
e = ceil(log2(d))

if(l == "easy"):
    a = e +(0.02 * (d))
    print("number of your chance is:" ,int(a))
if(l == "medium"):
    a = e
    print("number of your chance is:" ,int(a))
if(l == "hard"):
    a = e -(0.02 * (d))
    print("number of your chance is:" ,int(a))
    
g = None


for i in range(1,int(a+1),1):
    g = int(input("enter your first guess:"))
    x = None
    if(g<f and g>s):
        x = i
        print("your number was out of range,the left chance:" ,int(x))
    else:
        if(g == r):
            print("you win")

        else:
            if(g>r):
                print("the number you need is less than your guest,try again!")
                x = a - i
                print("the left chance:" ,int(x))
            else:
                print("the number you need is bigger than your guest,try again!")
                x = a - i
                print("the left chance:" ,int(x))
                if((int(x)) == 0):
                    print("game over")

        
           
            

        
    
        
        








    
