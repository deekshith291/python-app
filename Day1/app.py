''' Custom module:app.py'''
import os,sys
name="deekshith" #gloabl varaiable
def greet(ename):
    os.system('cls')
    data=[10,20,'murthy'] # private variable
    print(type(data))
    emps=[{'eno':101,'ename':'naga'},{'eno':102,'ename':'kiran'}]
    print(type(emps))
    print(emps)
    first,second=(100,200)
    print(first)
    


if __name__=='__main__':
    greet("murali")
    sys.exit()