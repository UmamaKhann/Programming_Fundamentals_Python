'''
# single line comment
'''
#mutiple line comment
'''
# print statements
# variables
# Operators(=,-,//,%)
# comparision opertor(<,>,<=,==)
# Logicat operatos(and,or,not)
# Assignment operators(*=,+,etc)
# Identity operators(is,isnot)
# membership operators

# practie question
# id card details
name='jhon'
age=18
address='F\242-4'
print('NAME',name )
print('AGE',age)
print('ADDRESS',address)

#print output in another line with backslah n
print('NAME',name,'\n'+'AGE',age,'\n'+ 'ADDRESS',address)

#swab value variable
a='umama'
b='khan'
c=a
a=b
b=c
print(a,b)

# int to float
x=12
y=float(x)
print(type(y))


# float to int
a=12.1
b=int(a)
print(b)

mod=9%2
double_div=11//3
print(mod,'\n',double_div)

#remove first 2 integer
p=bin(10)
s=str(p)
r=s[2:]
print(r)

#Bitwise operator
a=10
b=8
print(a^b)

a=10
b=8
print(a|b)

a=10
b=8
print(a&b)

print(10>>3)
#Conditional statement
m=89
if m>=90:
    print('yes you win')
print('thank you')

m=89
if m>=90:
    print('pass')
else:
    print('fail')
print('thank you')


m=80
if m>=90:
    print('pass')
elif m>=7 and m<90:
    print('Average')
else:
    print('fail')
print('thank you')

#nested statement
m=95
if m>=80:
    print('you go to picnic')
    if m>=95:
        print('you will get a bike')
else:
    print('you not go to picnic')

#short hand if and else statement

m=93
if m>=90: print('you go to picnic')

m=85
print('you go to picnic') if m>=90 else print('you not go to picnic')


# practice qno
num=int(input('enter the num: '))
if num>=0:
    print('The num is positive')
else:
    print('The num is negative')

#check num is odd or even
num=int(input('enter the num: '))
if num%2==0:
    print('The',num,'is a even num')
else:
    print('The',num,'is a odd num')

#Area calculate
area=input('Enter the area name: ')
if area == 'square':
    num=int(input('enter the num: '))
    a=num**2
    print('the area of square is',a)
elif area == 'rectangle':
    l=int(input('enter the l: '))
    b=int(input('enter the b: '))
    h=int(input('enter the h: '))
    a=l*b*h
    print('the area of rectangle is',a)

elif arear == 'parallelogram':
    b=int(input('enter the b: '))
    h=int(input('enter the h: '))
    a=b*h
    print('the area of parallelogram is',a)
else:
    print('This is not a shape name')
    
# chcek vowel or not
vowel='a,e,i,o,u' or 'AEIOU'
alpha=input('Enter the alpha: ')
if alpha in vowel:
    print('The alpha is a vowel')
else:
    print('The alpha is not a vowel')

#check the num is 1,2 or 5 digit num
digit=int(input('Enter the digit: '))
if digit>=0 and digit<=9:
    print(digit,'is a 1 digit num')
elif digit>9 and digit<=99:
    print(digit,'is a 2 digit num')
else:
    print(digit,'is a digit num')

digit=int(input('Enter the digit: '))
digit=str(digit)
if len(digit)==1:
    print(digit,'is a 1 digit num')
elif len(digit)==2:
    print(digit,'is a 2 digit num')
elif len(digit)==3:
    print(digit,'is a 3 digit num')
else:
    print(digit,'is a 5 digit num')

#loops 
#while , for , while True , nested Loops

#For Loop
for i in range(1,6):
    print(i)

for i in range(1,8,2):
    print('skip one num:',i)

#Table 
n=5
for i in range(1,11):
    print(n,'*',i,'=',n*i)

# Odd num table
n=2
for i in range(1,31,2):
    print(n,'*',i,'=',n*i)

# while loop
i=1
while i<=5:
    print(i)
    i+=1

# Even table
i=1
n=7
while i<=10:
    print(n,'*',i,'=',n*i)
    i+=2

#While true(infinite loop)

while True:
    num1=int(input('Enter num1:'))
    num2=int(input('Enter num2:'))

    num=num1+num2
    print(num)
    r=input('you want to stop:')
    if r=='Yes':
        break

# Nested Loop (loop inside the loop)
for i in range(1,5):
    for j in range(1,11):
        print(j,end=' ')
    print()

#pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
# nested condition
for i in range(1,6):
    if i==3:
        print('You can do it')
    print(i)

n=1
while n<=10:
    if n==3:
        print('You did it')
    n=n+1
    print(n)
 
# break and continue
n=1
while n<=5:
 
#practice qno     
#find sum of all even num
a=0
for i in range(2,50,1):
    a+=i
print('The sum of even num is',a)

#num with their square
for i in range(1,11):
    sq=i**2
    print(i,sq)

# to find sum of first ten odd num using while loop
n=1
i=1
a=1
while n<=9: 
    i+=2 
    a+=i 
    n+=1 

print('sum of first ten odd num',a)

# check num is divsible by 8 and 12 upto 100 
div=''

for i in range(1,100):
    if i%8==0 and i%12==0:
        i=str(i)
        div+=i+' ' 
if div=='':
    print('NO num div by 8 and 12')
print('num is divsible by 8 and 12:',div)

#program to create a billing sys of market

print(  "WELCOME TO THE UMAMA'S STORE"   )
print('We have Mango,Cake,Chips,Juice in our store ')

item1=50
item2=500
item3=100
item4=200

Total=0
a=int(input('Enter the total num of item do you want:'))
for i in range(1,a+1):
    name=(input('Enter the name of item:'))
    quantity=int(input('Enter the quantity item do you want:'))
    if name=='Mango':
        subTotal=item1*quantity
        Total+=subTotal
    elif name=='Cake':
       subTotal=item2*quantity
        Total+=subTotal
    elif name=='Chips':
        subTotal=item3*quantity
        Total+=subTotal
    elif name=='Juice':
        subTotal=item4*quantity
        Total+=subTotal
    else:
        ('we don;t provide this item')
    print('subTotal',subTotal)
print('The total bill is:',Total)
print('Thank You')
    

#str*int tu repeat hoga wo str jisai int ka num ha
#another method of previous question
while True:
    n=input('Enter the name of customer: ')
    total =0
    while True:
        amount=float(input('enter the amount:'))
        q=int(input('Enter quantity: '))
        total+=amount*q
        again=input('Do you want to continue shopping: ')
        if again.lower()=='no':
            break
    print('*'*15)
    print(n)
    print('Total amout is',total)
    print('-'*5,'Thank You','-'*5)
    print('*'*15)

    cust2=input('another customer:')
    if cust2.lower()=='no':
            break


a='Why fit in, When you are born to Stand Out!'
#find length of str
print('the len of the str is:',len(a))
#how many time o is occur
b=a.count('o')
count=0
for i in a:
    if i=='o':
        count+=1
print('o is occur',count,'time')
#lower and upper the str
print('The str in smaal',a.lower())
c=a.upper()
print('The str in capital: ',c)
#convert str in title
a='Why fit in, When you are born to Stand Out!'
print(a.title())
#find index no of fit in
num=a.index('fit in')
print('the index num is',num)

a='Why fit in, When you are born to Stand Out fit in!'
b=a.find('fit in')
for i in range(len(a)):
    if a[i:i+6] == 'fit in':
        print(a[i:i+6])
        print('The index num is',i)
# draw a pattern of triangle      
for i in range(1,6): 
    for j in range(1,i+1): 
        print(j,end=' ')
    print()

for i in range(1,6): 
    for j in range(1,i+1): 
        print(i,end=' ')
    print()   
    
# pattern of square
for i in range(1,6): 
    for j in range(1,6): 
        print(j,end=' ')
    print()
    
for i in range(1,6): 
    for j in range(1,6): 
        print(i,end=' ')
    print()
 
   
a=5
for i in range(1,6):
    for j in range(a):
        print(i,end=' ')
    print()
    a-=1

    *
   **
  ***
 ****
*****   
a=4
for i in range(1,6):
    print(a*' '+i*'*',end='')
    print()
    a-=1

1 
2 1 
3 2 1
4 3 2 1
5 4 3 2 1

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

*
**
***
*****
***
**
*


for i in range(1,5):
    print(i*'*')
for j in range(3,0,-1):
    print(j*'*')

1 
2 4 
3 6 9
4 8 12 16
5 10 15 20 25
6 12 18 24 30 36
7 14 21 28 35 42 49
8 16 24 32 40 48 56 64

for i in range(1,9):
    for j in range(1,i+1):
        print(i*j,end=' ')
    print()
    '''
