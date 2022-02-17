import requests,json

#first question
class Shape:
    def __init__(self,area,hekef):
        self.__area=None
        self.__hekef=None
        self.area=area
        self.hekef=hekef
    def __str__(self):
        return f"Shape area = {self.area},hekef = {self.hekef}"

    def __repr__(self):
        return f'Shape({self.area},{self.hekef}'

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self,x):
        if 0 < x:
          self.__area = x
    @property
    def hekef(self):
        return self.__hekef

    @hekef.setter
    def hekef(self,n):
        if 0 < n:
            self.__hekef = n

#second question
class Post:
    def __init__(self,d):
        self.__dict__ = d
    def __str__(self):
            result = ""
            for k, v in self.__dict__.items():
                result += str(k) + ":" + f"{v}" + "\n"
            return result

num = int(input("enter a number between 1 to 100"))
response = requests.get("http://jsonplaceholder.typicode.com/posts")
lst = json.loads(response.content)
for i in range(len(lst)):
    if lst[i]["id"] == num:
        new_data = Post(lst[i])
        print(new_data)
        break

#first bounes
#the diffrence comes in their oreder(meaning if there is a certain order that is seen by the index of each cell)
#and if they are changeable(meaning if you can change there values)
#and also if you can duplicate them
#list is ordered and changeable and duplicated
#set is unordered,unchageable and unduplicated
#tuple is ordered,unchangeable and duplicated

#second bounes
numero = int(input("enter your number"))
for i in range(numero):
    for k in range(i + 1):
        print("*",end=' ')
    print("\n")
for j in range(numero - 1,0,-1):
    for a in range(j):
        print("*",end=' ')
    print("\n")
