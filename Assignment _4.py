count=0

class Product:
    count1=0
    def __init__(self,name,price): #constructor
        self.name=name
        self.price=price
        global count
        count+=1
        Product.count1+=1
        print("Object is created")

    def get_info(self): #instance
        print(f"my name is {self.name} and my price is {self.price}")    
    
    @staticmethod
    
    def get_totalObject():  #static
         print(f"Total number of objects created : {count}")

    @classmethod
    def get_totalno_Objects(cls): #class
        print(f"Total number of objects created : -> {cls.count1}") 

    @staticmethod
    def calc_disc(price,dis):
        a=(price*dis)/100
        print(f"Total discount on me is {a}")
    
       
            

p1=Product("Phone",50_000)
p2=Product("Laptop",40_000)
p3=Product("Earbuds",30_000)
p4=Product("Headphones",20_000)
p1.get_info()
p4.get_info()
p4.get_totalObject()
Product.get_totalno_Objects()
Product.get_totalObject()
p1.count1=9
p2.count1=3
print(p1.count1)
print(p4.count1)
print(p2.count1)
p1.calc_disc(p1.price,45)
p2.calc_disc(p2.price,30)




        
    