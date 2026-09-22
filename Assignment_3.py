# Q1. 
str=input("Enter the string : ")
i=0
j=len(str)-1
flag=True
while(i<=j):
    if str[i]!=str[j]:
        flag=False
        break
    i+=1
    j-=1

if(flag==False):
    print("Not a Palindrome")
else:
    print("A Palindrome") 

# Q2
lis=[12, 56 ,23.3 ,90 ,10 ,5 ,4]  
sum=0
for i in lis:
    sum+=i

print(lis)
print("")
aveg=sum/len(lis)
print(f"The avg : {aveg}")

# Q3
list1=[]
list2=[]
m=int(input("Enter the size of list1 : "))
n=int(input("Enter the size of list2 : "))

print("Enter the list1 : ")
i=1
while(i<=m):
    list1.append(int(input()))
    i+=1

print("Enter the list2 : ")
j=1
while(j<=n):
    list2.append(int(input()))
    j+=1

print(f"list1 is {list1}{"\n"}list2 is {list2}")    
list3=list1
for ver in list2:
    list3.append(ver)

print("Enter the list3 : ")
print(list3)
print(type(list3))

# Q4
tup=(11,13,78,99,34,33,12,15,18,19,20)
lis1=[]
lis2=[]
for v in tup:
    if(v%2==0):
        lis1.append(v)
    else:
        lis2.append(v)    

tup1=tuple(lis1)
tup2=tuple(lis2)
print(f"{tup1}{"\n"}{tup2}{"\n"}{type(tup1)}{"\n"}{type(tup2)}")

# Q5
dictu={
    "Pooja" : 12,
    "Somya" : 13,
    "Raju" : 50,
    "Rohit" : 30,
    "Priya" : 40
}
print(dictu)
print(type(dictu))

# Q6
words=["apple","banana","kiwi","cherry","mango"]
dic={}
for ier in words:
    dic[ier]=len(ier)

print(f"The dictionary dic : {"\n"}{dic}")
print(type(dic))

# Q7
str23=input("Enter the string : ")
count=0
for wer in str23:
    if(wer==" "):
        count+=1

print(f"number of spaces in string : {count}")

# Q8
list1_=[]
list2_=[]
m=int(input("Enter the size of list1 : "))
n=int(input("Enter the size of list2 : "))
i=1
j=1
print("Enter the element of list1 : ")
while(i<=m):
    list1_.append(int(input()))
    i+=1

print("Enter the element of list2 : ")
while(j<=n):
    list2_.append(int(input()))
    j+=1

print(f"Enter the list1 : {"\n"}{list1_}")
print(f"Enter the list2 : {"\n"}{list2_}")
set1_=set(list1_)
set2_=set(list2_)
if(set1_.intersection(set2_)==set()):
    print("Share no common element")
else:
    print(list(set1_.intersection(set2_)))
    print("Share common element")    

# Q9
lisaa=[]
i=1
m=int(input("Enter the size of the list : "))
print("Enter the list : ")
while(i<=m):
    lisaa.append(int(input()))
    i+=1

print(f" the list : {lisaa}")
setaa=set(lisaa)
lisaa2=[]
for wet in setaa:
    if(lisaa.count(wet)>1):
        lisaa2.append(wet)

print(f"Enter the lisaa2 : {lisaa2}")

# Q10
strrr=input("Enter the string : ")
settii=set(strrr)
print(f"Enter the set : {settii}")
print(f"The count of unique characters : {len(settii)}")

