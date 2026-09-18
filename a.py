# name='Shreya';
# age=35;
# PI=3.14;
# print(name);
# print(print(name));
# print(type(name));
# print(type(age));
# print(type(PI));
# flag=False;
# print(flag);
# print(type(flag)); 

# a=4
# b=3
# print(a**b)
# a=9
# print(a)
# print(a**b)
# print(a>b)
# print(a<b)
# print(a>b or a<b)
# print(5>2 and 5>4)
# x=9
# print(type(x))
# x+=10
# print(type(x))
# x-=3
# print(type(x))
# x*=4
# print(type(x))
# x/=2
# print(x)
# print(type(x))
# x%=3
# print(type(x))
# print(x)

# print(type(4/2))
# a=int(98.6)
# b=34.5
# print(a)
# print(b)
# c=a+b
# print(c)
# print(type(a))
# print(type(b))
# print(type(c))
# # print(type(a)+"\n"+type(b)+"\n"+type(c)+"\n")
# val=bool(56)
# print(val,type(val))
# val3=bool(0)
# print(val3,type(val3))
# val4=bool(-78)
# print(val4,type(val4))
# a=input()
# print("The value of a : ",a)
# bs=str(input("Enter your name : "))
# print("The bs value : ",bs," ",type(bs))
# age=int(input())
# if age<13 :
#     print("child\n")
# elif age>=13 and age<=18 :
#     print("teenager\n")
# else :
#     print("adult")

# user_name=input("Enter the username : ")
# password=input("Enter the password : ")
# if user_name=="admin" and password=="pass":
#     print("congratulations ! Successfully logged in")
# else:
#     print("Invalid credential")
    
# name=input("Enter the name : ")
# match name :
#     case "Shreya":
#         print("Khup soni kudi")
#     case "Pooja":
#         print("Are khup bdi vali chudail chhe")
#     case "Somya":
#         print("Are vo to sidha nagin chhe")
#     case "Anjali":
#         print("Are uski to jitti tariph kre utti kam,vo to astin ki sap chhe")
#     case "Suhaan":
#         print("Iski ladki baji to kbhi khatam nhi hogi bs neecha dikhana ave chhe")
#     case _:
#         print("Tata bye")    

# i=0
# while i<5 :
#     print("Hello !\n\n")
#     i+=1

# i=1
# N=int(input("Enter the number : "))
# while i<=10:
#     if i==2:
#         i+=1
#         continue
#     if i==8:
#         break
#     print(N*i)
#     i+=1
# print(i)    
    
# string12="hello"
# #in => membership operator -to check presence

# for vp in string:
#     print(vp)
# string ="Shreya"
# if 'o' in string:
#     print("o exists in string")
# else:
#     print("o is not present")    

# for i in range(6): # 0 to 6-1
#     print(i*2)    

# count=0
# word="artificial intelligence"
# for wer in word:
#     if wer=='i':
#         count+=1
# print("number of i present in the word : ",count) 
       
# word="artificial intelligence"
# count=0
# for sw in word:
#     if sw=='a' or sw=='e' or sw=='i' or sw=='o' or sw=='u' :
#         count+=1
# print("number of vowels : ",count)        

# range(start,stop,step)  =>sequencial 
# for i in range(3,9,2):
#     print(i)

# n=int(input("Enter the number : "))
# count=0
# for i in range(1,n+1):
#     count+=i
# print("sum of n natural no : ",count)    

#function
# def finger():
#     print("Hello")

# def apple():
#     print("Good Morning")

# for i in range(1,11):
#     if(i%2!=0):
#         finger()
#     else:
#         apple()    

# def sum(c,d=3):
#     e=c+d
#     print("The sum of",c,"and",d,":",e)

# def calc_avg(a,b,c):
#     d=(a+b+c)/3
#     return d

# y=calc_avg(1,2,3)
# z=calc_avg(4,7,8)
# g=calc_avg(9,5,6)
# print(y,z,g)

