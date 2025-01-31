'''def add5(val):
    return val+5
print(add5(100))'''

# single line functions are called lambda functions 
add5=lambda x : x+5
print(type(add5))
print(add5(100))

sm=lambda x:True if x.startswith('M') else False
print(sm('murthy'))
print(sm('deekshith'))
print(sm('Mai'))

alist=['learn','python','step','by','step']
output=list(map(lambda x:x.upper(),alist))
print(type(output))
print(output)

'''score=[66,90,68,59,76,60,88,74,81,65]
def is_A_student(score):
    return score> 75
over_75=list(filter(is_A_student,score))
print(over_75)
'''

score=[66,90,68,59,76,60,88,74,81,65]
##def is_A_student(score):
##    return score> 75
checker=lambda x:x >75
over_75=list(filter(checker,score))
print(over_75)

# sort
list1=[("eggs",5.25),("honey",9.5),("carrots",1.4)]
list1.sort(key=lambda x:x[0],reverse=True)
#True=1 False=0
print(list1)

import numpy as np
x=np.array([1,2,3,4])
#obtain array of square of each element in x
squarer=lambda t:t**2
suuares=np.array([squarer(xi) for xi in x])
print (suuares)