# string manipulation
# inside in the string any combination
'''
1-length
a='hello World'
print(len(a))

2-count
a='hello'
print(a.count('o'))
print(a.count('H'))

3-upper, lower
print(a.lower())
print(a.upper())

4-Index
a.index('l')
a.index('l',6,11)

5-capitalize  (first letter capital )
print(a.capitalize())

6-casefold (str in lowwercase)
print(a.casfold())

7-Find
print(a.find('W'))

8-format (variable inside a str)
name='umama'
b='my name is {}'
print(b.format(name))

9-center 
print(name.center(10,'*'))

1o-isalnum (give True in the str are num and alpha no count space or special charcter)
b='hello 123'
print(b,b.isalnum())

11-isalpha (str in alphabet )
c='khan'
print(c,c.isalpha())

12-isdecimal (str are in decimal)
c=12345
print(c.isdecimal())

13- isdigit (str num ha ya nh)
print(c.isdigit())

14- isnumeric(same as isdigit)
print(c.isnumeric())

15- islower(check str in small character)
a='umama'
print(a.islower())

16- isupper(check str in capital character))
o='FATIMA'
print(o.isupper())

17- (isspace str are whitespace)
f='      '
print(f.isspace())

18- istitle (all charc first letter is capital)
a=print(a.istitle())

19- endswith (check last value wahan end ho rahe ha ya nh)

a='Harry Potter'
print(a.endswith('r'))
print(a.endswith('t',6,9))

20-startswith (check the str start with given value)

21-swapcase (upper ko lower and viceversa)
print(a.swapcase())

22-strip (trimmed the str(chezai hata tha ha))
a='      Harry Potter   '
print(a.strip(' '))

23- split
print(a.aplit('o'))

24-ljust (left alingment)

x=a.ljust(20)
print(x,'is my fvrt')

25- rjust(right alingment)
x=a.rjust(20'*')
print(x,'is my fvrt')

26-replace
print(a.replce('Harry','khan'))

27-rindex / rfind() (give index)
a='Harry Potter movie'
print(a.rindex('movie))
 28=sort
print(a.sor())
30=sorted
print(sorted(b))

#slicing
a='Harry Potter movie'
print(a[0:5])
print(a[:5])
print(a[-4:])
b=0123456
print(b[::2]) #gap ajai ga
print(b[::-1) # reverse


#practice qno
#fibonaci series

a=0
b=1
n=1
num=''
num+=str(a)+' '+str(b)+' '
naam=int(input('Enter the num:'))
while n<naam-1:
    c=a+b
    num+=str(c)+' '
    a=b
    b=c
    n+=1
print(num)

#check prime num

num=3
if num%3==0:
    print('The given num is prime')
else:
    print('The num is not prime')

prime=True
num=int(input('Enter the num: '))
for i in range(2,num):
    if num%i==0:
        prime=False
        print('The given num is not prime')
        break
if prime == True:
    print('The given num is prime')      

    num=int(input('Enter the num: '))
for i in range(2,num):
    if num%i==0:
        print('The given num is not prime')
        break

else:
    print('The given num is prime')      
    
# find palindrome of integer
num=int(input('Enter the palindrome num: '))
num=str(num)
a=num[::-1]
if num==a:
    print('The given num is palindrome')
else:
     print('The given num is not a palindrome')

num=int(input('Enter the palindrome num: '))
rev=0
temp=num
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if rev==temp:
    print('The given num is palindrome')
else:
    print('The given num is not a palindrome')

 # create an area calculator
while True:
    area=input('Enter the area name: ')
    
    if area == 'square':
        while True:
            num=int(input('enter the num: '))
            a=num**2
            print('the area of square is',a)
            again=input('do you want t repaet?')
            if again=='no'.lower():
                break
    elif area == 'rectangle':
        while True:
            l=int(input('enter the l: '))
            b=int(input('enter the b: '))
            h=int(input('enter the h: '))
            a=l*b*h
            print('the area of rectangle is',a)
            again=input('do you want t repaet?')
            if again=='no'.lower():
                break
    elif arear == 'parallelogram':
        while True:
            b=int(input('enter the b: '))
            h=int(input('enter the h: '))
            a=b*h
            print('the area of parallelogram is',a)
            again=input('do you want t repaet?')
            if again=='no'.lower():
                break            
    else:
        print('This is not a shape name')
    again=input('do you want to repaet whole code?')
    if again=='no'.lower():
        break
        
#practice qno
#seprate the str into coma
a='OOTD.YOLO.ASAP.BRB.GTH.OTW'
b=a.split('.')
print(b)
#sorted the func
b.sort() #for list
print(b)
c=sorted(a)# for str
print(c)
#remove charc
remove=a.replace('BRB','KARACHI')
print('The str after remove ',remove)

#remove dot from str
name='U.M.A.M.A'
after=name.split('.')
print('The name is',after)

name='U.M.A.M.A'
after=name.replace('.','')
print('The name is',after)

#check the occurence
name=input('Enter the variable: ')
search=input('what you want to count: ')
occur=name.count(search)
print('The',search,'occur in variable is',occur,'times')

#str then reverse it
name=input('Enter the variable: ')
u=name[::-1]
print('The str after reverse',u)
#str contain only digit
name=input('Enter the variable: ')
c=name.isdigit()
print('THe given str is',c)

#vowels in a str
vowels='aeiouAEIOU'
name=input('Enter the variable: ')
c=''
count=0
for i in name:
    if i in vowels:
        c+=i
        count+=1
print('the vowels in the str are',c)
print('The no of vowels in the str are',count)

#str begins with capital letter
istitle() also use
name=input('Enter the variable: ')
lst=name.split('')
capital=True
for i in lst:
    if i[0].isupper()==False:
        capital=False
        print('The whole variable does not begin with capital letter')
        break
if capital==True:
    print('The whole variable begin with capital letter')

#List
#collection of ordered and mutable data give multiple value
#i.e=['apple','banana','cherry','45']

a=['apple','banana','cherry']
print(a[1])
print(a[::2])
print(a[-3:-1])
print(a[::-1])
#iteration using loop

a=['apple','banana','cherry','45']
#iteration using for loop
for i in a:
    print(i)
for i in range(len(a)):
    print(a[i])
 #iteration using while loop  
i=0
while i<len(a):
    print(a[i])
    i=i+1 
#short_hand for loop
[print(i) for i in a]
#List func
#find len of lst
print(len(a))
#count the occurance of an element
b=['apple' , 'banana' , 'cherry' , '45' ,'45']
print(a.count('45'))
#add to the lst
a.append('superman')
print(a)

#specific location
a.insert(3,'cherry')
print(a)
#remove from a lst
a.remove('banana')
print(a)

#certain location
#return the value what we remove 
a=['apple' , 'banana' , 'cherry' , '1' ,'45']
print(a.pop(1))
print(a)

#create a copy
lst=a.copy()
print(lst)
#to access an element
print(a.index('cherry'))
#extend the lst
c=['1','2']
a.extend(c)
#reverse
a.reverse()
print(a)
#to sort
a.sort()
print(a)
#to clear
a.clear()
print(a)

#list comprihensive
lst=[4,8,9,0]
lst2=[]
for i in lst:
    lst2.append(i)
print(lst,'\n',lst2)
#ek lst ka data ek lst ma karna hu
lst3=[i for i in lst if i> 45]
print(lst3)

#practice qno
#swap
a=['umama','fatima','kinza']
a[0],a[2]=a[2],a[0]

#value at 2nd position
a.insert(1,'fatima')
print(a)
a.pop(2)
print(a)
#multiply the num
lst=[1,3,9,7]
multiply=1
for i in lst:
    multiply*=i
print(i)
#largest num from the lst

lst.sort()
prin('largest value is',lst[-1])

prin('smallest value is',lst[0])
#INTRODUCTION TO TUPLES
#tupkes are lst and we don't edit the tuple
a='apple','mango',1,9
print(type(a))
print(a)
b='umama',
print(type(b))

#slicing in tuple
a='nokia','vivo','oppo','techno'
print(a[::3])
print(a[::2])
print(a[2::-1])
#for loop
for i in a:
    print(a)
for i in range(len(a)):
    print(a[i])
#while loop
i=0
while i<len(a):
    print(a[i])
    i+=1
#converstion of tuples into list
a='nokia','vivo','oppo','techno'
a=list(a)
a.append('oneplus')
a=tuple(a)

print(a.count('vivo'))

print('the index of nokia is',a.index('nokia'))

#INTRODUCTION TO DICTIONARY
#write the data in the form of keys and values
keys and values are separated by colon 
using curly bracket
i.e;
data ={'name':'umama','age':18,'gender':'female'}
print(data)

data ={'name':'umama','age':18,'gender':'female'}
#iteration in dic
for i in data:
    print(i)
#getting keys
for i in data:
    print(data[i])
#dono values mil jai gi
for i in data.items():
    print(x,y)
#FUnctions in dic
#get
x=data.get('gender')
print(x)
#keys
b=data.keys()
#values
c=data.values()
#copy
a=data.copy()

#setdefault (if keys are not in the lst we use this to save from error )
data ={'name':'umama','age':18,'gender':'female'}
c=data.setdefault('rida',18)
print(c)
#update the items
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

#pop func
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)

#lst mutable ha tuple nh
#keys ma immutable chezai dal tai hain value ma koi bhi dal du value
car = {
  ('brand'): "Ford",
  90: "Mustang",
  "year": 1964
}
print(car)

#NESTED LIST
data ={1:{'name':'umama','age':18,'gender':'female'},
2:{"brand": "Ford","model": "Mustang",
  "year": 1964}}

print(data)

print(data[2])


#practice problem
#sort a dic
a={'a':1,'b':9,'c':6}
a=sorted(a.values())
print(a)
#insert the value i dic
a={}
a[1]='alphabet'
print(a)

a={}
for i in range(1,10):
    a[i]=i**2
print('The values is the square of key is:',a)

a={'a':9,'b':7,'c':3}
product=1
for i in a:
    product*=a[i]
print(product)

#INTRODUCTION TO SETS
#unordered collection of data
#collection of dataevery elemnt are unique and mutable
#set written inside the curly brackets
#and ek value repeat nh ho sekhthi ek hee set mai

a={'umama','rida','fatima','kinza'}
print(type(a))
for i in a:
    print(a)

#function of sets
#add
a.add('bisma')
#pop (randomly value remove)
a.pop()
#a.remove('rida')
#discart
a.discart('bisma')
#copy
b=a.copy()
#isdisjoint 
print(a.isdisjoint(c))
#issubset (b ka element present ha ya nh set a ma)
c={'3,5,9,7'}
print(c.issubset(a))
#update (like union)
a.update('c')
#clear
a.clear()
print(a)
a={'umama','rida','fatima','kinza'}
c={'3,5,9,7'}
b={'umama','rida','fatima','ghania'}
#union
print(a.union(b))
#diffrence (only give set a element or common value nh da ta)
print(a.union(c))
#difference update ( jo set ha osai hee update karna)
a.diffrence_update()
#intersection
w=(a.intersection(b))
#intersection_update
w=(a.intersection_update(b))
#symmetric diff (no common value give)
n=a.symmetric_diffrence(b)
n=a.symmetric_diffrence_update(b)

#practice problem

#find max and min in a set
num={1,4,6,9,3}
maximum=max(num)
minimum=min(num)
print('The mav value is ',maximum)
print('the min alue is ',minimum)

#program to find thwe common element in 3 list using set
a={1,3,4,6}
b={3,9,5,2}
c={3,2,10,11}
print(set(a) & set(b)& set(c))

#find diffrence b\w two set
a={1,3,4,6}
b={3,9,5,2}
store=a.difference(b)
print('the diffreence b\w is:',store)

#remove an element in the set if it present
a={1,3,4,6}
b=a.copy()
g=True
search=int(input('enter what you want remove:'))
for i in b:
    if i==search:
        a.remove(search)
        g=False
if g==True:
    print('It is not present')
print('After removing the element:',a)

#check set is a subset of another set
a={1,3,4,6}
b={3,9,5,2}
c={1,3,4,6}
print(a.issubset(c))

#FUNCTIONS
#which once created they cam be used throughout the program
#i.e;
def add()
    x=3
    y=5
    c=x+y
print(add(c))

#PARAMETER add(x,y) when define the func
#ARGUMENT provide values is argument
#ARBITARY ARGUMENT (use index num)
def hello(name):
    print('hello',name[1])
print('umama','rida','fatima')

#return (when use this no need of print statement)
#RECURSION 
#call itself again and again they also have a basecase
#i.e:
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(5)) 

#LAMBDA
#for a short period of time (temporary func)+(only one expression)
#they have multiple argumentt
a=lambda b: b*5
print(a(4))

x=lambda a,b,c: a+b
print(x(3,4,7))

#LOCAL AND GLOBAL VARAIBLE
#Local 
i.e:
x=3
def s():
    global x
    x=25
    return x
print(s())

x=3
def s():
    x=25
    return x
print(s())

# Practice Problem
#func to find max of three num

def maximum(x,y,z):
    c=max(x,y,z)
print(max(2,7,10))

#square of num in lst 1 till 30
def square(a):
    if a==0:
        return [0]
        
    else:
       return square(a-1)+[a**2] #[0,1]
        
        
print(square(30))

# sum all the num in a lst 
lst=[]

def sum(n):
    c=0
    for i in range(1,n+1):
        c+=i
    lst.append(c)
print(sum(10))
print(lst)
# sum of lst
lst=[2,17,4,1]
def sum (lst):
    c=0
    for i in lst:
        c+=i
    return(c)
print(sum([2,17,4,1]))


# prime or not
def prime(num):

    if num%3==0:
        print('The given num is prime')
    else:
        print('The num is not prime')

    prime=True
    num=int(input('Enter the num: '))
    for i in range(2,num):
        if num%i==0:
            prime=False
            print('The given num is not prime')
            break
    if prime == True:
        print('The given num is prime')      
print(prime(3))
#MODULES
# code banai hoi hongai we just call them

#Datetime
import datetime
x=datetime.datetime.now()
print(x)

# date ki representation data ha
#also find specific date wagera
y=datetime.datetime.now()
print(y.strftime("%A")) # complete day
print(y.strftime("%a")) # day in shortform
print(y.strftime("%B")) # month
print(y.strftime("%m")) #month in num
print(y.strftime("%Y")) #complete year
print(y.strftime("%y")) # year last 2 digit
print(y.strftime("%p")) #am or pm
print(y.strftime("%M")) # mint
print(y.strftime("%S")) # sec
print(y.strftime("%f")) #micro second

# Random module
#pick any value 

import random

x=random.randint(1,10)
print(x)

l=['apple','cherry']
x=random.choice(l)
print(x)

#MAth modul
import math
# max value 
x=max(34,9,17)
print(x)
#min value find
x=max(34,9,17)
print('min',x)
#power
a=pow(3,2)
print(a)

#square root
b=math.sqrt(49)
print(b)

#absolute num
x=abs(-17)
print(x)

x=abs(-9*17)
print(x)

# next to the point num
k=math.ceil(2.5)
print(k)
#previous to the num
k=math.floor(2.5)
print(k)

#CREATION OF MODULE (func banai ga calll nh hoga)
#main.py 
#demo.py (main file)
'''
#NUMPY
#numerical python ,ya func dai ta ha
#Array
#colletion of items of same data time,consume less space
#ist vs array
#canot handle direct mathematic operation in list


#numpy array ma agr sub lst da rahai hu tu don ki len bara br hu 