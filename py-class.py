# class Student:
#     def __init__(self,username,age):
#         self.username=username
#         self.age=age
# userOne=Student("A",23)
# userTwo=Student("B",34)

# print(userOne.username)
# print(userOne.age)

# class School:
#     def __init__ (self,teacher, student):
#         self.teacher=teacher
#         self.student=student
# a=School("so","erw")
# b=School("efw","fs")
# print(a.teacher)

# class Student:
#     def __init__(data,name,age):
#         data.name=name
#         data.age=age
#     def display(xyz):
#         print("my name is" + xyz.name+" I am " + str(xyz.age))
        
        
# s1=Student("so",24)
# s1.display()


# class User:
#     def __init__(self,user_id,username):
#         self.user_id=user_id
#         self.username=username
#         self.followers=0
#         self.following=0
#     def follow (self,user):
#         user.followers+=1
#         user.following+=1
# user1=User(1,"usf")
# user2=User(2,"fs")

# user1.follow(user2)
# print(user1.followers)
# print(user1.following)        
# print(user2.followers)
# print(user2.following)

# class Calculate:
#     def __init__ (self,numOne,numTwo, numThree):
#         self.numOne=numOne
#         self.numTwo=numTwo
#         self.numThree=numThree
        
#     def add(xyz):
#         return xyz.numOne+xyz.numTwo+xyz.numThree
    
#     def minus(xyz):
#         return xyz.numOne-xyz.numTwo-xyz.numThree  
#     def multiply(xyz):
#         return xyz.numOne*xyz.numTwo*xyz.numThree
# one=Calculate(1,2,3)
# print(one.add())
# print(one.minus())
# print(one.multiply())

# class Animal:
#     def __init__(self,name,favfood):
#         self.name=name
#         self.favfood=favfood
#     def eat(x):
#         return x.name + " likes to eat "+ x.favfood
# first=Animal("Jojo","meat")
# print(first.eat())

# class Parent:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
        
#     def display(self):
#         print(self.fname, self.lname)
        
# class Child(Parent):
#     pass
    
        
# a=Child("sd","sff")
# a.display()

        
# class Animal:
#     def __init__(self,name,gender,food):
#         self.name=name
#         self.gender=gender
#         self.food=food
        
#     def release(self):
#         return "it's a "+self.gender
#     def display(self):
#         return int(self.gender)+1
#     def eat(self):
#         return self.name +" likes to eat "+self.food
# class Dog(Animal):
#     pass
# a=Dog("James","2","meat")
# print(a.release())
# print(a.display())
# print(a.eat())      


#polymorphism        
# class Flower:
#     def __init__ (self,color,name):
#         self.color=color
#         self.name=name
#     def display(self):
#         print("beautiful")
# class Fruit:
#     def __init__ (self,color,name):
#         self.color=color
#         self.name=name
#     def display(self):
#         print("tasty")        
# class Tea:
#     def __init__ (self,color,name):
#         self.color=color
#         self.name=name
#     def display(self):
#         print("good")          
# Flower1=Flower("Red","Rose")    
# Fruit1=Fruit("Yellow","Banana")
# Tea1=Tea("BlackTea","Red")
# for x in (Flower1,Fruit1,Tea1):
#     x.display()
        
#write a python code to find the sum of 1st 10 odd numbers if the number is 3, 7 and 9 ignore to the summation      

# i=-1
# sum=0
# while i<19:
#     i+=2
#     if i==3 or i==7 or i==9:
#         continue
#     sum+=i
#     print(i)
# print(sum)    
    
# #2.write a python code to find a number is even or not 

# num=4
# if num%2==0:
#     print("even")
# else:
#     print("not even")
        
# 3.write python code to find the average of students if they scored >80 else just throw a mssg that you are not qualified         

# score=[23,45,23,54,90,99,67,98,98,98,90]  
# sum=0
# for x in score:
#     sum+=int(x)

# avg=sum/len(score)
# print(avg)        
# if avg>80:
#     print("pass")
# else:
#     print("fali")
        
        
class Animal:
    def __inti__ (self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display_name(self):
        print("my name is "+ self.name)
    def display_age(self):
        print("i am " + self.age + "years old")
    def display_gender(self):
        print("I am a " + self.gender)
class Dog(Animal):
    pass
a= Dog("Luke","2","boy")
dog2= Dog("Lola","3","girl")
a.display_name()        



 