'''
first imports the class .
'''
class Stack:
     def __init__(self):
         self.a = 0
         self.b = 0
         self.c = 0

     def zarb(self,a,b,c):
         return a*b*c

     def jam(self,a,b,c):
         return a+b+c

     def menha(self,a,b,c):
         return a-b-c

     def peek(self,a,b,c):
         return a+b-c


var_obj = Stack()
print var_obj.peek(73,22,24)
print var_obj.jam(78,72,43)
print var_obj.menha(56,37,78)
print var_obj.zarb(75,14,14)