# sum(12,90)
# sum(33,77)
# sum(90)
# sum(11)

# p=sum(34,56)
# q=sum(1,5)
# print(p," ",q)
# sum(200,300)
# sum(89,23)
# sum(12,20)

# pre=lambda c,d,e : c+d-e
# print(pre(2,4,5))
# print(pre(90,34,20))
# sum=lambda a,b:a+b
# print(sum(90,12))
# print(sum(99,11))

#factorial of a number N

# def fact(N):
#     count=1
#     for i in range(N,0,-1):
#         count*=i
#     return count
# N=int(input("Enter the number N : "))
# p=fact(N)
# print(p)

# word="School "
# p=len(word)
# print(p)
# # print(word[0])
# print(word[2])

# word="I love my Mammy"
# p=len(word)
# q=word[2:9]
# print(q)
# print(word[:])
# ans=word[-len(word):0]
# print(ans)
     
# word="Aayush_Yadav"
# p=word[:7:-1]
# print(p)
# # word[start:stop:step]
# q=word[::-1]
# print(q)
# w=word[5::-1]
# print(w)

# list => mutable sequence of values

# name="payal"
# age=23
# roll_no=30
# result="Name of student is "+name+" and age is "+str(age)+" and roll no is "+str(roll_no)
# print(result)
# result2="Name of the student is {} and age is {} and roll no is {}".format(name,age,roll_no)
# print(result2)

# a=10
# b=5
# sum=a+b
# result="sum of {} and {} is {}".format(a,b,sum)
# print(result)
#index based formatting
# result1="sum of {1} and {0} is {2}".format(a,b,sum)
# print(result1)
#value based formatting
# result2="sum of {p} and {q} is {r}".format(p=a,q=b,r=sum)
# print(result2)

# F-strings
# a=89
# b=90
# result4=f"sum of {a} and {b} is {(a+b)/2}"
# print(result4) 
# marks=[99,89.75,72,25,60]
# print(marks[0])
#print all the element in marks 
#  for i in range(len(marks)):
#      print(marks[i])
#     #print all the element in marks
# print("")
# for mark in marks:
#     print(mark)    
# marks[3]=50
# print(marks)  
# print(type(marks)) 
# marks[2]="abs" 
# print(marks)
# print(type(marks))
# print(marks[0:2])
# print(marks[:])
# print(marks[3:0:-1])
# print(marks[::-1])
# print(marks[4:0:-1])
# print("")
# python=[99,89,100,65,92,"abc",100.99]
# print(python)
# print(python[4:1:-1])
# print(python[2:5])
# print(python[-5:-2])
# marks=[10,60,45,23,90,80,100]
# print(marks)
# print("")
# marks.append(120)
# marks.insert(3,60)
# print(marks)
# marks.reverse()
# print(marks)
#sort in descending order

# marks.sort()
# print(marks)
# marks.reverse()
# print(marks)

#sort in descending order

# marks.sort(reverse=True)
# print(marks)
# nums=[1,2,3,10,4,10,15]
# for num in nums:
#     print(num)
# print(nums)    
# print("")
# X=int(input("Enter the X : "))
# idx=0
# flag=False
# for num in nums:
#     if(num==X):
#         flag=True
#         print(f"{X} found at index = {idx}")
#         break
#     idx+=1
# if(flag==False):
#     print(f"{X} is not found")    
# string=>immutable sequence of characters
# list=>mutable sequence of values
# tuples=>immutable sequence of values
# table=(90,78,45,"plk",70,60,"olp",12,34)
# print(table)
# print(type(table))
# table[2]='asd' # giving error bcz it is immutable 
# print(table)
# lists=[1,4,1,5,9,7,9,23,9]
# print(lists.index(4))
# lists=[1]
# print(lists)
# yup=(34)  #takes as expression bcz in expression we use parenthesis so when u want 
#ki ye tuple bne you symply put comma at the end
# print(yup)
# print(type(yup))
# yar=(34,)
# print(yar)
# print(type(yar))
# print(type(yar[0]))
# print(yar[0])
# print(table[:])
# print(table[1:])
# print(table[2:6])
# for rulw in table:
#     print(rulw)

