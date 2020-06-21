
# coding: utf-8

# In[1]:


#Program to design simple calculator  for the operators
a=float(input('Enter value of a'))
b=float(input('enter value of b'))
print('MENU:- ')
print('Press 1 to Addition +')
print('Press 2 to Subtraction -')
print('Press 3 to Multiplication *')
print('Press 4 to Division /')
print('Press 5 to Modulus %')
print('Press 6 to Exponent **')
print('Press 7 to Floor division //')
op=int(input('Enter the operation:>>>'))
if(op==1):
    print("sum of a+b=")
    r=a+b
elif(op==2):
    print("diff of a-b=")
    r=a-b
elif(op==3):
    print("mul of a*b=")
    r=a*b
elif(op==4):
    print("div of a/b+")
    r=a/b
elif(op==5):
    print("mod of a%b=")
    r=a%b
elif(op==6):
    print("exponent of a**b=")
    r=a**b
elif(op==7):
    print("floor div of a//b=")
    r=a//b
else:
    r="invalid selection"
print(r)
print("THANK YOU")


# In[2]:


#Program to calculate Simple Interest

p=int(input('Enter the principal amount'))
t=int(input('Enter the time duration'))
r=float(input('Enter the rate of interest'))
si=p*t*r/100
print(si)


# In[3]:


#Program to Calculate Area of  a Circle

radius=float(input("Enter the radius of circle"))
pi=3.142
print("Area of a circle is=")
area=pi*(r*r)
print(area)


# In[6]:


#Program to Calculate Area of a triangle

Base=float(input("Enter the base of a triangle="))
Height=float(input("Enter the height of a triangle="))
AreaofTri=1/2*(Base*Height)
print(AreaofTri)


# In[7]:


#Program to Temperature in Celsius to Fahrenheit

c=float(input("Enter the temperature in Celsius="))
temp=(c*(9/5))+32
print("Temperature in Fahrenheit=",temp)


# In[8]:


# Program to Calculate Area of Rectangle


l=float(input("Enter the length of Rectangle="))
w=float(input("Enter the width of Rectangle="))
AreaofRec=l*w
print("Area of Rectangle=",AreaofRec)


# In[9]:


#Program to Calculate Perimeter of Square

side=float(input("Eneter the side of a Square="))
P=4*side
print("Perimeter of square =",p)


# In[10]:


#Program to Calculate Circumference of Circle

pi=3.142
r=float(input("Enter the radius of circle="))
circum=2*pi*r
print("Circumference of Circle =",circum)


# In[12]:


#Program to Swap two Numbers

num1=int(input("Enter the value of num1="))
num2=int(input("Enter the value of num2="))
print("Values before Swapping=",num1,num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("Values after Swapping=",num1,num2)

