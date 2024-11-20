import numpy as np
import statistics as stats

#multi dimensional array ,same col and row
'''
a=np.array([[4,6,8,9],[12,22,5,78]])
print(a)
print(type(a))
#slicing
a=np.array([4,6,8,9])
print(a[2:])
#multi slicing
a=np.array([[4,6,8,9],[12,22,5,78]])
print(a[0:2,0:2])#also same element hu
print(a[1,2:4])#jis bhi array ka element chahaiyai oska pehlai index num lwhko then slicing like [0,1:3]

b=np.array([[4,6,8,9],[12,22,5,4],[33,55,77,88]])
print(b[2,3:])

print(np.shape(b))#num of row and shape ai ga
print(np.size(b))# how many element
print(np.ndim(b))#for dimension 
print(b.dtype)#for type array ka ander moojod type

##FUNCTION
a=np.array([3,67,89,4])
print(a.shape) #array dimension
print(len(a)) #lenght of aaray
print(a.astype(str)) #conversion of data type


a=np.array([[3,67],[89,4]])
a2=np.array([[3,6],[0,3]])
print(a,a2)
print(np.add(a,a2))#operations ha inkai or func
print(np.divide(a,a2))
b=np.array([3,67])
b2=np.array([3])
print(np.power(b,b2))
print(np.sqrt(b))
b=np.array([[4,16],[49,9]])#also
print(np.sqrt(b))

#concatenate
a=np.array([2,4,6])
b=np.array([3,67])
print(np.concatenate([a,b]))
a=np.array([[2,4],[0,6]])
b=np.array([[3,67],[77,9]])
print(np.concatenate([a,b],axis=1))#first first walai conc
a=np.array([[2,4],[0,6],[7,9]])
b=np.array([[3,67],[77,9],[4,6]])
c=np.array([[2,4],[77,9],[4,6]])
print(np.concatenate([a,b,c],axis=1))
#ek array ma ajai ga sb first walai first ka sath
#without axis given tu bhi ek array ma alg alg ai ga
#horizontal concatenation
print(np.hstack([a,b]))
#vertical
print(np.vstack([a,b]))

#split
c=np.array([3,67,12,44,90])
print(np.array_split(c,3))

c=np.array([[3,67,12],[44,90,45],[3,67,99]])
print(np.array_split(c,4))#num of rows or nh ha jo thi wo da deya or phr baqi ma blank lst or type bata di


a=np.array([[4,6,8,9,1,1],[2,2,12,22,5,78],[3,3,44,90,45,55],[3,4,5,67,99,22]])
print(a[0:3,:-2]) #first colum batai ga ka konsi row chahiyai

#append
a=np.array([[3,67,12],[44,90,45],[3,67,99]])
print(np.append(a,90))
print(np.append(a,[90,80,99]))#jitna element ha utna hee add karwao ya one karwao srf
#insert
print(np.insert(a,1,50))
print(np.insert(a,[1,3],[50],axis=1))

#[[ 3 50 67 12 50]
 #[44 50 90 45 50]
 #[ 3 50 67 99 50]]
 
print(np.insert(a,[1,3],[50,67,6],axis=1))#ismai error ai ga kiu ka 1 or 3 ma num zada ho jatai bqi ma nh 
#print(np.insert(a,[1,3],[50,67,9],axis=0))#he index ka 3 or 1 pr bhi kar ka da raha 

[[ 3 67 12]
 [50 50 50]
 [44 90 45]
 [ 3 67 99]
 [50 50 50]]

print(np.delete(a,1))
print(np.delete(a,1),axis=1)

#sort
a=np.array([3,67,12])#only one array  pr
print(np.sort(a))

#search
s=np.where(a==3)
print(s)

s=np.where(a%2==0)#all even num ka index ai ga
print(s)

ss=np.searchsorted(a,2)#array sorted hu

#Filter
a=np.array([2,30,89,0]) #jidhar true lehk rahai hain wahn pr wali value ai gi new array ma or jitna element hu utna hee true wagera
b=[True,False,True,False]#boolean matrix
print(a[b])
#even walai
c= a%2==0
new=a[c]
print(new)

print(a[a%2==1])

#aggregating func in array
a=np.array([2,30,89,0])
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.size(a))
print(np.mean(a))
print(np.cumsum(a)) #phela or dosra ko add karna 
print(np.cumprod(a))

a=np.array([11,10,16,14,19,77])
b=np.array([2,9,6,4,5])
price=np.array(a)
quantity=np.array(b)

print(price,'\n',quantity)
print()

c=np.cumprod([price,quantity],axis=0)
print(c[1].sum())
'''
#Statistical func
baked_food=[200,120,100,200,800,300]
a=np.array(baked_food)
print(np.mean(baked_food))#sum of all the values divided by num of values(avg)
print(np.median(baked_food))#bari value or min value ko add kar ka 2 sa divide kar ka jo ans ai wo 
print(stats.mode(baked_food))#(same num of occurance ha agr do values ki tu wo fifo method use karai ga0.(library la ga mode ka func nh hota alag sa or statistic builtin library ha)most repeated value
#sorted array ma median center wala hoga
print(np.std(baked_food)) #standard deviation os mean sa kitni durr ha wo value onko add kar ka osai divide karda ga total num of values sa
print(np.var(baked_food))

#Corelation (do chezai apas ma relate krti hain ya nh)
inflation=np.array([34,89,90,55,12])
deaths=np.array([15,150,28,90])
print(np.corrcoef([inflation,deaths]))















