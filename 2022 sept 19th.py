from multiprocessing.sharedctypes import Value
2022/09/19

Parameters

def add_sub(num1, num2, num3):
    """add_sub does the following:
    Add the first two parameters
    Subtract the third paramter
    Print the result"""
    print(num1 + num2 - num3)

add_sub(5, 10, 15)

굳이..
# declare def and then add at the last

def subtract(num1, num2):
    """Subtract the second parameter from the first"""
    print(num1 - num2)
    
subtract(5, 2)
subtract(2, 5)
subtract(num2=2, num1=5)
1"""직접 이름 지정 가능
subtract(num2=2, num1=5) 이렇게"""

def parameter_types(param1, param2, param3, param4):
    """Takes four parameters
    Print the type of each element"""
    print("The type of {} is {}".format(param1, type(param1)))
    print("The type of {} is {}".format(param2, type(param2)))
    print("The type of {} is {}".format(param3, type(param3)))
    print("The type of {} is {}".format(param4, type(param4)))
        
parameter_types(1, 5.9, "Beatles", False)
# {} 하고 .format으로 link한다. 

*try... except*
def addition(num1, num2):
    """Add the two parameters together
    Use try/except to catch any errors"""
    try:
        print(num1 + num2)
    except:
        print("There is an error in your code.")
    
addition(5, "cat")
"""thier is ~~   except 하면 에러나면 내놔라!!"""

def add_if_true(num1, num2, bool = True):
    """Prints the sum of two numbers
    if the variable bool is true"""
    if bool:
        print(num1 + num2)
    else:
        print("No addition, bool is false")

add_if_true(5, 7)
add_if_true(5, 7, False)
"""이런식으로 if 쓸수도 있음"""



returning Value
def add_five(num):
    """Add five to the parameter num"""
    return(num + 5)
  
add_five(10)
'''이거는 print안됨'''

def add_five(num):
    """Add five to the parameter num"""
    return(num + 5)
  
new_number = add_five(10)
print(new_number)
'''이렇게 바꿔줘야함'''

*List Method*
ex) my_list. append("hi")
#list name and '.'(period), list method, 괄호, method parameter

my_list = [1, 2, 3]
new_element = 4

my_list.append(new_element)
print(my_list) 
'''요렇게'''

*Pop Method*
'''얘는 method parameter 필요업음'''
ex_) my_list.pop()

my_list = [1, 2, 3, 4]
print(my_list)
print(my_list.pop())
print(my_list)
'''[1,2,3,4], 4, [1,2,3] 이 나옴   왜냐면 아무것도 안 넣어주면 마지막 -1 index나옴'''

*insert method*

my_list = [1, 2, 3, 4]
my_list.insert(2, "Hi")
print(my_list)
'''index 두번째를 hi로 바꾸거라'''

*remove method*
my_list = [1, 2, 3, 3, 4]
my_list.remove(2)
print(my_list)

Pop vs	                            Remove
Removes an element	            Removes an element
Removes based on index	        Removes based on value
Returns the removed value	    Does not return anything

*count*
'''갯수세기'''
my_var = 2
my_list = [2, "red", 2.0, my_var, "Red", 8 // 4]
print(my_list.count(2))
'''2가 총 4개 있으니까 4가 출력됨'''

*The Index Method*
'''index알려줌'''

*The Sort Method*
'''sord해줌 같은 종류만 가능, 대소문자도 분류가능'''
my_list = [23, 55, 11, 7, 82.9, -14, 0, 34]
print(my_list)
my_list.sort()
print(my_list)

my_list = [23, 55, 11, 7, 82.9, -14, 0, 34]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
'''이건 내림차'''

my_list = ["north", True, 45, 12, "red"]
print(my_list)
my_list.reverse()
print(my_list)
'''이건 단순히 순서 반대로 내줌'''
['north', True, 45, 12, 'red']
['red', 12, 45, True, 'north']
요렇게

*The Sum Function*
'''int만 가능 말그대로 더하기'''


*the min function*
'''제일 작은 수를 출력함 string에 사용하면 알파벳 순으로 나옴, 
int랑 섞어도 가능하고{이것만 가능("숫자"), (숫자)이거는 안됨} 무조건 string형식만 가능'''
*max 도 있지롱*

*Iterating*
'''반복문 for과 유사'''
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)
'''mumbers: list to literate over, number: varivalbe,   '''