
# def functionname( parameters ):
#    "function_docstring"
#    function_suite
#    return [expression]

#1.Required arguments
print("-------------Required arguments----------------")
def printme( str ):
   print(str)
   return

printme("Trilochan")

print("-------------------------------------------------")
#2Keyword Argumnets
print("-------------Keyword Argumnets----------------")
def printinfo( name, age ):
   print("Name: ", name)
   print("Age ", age)
   return;

printinfo( age=50, name="miki" )

print("-------------------------------------------------")
#3Default arguments
print("-------------Default Argumnets----------------")
def printinfo( name, age = 35 ):
   print("Name: ", name)
   print("Age ", age)
   return;

printinfo( age=50, name="miki" )
printinfo( name="miki" )

print("-------------------------------------------------")

#4.Variable-length arguments(*)
print("-------------Variable-length arguments----------------")
def printinfo( arg1, *vartuple ):
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;

printinfo( 10 )
printinfo( 70, 60, 50 )
print("-------------------------------------------------")

#5.Keyword Variable-length arguments(**)
print("--------------------Keyword Variable-length arguments(**)-------------------")

def intro(**data):
   print("\nData type of argument:", type(data))
   for key, value in data.items():
      print("{} is {}".format(key, value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

print("-------------------------------------------------")

#6.Anonymous Functions: lambda [arg1 [,arg2,.....argn]]:expression
print("-------------Anonymous Functions----------------")

sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))

print("-------------------------------------------------")

#7.Return Statement
print("-------------Return Statement----------------")

def sum( arg1, arg2 ):
   total = arg1 + arg2
   print("Inside the function : ", total)
   return total;

total = sum( 10, 20 );
print("Outside the function : ", total)

print("-------------------------------------------------")
#8.Global vs. Local variables
print("-------------Global Vs Local----------------")

total = 0; # This is global variable.
def sum( arg1, arg2 ):

   total = arg1 + arg2; # Here total is local variable.
   print("Inside the function local total : ", total)
   return total;


sum( 10, 20 );
print("Outside the function global total : ", total)
print("-------------------------------------------------")

