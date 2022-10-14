import argparse


#defining support function-->

def verbose():
    print("Print the verbose here")
    print("\n\n")
    while 1:
        print("Go to the following pages of the program-->")
        print("1. Version\n2. Method details\n3. Go to main Program\n4. Exit")
        char = input("Enter your choice -->")
        if char == "1":
            version()
            pass
        elif char == "2":
            method()
            pass
        elif char == "3":
            mainfunc()
            
        elif char == "4":
            exit(0)
        else:
            print("wrong choice")
            pass
        
def version():
    print("The ongoing version is V1.1.0")
    print("\n\n")
    while 1:
        print("Go to the following pages of the program-->")
        print("1. Verbose\n2. Method details\n3. Go to main Program\n4. Exit")
        char = input("Enter your choice -->")
        if char == "1":
            verbose()
            pass
        elif char == "2":
            method()
            pass
        elif char == "3":
            mainfunc()
        elif char == "4":
            exit(0)
        else:
            print("wrong choice")
            pass    
        
def method():
    
    print("Here we have the following list of Functions -> \n1. sqr\n2. add\n3. isodd\n")
    temp = input("Please provide the method name you want to know abbout: ")
    if temp == "1":
        print(help(sqr))
    if temp == "2":
        print(help(add))
    if temp == "3":   
        print(help(isodd))
        
    print("\n\n")
    while 1:
        print("Go to the following pages of the program-->")
        print("1. Version\n2. Verbose\n3. Go to main Program\n4. Exit")
        char = input("Enter your choice -->")
        if char == "1":
            version()
            pass
        elif char == "2":
            verbose()
            pass
        elif char == "3":
            mainfunc()
            
        elif char == "4":
            exit(0)
        else:
            print("wrong choice")
            pass   
        
        
        
def Help():
    print("The command lines available in this programme is --> \n-v for verbose\n-V for version\n-m for module details")
    print("\n\n")
    while 1:
        print("Go to the following pages of the program-->")
        print("1. Version\n2. Method details\n3. Go to main Program\n4. Exit")
        char = input("Enter your choice -->")
        if char == "1":
            version()
            pass
        elif char == "2":
            method()
            pass
        elif char == "3":
            mainfunc()
            
        elif char == "4":
            exit(0)
            
        else:
            print("wrong choice")
            pass
            
    
#defining work functions-->
def mainfunc():
    
    n = int(input("Please provide the Number to start with -->"))
    print("Here we have the following list of Functions -> \n1. sqr\n2. add\n3. isodd\n4. Exit")
    temp = input("Please provide the method name you want to know abbout: ")
    while 1:
        if temp == "1":
            r = sqr(n)
            print("The square of the given value is {}".format(r))
            break
        elif temp == "2":
            r = add(n)
            print("The addition result is {}".format(r))
            break
        elif temp == "3":   
            r = isodd(n)
            if r==1:
                print("The Number is even")
            else:
                print("The number is odd")
            break    
        elif temp == "4":
            exit(0)
        else:
            print("Wrong input...")
            pass
        
    print("\n\n")    
    while 1:
        print("Go to the following pages of the program-->")
        print("1. Version\n2. Method details\n3. Go to main Program AGAIN\n4. Exit")
        char = input("Enter your choice -->")
        if char == "1":
            version()
            pass
        elif char == "2":
            method()
            pass
        elif char == "3":
            mainfunc()
            
        elif char == "4":
            exit(0)
            
        else:
            print("wrong choice")
            pass


def sqr(n):
    '''
    This function is used to find the SQUARE of the given number
    '''
    return (n*n)
def add(n):
    '''
    This function is used to find the ADDITION of the given number with itself
    '''
    return (n+n)
def isodd(n):
    '''
    This function is used to find the given number is odd or even
    '''
    if (n%2) == 0:
        return 1
    else:
        return 0
        
#commandline parsing using argpaese -->
          
'''
Pass ArgumentParser a conflict_handler="resolve" argument, helps to modify the -h text, but --help will works as default.
'''

parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument('-v', '--verbose', help='This programme is used for....', action='store_true')
parser.add_argument('-V', '--version', help='Print the version of the project', action='store_true')
parser.add_argument('-h', '--Help', help='This programme is use to test the command line parsing', action='store_true')
parser.add_argument('-m', '--module', help='Print the details about the method', action='store_true')

args = parser.parse_args()

if args.verbose:
    verbose()
    
elif args.version:
    version()

elif args.Help:
    Help()
    
elif args.module:
    method()

else: 
    mainfunc()       
         
        
