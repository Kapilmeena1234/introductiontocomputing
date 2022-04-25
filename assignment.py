 # QUESTION 1
number_1=int(input("Enter number 1 :"))      #taking input of three integers from user
number_2=int(input("Enter number 2:"))
number_3=int(input("Enter number 3:"))
#The average of three number = sum of all the elements/number of elements
Average=(number_1+number_2+number_3)/3
print('The average is:',Average)



#Question 2

standard_deduction=10000 
depend_deduction=3000 
gross=input("enter gross income") 
No_of_dependents=input("Enter number of dependents") 
taxable_income=int(gross)-int(standard_deduction)-(int(depend_deduction)+int(No_of_dependents)) 
tax=(float(taxable_income)*0.2) 
print("Your income tax is :") 
print(float(tax))



# QUESTION 3
number_of_minutes=int(input("Enter number of seconds : "))                       #takes number of minutes as input from user
# //-  gives Quotient as output
# %-   gives remainder as output
print("It has",number_of_minutes//60,"minutes and " ,number_of_minutes%60,"seconds")


# Question 4 
a= 25 
b='25' 
c=25.0 
sum=(a+int(b)+int(c)) 
print(str(sum))



# QUESTION 5
import math                                 # Command to import math module in order to use mathematical terms and values    
for i in range(0,360,15):                   # for loop is used first shows starting value
                                                             # second shows ending value
                                                             # third shows steps or gaps to be taken                 
    cosine=math.cos(math.radians(i))       # i is a variable runing in for loop
    sine=math.sin(math.radians(i))         # Gives answer in radians 
    print( "cosine(",i,") is",round(cosine,4),"           sine(",i,") is",round(sine,4))
