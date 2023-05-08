print("This is one.py")
def func():
    print("My func has been run")
def myfunc():
    print("one.py is being run")
# similar to a main function to c++ and java
if __name__=="__main__":
    myfunc()
else:
    print("one.py has been imported")

