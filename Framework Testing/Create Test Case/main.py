'''
first import the class name

'''
#project imports :
from stack import Stack

#python imports:
from types import FunctionType
from random import randint,randrange,choice,random
from string import lowercase
import string
import os

__Author__ = "Amir Mohammad & Sepehr"


def my_string(set_len):
    a = randrange(1,100)
    alph = 'abcdefghi jklmnopqr stuvwxyz'
    create_string = ''.join(choice(alph) for i in range(set_len))
    return create_string

class Main:
    
    def get_methods(self,classs):
        init = "__init__"
        a = [x for x, y in classs.__dict__.items() if type(y) == FunctionType]
        if init in a:
            a.remove(init)
        
        return a

    
    def test_int(self,length,cls):
        f= open("test_int.txt","w+")
        result = []
        met = self.get_methods(cls)
            
        for i in range(len(met)):
                
            test_case = str(met[i]) + "("
            for j in range(length-1):
                test_case += str(randint(1,101)) + ","
            test_case += str(randint(1,101)) + ")"
            result.append(test_case)
            f.write(str(test_case)+ "\n")

        f.close()       
        return result

    def test_string(self,length,cls):

        result = []
        f= open("test_string.txt","w+")
        met = self.get_methods(cls)
        for i in range(len(met)):
            
            test_case = str(met[i]) + "("
            for j in range(length-1):
                test_case += str(my_string(length)) + ","
            test_case += str(my_string(length)) + ")"
            result.append(test_case)
            f.write(str(test_case)+ "\n")
        f.close()
        return result


    def test_float(self,length,cls):
        f= open("test_float.txt","w+")
        result = []
        met = self.get_methods(cls)
            
        for i in range(len(met)):
                
            test_case = str(met[i]) + "("
            for j in range(length-1):
                test_case += str(random()*100) + ","

            test_case += str(random()*100) + ")"
            result.append(test_case)
            f.write(str(test_case)+ "\n")

        f.close()       
        return result

        
    def create_test_file(self,class_name):
                            
        class_name = str(class_name).replace('stack','')
        class_name = str(class_name).replace('.','')
        r = open("Stack.py",'r')
        new_r = open("test.py",'w+')
        new_t = open("test_int.txt",'r')

        for l in r:
            new_r.write(str(l))
            print l

        new_r.write("\n")
        new_r.write("\n")
        new_r.write("var_obj = "+str(class_name)+"()"+"\n") #create object
        for a in new_t:
            new_r.write("print "+"var_obj"+'.'+str(a))
            print a
        
        
    def run_test(self):
        """ run the test case file !"""
        run_command = "python test.py > output.txt"
        os.popen(run_command).read
        print "ouput.txt has Created !!!"
        

obj = Main()
#obj.get_methods(Stack)
#obj.test_int(3,Stack)
#obj.test_string(3,Stack)
#obj.test_float(3,Stack)
#obj.create_test_file(Stack)
#obj.run_test()
