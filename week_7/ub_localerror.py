counter = 0

def modify_counter():
    counter = counter + 1
    print(counter)

#modify_counter()
#Traceback (most recent call last):
  #File "C:/Users/veda2/OneDrive/Desktop/python lab tasks/week_7/ub_localerror.py", line 7, in <module>
    #modify_counter()
  #File "C:/Users/veda2/OneDrive/Desktop/python lab tasks/week_7/ub_localerror.py", line 4, in modify_counter
    #counter = counter + 1
#UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
counter = 0

def modify_counter():
    global counter
    counter = counter + 1
    print(counter)

modify_counter()
#1
