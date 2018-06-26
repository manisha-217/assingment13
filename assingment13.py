#Q.1. name and handle the exception occured in the following program
try:
 a=3
 if a<4:
     a=a/(a-3)
     print(a)
except Exception :
    print("exception occured")
     #ZeroDivisionError

#Q.2. name an handle the exception occured in the following program
l=[1,2,3]
try :
    print(l[3])
except Exception:
    print("exception occured")
print("indexerror")
# index error
#Q.3.what will the output of following code
#try :
#    raise NameError("Hi there") #raise error
#except NameError:
#    print("An exception")
#    raise # to determine whether the exception was raised or
#answer-    raise NameError("Hi there") #raise error
            #NameError: Hi there

#Q.4. what will be theoutput of following code
# Function which return a/b
def AbyB(a,b):
    try:
         c=((a+b)/(a-b))
    except ZeroDivisionError :
         print ("a/b result in 0")
    else:
        print(c)
AbyB(2.0,3.0)
AbyB(3.0,3.0)
#answer:-  -5.0
          #a/b result in 0
#Q.5. write a program to show and handle following exception
               #1. import error
               #2. value error
               #3. index error
try :
 import pink 

except Exception:
    print("import error occured")
try :
    x=int("abc")
    print("raise error")
except Exception :
    print("value error occured")
    
try :
    l=[1,2,3]
    print(l=[4])
except Exception :
    print("index error occured")
#Q.6 creat a user defined error
class Age(Exception) :
    pass
class AgeTooSmallError(Age):
    pass
n=18
while True:
    try:
        age=int(input("entr your age"))
        if age<n:
            raise AgeTooSmallError
        else :
            print("congress ur age is correct")
            break

    except AgeTooSmallError :
        print("your age is too small than 18")

















 
