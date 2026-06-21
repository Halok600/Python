# Strings: ordered, immutable, text representation

my_string = "Hello World!"
string2 = 'I\'m a programmer'
triple_quote = """This is 
multine string mostly used for documentation"""
triple_quote_with_slash = """This is \
multine string mostly used for documentation"""
print(my_string)
print(string2)
print(triple_quote)
print(triple_quote_with_slash)


char = my_string[3]

#my_string[0] = 'h' #cannot happen because immutable
print(char)

substring = my_string[1:5:] #my_string[start_index:end_index:step]

name = "Tom"
greetings = "Hello"
new_sentence = greetings+' '+name
print(substring)
print(new_sentence)

for i in greetings:
    print(i)

if 'e' in greetings:
    print("Yes")
else:
    print("No")

#useful

my_string = '    Hello World!     '
print(my_string)
my_string = my_string.strip()# it does not change the og string we need to assign it again to the string as it string are immutable
print(my_string)

print(my_string.upper()) # similarly lower

print(my_string.startswith('Hello')) # can also be endswith() with word or letter
print(my_string.find('l'))
print(my_string.find("World")) 
print(my_string.find('pp'))
print(my_string.count('o'))
print(my_string.replace('World', 'Universe')) #If does not find the subset it will remain the same as og also here it returns a new string as strings are immutable

my_string = "how are you doing?"
my_list = my_string.split(" ")
print(my_list)
list2 = my_string.split(',')
print(list2)
new_string = ' '.join(my_list) # Important one
print(new_string)

from timeit import default_timer as timer

list3 = ['a']*1000000

# very expensive process to create a string from lists of string/char as it creates a string all the time (as strings are immutable)
start = timer()
my_string = ''
for i in list3:
    my_string += i #here every time new strings is being created as we are adding new char
stop = timer()
print(stop-start)

#Good method
start = timer()
my_string = ''.join(list3)
stop = timer()
print(stop-start)

# Formatting string

#%, .format(), f-strings

#Very old formatting style

#s
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)
#d
var = 3
my_string = "the variable is %d" % var
print(my_string)
#f
var = 3.12324
my_string = "the variable is %.3f" % var
print(my_string)

#by default it has 6 digits

#newer

var = 3.1234567
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var,var2)
print(my_string)

#Latest method
my_string = f'the variable is {var*2} and {var2}'
print(my_string)