# year=(10,20,30,40,50,60)
# sum=0
# for wer in year:
#     sum+=wer
# print(f"The sum of the tuple year is {sum}")
# year.insert(3,37) no insert,append function in  tuple
# print(year)
# year.append(90) 
# print(year)
# year.reverse()
# print(year)

#main point for list
#the alll below function are in list
# insert
# append
# sort
# sort(reverse=True)
# reverse
# index(val)
# count(val)

#main point for tuple
#the only below functions are in tuple
#index(val)
#count(val)



# print(f"the index of 7 in the list is {lists.index(7)}")
# print(f"The total occurence of 9 in the list is {lists.count(9)}")
# print(f"The total occurence of 1 in the list is {lists.count(1)}")
# print(f"The total occurence of 4 in the list is {lists.count(4)}")

# print(hash(1))
# print(hash("apple"))
# print(hash([1,2,3]))
# print(hash((23,45,67)))

# immutable (cannot change) => hashable => dictonary key
# mutable ( can change ) => unhashable => cannnot be the dictionary key
# dictonary in python <=> unordered map in c++
#dictionary is mutable
# popu = {
#     "name": "shraddha",
#     "roll_no": 345,
#     "age": 20,
#     "salary": 1000000,
#     3.14: 12
# }
# popu["class"]="12th"
# print(popu)
# print(type(popu))
# print(popu["salary"])
# print(popu["age"])
# print(popu[3.14])
# print(popu["class"])
# popu["age"]=90
# print(popu)

#methods in dictionary
# keys()
# values()
# items()
# get(val)
# update(new_item)

# apple=popu.keys()
# print(apple)
# print(type(apple))
# banana=popu.values()
# print(banana)
# print(type(banana))
# apple=list(apple)
# banana=list(banana)
# print(apple)
# print(type(apple))
# print(banana)
# print(type(banana))
# tinku=popu.items()
# print(tinku)
# print(type(tinku))
# tinku=list(tinku)
# print(tinku)0
# print(type(tinku))
# asd=popu["app"] #wrong key => giving error
# print(asd)
# asd=popu.get("app") #wrong key => giving None
# print(asd)
# print(popu)
# popu.update({"height": "123cm"})
# print(popu)
# popu["edu"]="pass"
# print(popu)

#set in python <=> unordered set in c++
# set is mutable
# s={10,-5,2,1000,1,1000,1,1}
# print(s)
# print(type(s))
# print(len(s))
# print(id(s))
# s.add(23)
# print(s)
# emp_set={}  #it is dictionary
# emp_set=set({}) #it is set
# print(type(emp_set))

# s={1,2,2,45,-90,1}
# print(s)
# s.add(50)
# print(s)
# s.remove(2)
# print(s)
# s.pop()
# print(s)
# s.clear()
# print(s)
# s1={2,5,6,5,45}
# print(s1)
# s2=s.union(s1)
# print(s2)
# s3=s.intersection(s1)
# print(s3)

# info=[
#     ("Alice","Math"),
#     ("Bob","Science"),
#     ("Alice","Science"),
#     ("Charlie","Math"),
#     ("Bob","Math"),
#     ("Alice","English"),
#     ("Charlie","English")
# ]
# for vap in info:
#     if(vap[1]=="English"):
#         print(vap[0])

# s=set({})
# for vap in info:
#     s.add(vap[1])

# print(s)
# wat={} #dictionary
# for mintu in info:
#     if(wat.get(mintu[0])==None):
#         wat[mintu[0]]=set()
#         wat[mintu[0]].add(mintu[1])
#     else:
#         wat[mintu[0]].add(mintu[1])
# print("")
# print(wat) 