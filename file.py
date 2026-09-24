# f=open("./sample.txt","r") #file object
# data=f.readline()
# print(data)
# print(type(data))
# print(type(f))
# data=f.readline()
# print(data)
# f.close()
# f=open("./sample.txt","w")
# data=f.write("Gadha khi ka")
# f.close()

# with keyword automatically close the file, we dont have to explicitely close it 

# with open("./sample.txt","r") as f:
#     data=f.read()
#     print(data,f"\nlenght of the file is {len(data)}")

# f=open("./f.txt","a")
# f.write("pol")
# f.close()

# modes 

# r  reading [default]
# w  writing truncate file first
# x  create new and open for writing
# a  writing appends at end 
# b  binary mode 
# t  text mode [default]
# +  apple to do both operations read and write

# with open("./sample.txt","r") as f:
#     count=1
#     data=f.readline()
#     while(data!=""):
#         if "python" in data:
#             print(f"the word is present at line {count}")
            
#         count+=1
#         data=f.readline()


# try -> the block where the possibility of occuring an error 
         # though it can be throw a error or not but where there is any doubt we simply put that part in try
# except the error name : and here this is catching that throw that error and here we write that thing which we want to be
# shown as output if any error is occured

# try:
#     x=int(input("Enter the x  : "))
#     abc=10/x

# except ValueError:
#     print("invalid input")

# except ZeroDivisionError:
#     print("Division by 0 is not possible")

# else:
#     print(abc)

# finally:  #if we want the some code that should be always execute irrespective of exception thrown or not 
#     print("Our program was done")  

# li=[]
# for i in range(6): #0 to 5
#     li.append(i*i)

# print(li)    

# sq=[i*i for i in range(6)]
# print(sq)

# ad=[i+2 for i in range(9)]
# print(ad)

# sqp=[i*i for i in range(6) if(i%2!=0)]
# print(sqp)

# lip=[-2,-4,3,5,2,-1]
# for i in range(len(lip)):
#         if(lip[i]<0):
#           lip[i]=0
        
# print(lip) 

# # 1. basic structure
# # [kya chahiye  for item in list]
# num=[1,2,3,4]
# res=[]
# res=[x*2 for x in num]
# print(res)

# # 2. sirf filter krna-> sirf if bina else ke
# # jb kuch elements lo select krna ho or baki ko chhod dena ho tb if last me lgta h
# #[kya chahiye  for item in list  if condition]
# num1=[1,2,3,4,5,6]
# evens=[]
# odds=[]
# evens=[u  for u in num1 if u%2==0]
# odds=[p  for p in num1 if p%2!=0]
# print(evens,"\n",odds)

# # 3. value badalna -> jb if ke sath else bhi ho
# # jb hr element ko rkhna h lekin condition ke hisab se value badalni ho
# lite=[-4, -5, 6, 9, 1, 4, -3]
# k=[0 if j>0 else j+5 for j in lite]
# print(k)

# words=["hello","python","apnacollege"]
# words=[kl.upper()   for kl in words]
# print(words)










    

 






   
    



