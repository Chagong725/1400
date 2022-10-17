from dataclasses import dataclass
from turtle import right
from symbol import flow_stmt


2022 10 10
Helper functions are any functions which provide a result that is used by another function. 
Helper functions can be declared outside of the function it helps. 
Or, a helper function can be declared inside the function it helps.

ex)피타고라스 정리로 반지름 구하기 (루트(x2−x1)^2+(y2−y1)^2)
import math

def radius(x1, y1, x2, y2): 반지름 정의
    """Distance formula to determine the radius of a circle"""
    return(math.sqrt((x2 - x1)**2 + (y2 - y1)**2)) math모듈에서 루트 사용(square root==sqrt)
  
def area(x1, y1, x2, y2):
    """Area of a circle function"""
    return(math.pi * radius(x1, y1, x2, y2)**2)

print(area(0, 0, 4, 4))

return(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))) 요것도 가능 pow가 제곱임
return(math.pi * math.pow(radius(x1, y1, x2, y2), 2))요것도 가능

Inner Functions
이너 펑션은 메인 프로그램에서 사라지게 하는거임
import math
  
def area(x1, y1, x2, y2):
    """Area of a circle function"""
    def radius(x1, y1, x2, y2):
        """Distance formula to determine the radius of a circle"""
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    
    return(math.pi * math.pow(radius(x1, y1, x2, y2), 2))
  
print(area(0, 0, 4, 4)) area를 radious로 바꾸면 에러남 왜냐면 The Python program cannot "see" inside the area function

Function Composition
두개 이상의 함수를 사용함 큰 작업할때 사용 help랑 비슷함 하지만 좀 더 구체적. parameter(매개변수) 로 사용
When a function has another function as a parameter, this is called function composition.


import math

def area(r): area는 parameter 사용 안함 value를 필요로 함
    """Area of a circle"""
    return(math.pi * math.pow(r, 2))

def radius(x1, y1, x2, y2):
    """Distance formula to calculate the radius"""
    return(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))

print(area(radius(0, 0, 4, 4))) radious를 먼저 실행해서 그 값을 area로 보냄, 
function1(function2(7)) 요런식으로 되어있는게 composition임

helper vs composition
거의 같은 기능을 함 하나를 다른데다 써도 결과는 다르지 않음
circle_area1(x1, y1, x2, y2) #데카르트 평면 정의인지 확실하지 않음
circle_area2(radius(x1, y1, x2, y2), math.pi) #파이와 반지름이 면적을 계산하는데 사용됨을 ㅏㄹ 수 있음

helper는 user define function임

print(len(str(math.sqrt(math.pow(3, math.degrees(math.sin(5.79))))))) 이거는 파이썬은 읽지만 인간이 읽기는 복잡함

step1 = math.degrees(math.sin(5.79))
step2 = math.sqrt(math.pow(3, step1))
step3 = len(str(step2))
print(step3) 이렇게 쪼개주는게 더 좋음

Modularity
func기능의 또다른 이점임. Modularity means dividing a program into separate and independent units
재사용 됨(,reusable)
그림그리기

집을 그리기.  삼각형과, 직사각형, 시작점을 바꾸는 기능이 필요함
import turtle

t = turtle.Turtle()

def triangle(size):
    """Draw a triangle with a given size"""
    for i in range(3):
        t.lt(120)
        t.forward(size)

def rectangle(width, height):
    """Draw a rectangle with a given width and height"""
    for i in range(2):
        t.forward(width)
        t.lt(90)
        t.forward(height)
        t.lt(90)
        
def reposition(x, y):
    """Pick up the pen, move the turtle, set the
    direction of the turtle, and put the pen down"""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
        
rectangle(100, 100) #draw the house 시작 좌표임
reposition(100, 100) #move to starting point for the roof
triangle(100) #draw the roof
reposition(40, 0) #move to starting point for the door
rectangle(20, 40) #draw the door
reposition(10, 50) #move to starting point for the left window
rectangle(20, 20) #draw the left window
reposition(70, 50) #move to starting point for the right window
rectangle(20, 20) #draw the right window

turtle.mainloop()

함수가 parameter로 사용됐음. Modularity makes functions reusable.

internal function을 사용해서
def force(dv, time, mass):
    """Calculate force"""
    def acceleration(dv, time):
        """Calculate acceleration"""
        return(dv / time)
    return(mass * acceleration(dv, time))
요렇게 쓸 수 있음

velocity = change in position / time
position_change = final_position - starting_position 일때
starting position is 0, the final position is 100 and the time is 30 구해라

velocity(position_change(0, 100), 30) 이렇게 씀

Local Scope
def function_1():
    my_var = "Hello"
    print(my_var)
    
def function_2():
    print(my_var)
    
function_1()
function_2()
에러남 왜냐면 함수 1에만 정의되어있음 2는 정의 안됨

More Local Scope
def function_1():
    my_var = "Hello"
    print(my_var)
    
def function_2():
    my_var = "Bonjour"
    print(my_var)
    
function_1()
function_2()
요렇게 쓰는 것는 가능함 같은 var을 같고 있어도 각각 다름

Global Scope - Referencing Variables
When a variable is declared in the main program, it has global scope. 
Global variables are declared outside of functions, but can be referenced inside a function.

greeting = "Hello"

def say_hello():
    """Print a greeting"""
    print(greeting)

say_hello()
hello가 나옴 왜냐? 이미 gretting==hello라고 정의해놨으니 선수쳤음

greeting = "Hello"

def say_hello():
    """Print a greeting"""
    greeting = "Bonjour"
    print(greeting)

say_hello()
print(greeting)
요거는 당연히 봉쥬르 헬로 나옴

Global Scope - Modifying Variables
수정은 안됨 아까도 둘다 나온 것처럼 하지만 global keyword쓰면 수정 가능
greeting = "Hello"

def say_hello():
    """Demonstrate how to use the global keyword"""
    global greeting
    greeting = "Bonjour"
    print(greeting)

say_hello()
print(greeting)
그냥 글로벌적어줌

Global vs Local Scope
로컬과 글로벌이 충돌하면 항상 로컬이 우선순위

my_var = 5
def add_5():
    print(my_var + 5)
add_5()
10나옴


Building a Command Line Application
https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea
이사이트에 있는 영화처럼 sort할 예쩡
import csv

movie_csv = "student_folder/.labs/movie_data.csv"

def fetch_movie_data(movie_csv):
    """Return movie data from a CSV file"""
    pass #자리표시자로 함수가 작성되지 않아도 오류없이 출력, 

movie_data = fetch_movie_data(movie_csv) 
print(movie_data)

none이 나옴

import csv

movie_csv = "student_folder/.labs/movie_data.csv"

def fetch_movie_data(movie_csv):
    """Return movie data from a CSV file"""
    with open(movie_csv, "r") as movie_file:
        reader = csv.reader(movie_file)
        movie_info = [] #로컬 var 생성
        for row in reader: #리터레이트 
          movie_info.append(row) #row를 로컬 var에 추가
        return movie_info #반환

movie_data = fetch_movie_data(movie_csv) 
print(movie_data)

[['Film', 'Genre', 'Rotten Tomatoes %', 'Worldwide Gross', 'Year'], ['Zack and Miri Make a Porno', 'Romance', '64', '41.94', '2008'] ....
요렇게 나옴

이제는 정리할 예정
import csv

movie_csv = "student_folder/.labs/movie_data.csv"

def fetch_movie_data(movie_csv):
    """Return movie data from a CSV file"""
    with open(movie_csv, "r") as movie_file:
        reader = csv.reader(movie_file)
        movie_info = [] #print는 대괄호를 출력함
        for row in reader:
          movie_info.append(row)
        return movie_info

def print_movie_data(data): #새로운 함수
    """Print the movie data in easy to read columns"""
    for title, genre, rotten, gross, year in data: #unpacking
      print("{:36} {:10} {:18} ${:16} {}".format(title, genre, rotten, gross, year))
      #:10 오른쪽에 패딩(공백 만들기) 추가(268참조) 이렇게 하면 깔끔하게 정렬됨
      # 돈관련을 알 수 있도록 총액에 $추가
      
movie_data = fetch_movie_data(movie_csv) 
print_movie_data(movie_data) #print_movie_data 이거 추가하고 print(movie_data)이건 지워

Film                                 Genre      Rotten Tomatoes %  $Worldwide Gross  Year
Zack and Miri Make a Porno           Romance    64                 $41.94            2008
요런식으로 깔끄맣게 나옴
Formatting a String with Padding
1. 10 space of padding on the right: "{:10}".format("test")
result:   test하고6개의 공백이 생김(토탈 10글자)(test......) ".을 스페이스라고 가정해서 적음"
2.                     on the left: "{:>10}".format("test")
result:   왼쪽에 공백 6개 그리고test적힘 (......test)
3. 중앙에 글을 적고 싶음(양옆 공백) "{:^10}".format("test")
결과 (...test...)
4. 10 "_" of padding on the right "{:_<10}".format("test")
result (test_ _ _ _ _ _)


Sorting the Movie Data
아까 방식으로 daa를 처리하기에는 까다랑ㅁ 왜냐면 it is a list of lists
outer list에서 sort하면 알파벳으로 정렬됨

import csv, operator #operator 모듈을 csv와 함께 가져온다.

movie_csv = "student_folder/.labs/movie_data.csv"

def fetch_movie_data(movie_csv):
    """Return movie data from a CSV file"""
    with open(movie_csv, "r") as movie_file:
        reader = csv.reader(movie_file)
        movie_info = []
        for row in reader:
          movie_info.append(row)
        return movie_info

def print_movie_data(data):
    """Print the movie data in easy to read columns"""
    for title, genre, rotten, gross, year in data:
      print("{:36} {:10} {:18} {:16} {}".format(title, genre, rotten, gross, year))
      
def sort_movie_data(data, index): #data parameter와 index로 함수 만들기
    """Sort movie data based on the column data"""
    pass #그만하거라
      
movie_data = fetch_movie_data(movie_csv) 
print_movie_data(movie_data)

Film                                 Genre      Rotten Tomatoes %  Worldwide Gross  Year
Zack and Miri Make a Porno           Romance    64                 41.94            2008
요렇게 나옴(이름 역순 z-a-숫자)

import csv, operator

movie_csv = "student_folder/.labs/movie_data.csv"

def fetch_movie_data(movie_csv):
    """Return movie data from a CSV file"""
    with open(movie_csv, "r") as movie_file:
        reader = csv.reader(movie_file)
        movie_info = []
        for row in reader:
          movie_info.append(row)
        return movie_info

def print_movie_data(data):
    """Print the movie data in easy to read columns"""
    for title, genre, rotten, gross, year in data:
      print("{:36} {:10} {:18} {:16} {}".format(title, genre, rotten, gross, year))
      
def sort_movie_data(data, index): #index parameter는 inner list를 sort하는데 필요한 요소를 알 수 있다.
    """Sort movie data based on the column data"""
    header = data[0] #모든 data를 정렬하면 섞임 헤드랑, 그래서 헤드를 따로 선언해준다.
    sorted_movies = data[1:]
    # #영화 정렬하는 새로운 걸 선언, 첫번째 row(colmm 타이틀)의 무비데이터는 hreader로 저장됨
    # 나머지 데이터는 sorted_movies에 들어감
    sorted_movies.sort(key=operator.itemgetter(index)) '''여기서 sort method사용함 괄호 사이는 무슨 뜻인지..'''
    sorted_movies.insert(0, header)
    return sorted_movies #데이터 반화
      
movie_data = fetch_movie_data(movie_csv) 
print_movie_data(sort_movie_data(movie_data, 0))
'''이전에 사용했던 print_movie_data(movie_data)를 print_movie_data(sort_movie_data(movie_data, 0))
로 바꿔줌'''
Film                                 Genre      Rotten Tomatoes %  Worldwide Gross  Year
(500) Days of Summer                 Comedy     87                 60.72            2009
이렇게 나옴(a-z)
하지만 이렇게 하면 index가 3인경우에는 작동 안함 그 columm은 string으로 읽힘
20보다 110이 먼저나옴 따라서 인덱스가 3이면 float 사용 그러려먼 gross를 parameter로 
사용하는 새로운 함수 만듬(get_money)
def get_money(gross):
  return float(gross[3])
  요렇게
그리고 
def sort_movie_data(data, index):
    """Sort movie data based on the column data"""
    header = data[0]
    sorted_movies = data[1:]
    if index == 3:
      sorted_movies.sort(key=get_money) #true면 get money에서 설정한대로 정렬함
    else:
      sorted_movies.sort(key=operator.itemgetter(index))
    sorted_movies.insert(0, header)
    return sorted_movies
    얘를 이렇게 수정함 이거는 index가 3일때 사용
    위에랑 똑같은 값이 나옴

Lab 3 - Ascending or Descending Order

import csv, operator

movie_csv = "student_folder/.labs/movie_data.csv"

def fetch_movie_data(movie_csv):
    """Return movie data from a CSV file"""
    with open(movie_csv, "r") as movie_file:
        reader = csv.reader(movie_file)
        movie_info = []
        for row in reader:
          movie_info.append(row)
        return movie_info

def print_movie_data(data):
    """Print the movie data in easy to read columns"""
    for title, genre, rotten, gross, year in data:
      print("{:36} {:10} {:18} {:16} {}".format(title, genre, rotten, gross, year))
      
def sort_movie_data(data, index): #여기에다 descending만 넣어주면 됨
    """Sort movie data based on the column data"""
    header = data[0]
    sorted_movies = data[1:]
    if index == 3:
      sorted_movies.sort(key=get_money)
    else:
      sorted_movies.sort(key=operator.itemgetter(index))
    sorted_movies.insert(0, header)
    return sorted_movies
      
movie_data = fetch_movie_data(movie_csv) 
print_movie_data(sort_movie_data(movie_data, 0))


def sort_movie_data(data, index, descending):
    """Sort movie data based on the column data"""
    header = data[0]
    sorted_movies = data[1:]
    if index == 3:
      sorted_movies.sort(key=get_money)
    else:
      sorted_movies.sort(key=operator.itemgetter(index))
    if descending: #des가 ture인지 확인
        pass #이거를 sorted_movies.reverse()이렇게 바꾸면 descend으로 나옴 파이썬은 항상 asce
    sorted_movies.insert(0, header)
    return sorted_movies
movie_data = fetch_movie_data(movie_csv) 
print_movie_data(sort_movie_data(movie_data, 0)) 
'''print_movie_data(sort_movie_data(movie_data, 0, True))이렇게 바꿔줌'''
Film                                 Genre      Rotten Tomatoes %  Worldwide Gross  Year
Zack and Miri Make a Porno           Romance    64                 41.94            2008
이렇게 z-a로 나옴

def my_function(x=5):
    print(x)

print(my_function())
print(my_function(7))
5.7 나옴 왜? parameter x는 옵션임 따라서 x==5 but, 7을 매개로 하면 7이 나옴

Lab 4 - Command Line Interface
def user_interface(): #no parameter
    """Ask user how they want to sort the movie data"""
    while True:
        pass
interface 함수의 flow
1. 어떤 기준으로 sort할지 묻는다.
2. 사용자가 6을 입력하면 종료한다
3. 입력한 데이터 확인 유효하지 않으면 print message하고 다시 시작 프로그램이 중단되거나 충돌 되지 않아야함
4. 사용자에게 오름차인지 내림차인지 묻는다.
5. 입력한 데이터 확인 유효하지 않으면 print message하고 다시 시작 프로그램이 중단되거나 충돌 되지 않아야함
6. print sorted data
7. 사용자가 종료할떄 까지 반복
이런 flow를 같기 위해서는 몇가지 조건 필요 

def user_interface(): #위에서 한 movie_data = fetch_movie_data(movie_csv)(402행) 
#print_movie_data(sort_movie_data(movie_data, 0))(403행) 를 제거하고 user interface를 사용
    """Ask user how they want to sort the movie data"""
    while True:
        column = ask_column() '''칼럼은 데이터를 정렬할 sort 파일의 칼럼임
        ask 칼럼은 칼럼을 표시하고 사용자에게 1~6을 입력하도록 요청함'''
        if column == "6":
            break
        if sanitize_column(column): #sanitize_column 숫자가 1~6이면 true아니면 false를 반환함
            order = ask_order() #애스크 오더는 사용자에게 1또는 2를 입력하도록 요청 
            if sanitize_order(order): #새니 오더는 사용자가 1or2를 입혁하면 true 아니면 false반환
                movie_data = fetch_movie_data(movie_csv) 
                print_movie_data(sort_movie_data(movie_data, int(column) - 1, int(order) == 2))
                '''칼럼과 오더는 string으로 저장되는 user input. 사용하려면 int로 캐스트 해야함
                킬럼은 1~6까지 숫자 6은 종료함 csv 파일은 0~4칼럼있으니 csv 파일과 일치위해 -1한다
                order는 int이지만 parameter는 boolean이어야함 boolean을 parameter로 사용하면 참 혹은 거짓이
                 print_movie_data로 던달'''
            else:
                print("Enter a number 1 or 2.\n")
        else:
            print("Enter a number 1 to 6.\n")
조건에 대한 골격임

Lab 5 - Adding Helper Functions

def ask_column(): 
    """Ask the user by which criteria they want to sort the data"""
    pass
      
def sanitize_column(column):
    """Return True if the user entered a valid number, else return False"""
    pass
    
def ask_order():
    """Ask the user how they want the data sorted: ascending or descending"""
    pass

def sanitize_order(order):
    """Return True if the user entered a valid number, else return False"""
    pass

def user_interface(): #위에다 새로운 함수를 추가했음
    """Ask user how they want to sort the movie data"""
    while True:
        column = ask_column()
        if column == "6":
            break
        if sanitize_column(column):
            order = ask_order()
            if sanitize_order(order):
                movie_data = fetch_movie_data(movie_csv) 
                print_movie_data(sort_movie_data(movie_data, int(column) - 1, int(order) == 2))
            else:
                print("Enter a number 1 or 2.\n")
        else:
            print("Enter a number 1 to 6.\n")
위에 함수는 아무런 기능이 없어서 무한루프 됨 뭔가를 더 적어야함
위에 코드를 실행하면 interface가 실행됨 여기는 true:loop가 있음 
break는 var가 6일때만 실행됨 ask_columm은 칼럼에 대한 값을 생성함 지금은 6과 같지 않은 pass를 리턴함
따라서 무한 루프임

def ask_column(): #숫자 입력 요청
    """Ask the user by which criteria they want to sort the data"""
    column = input("""How do you want to sort the movie data? Enter '6' to exit the program.
        1) By Film Title #읽기 위해서는 각각의 번호가 각각의 선에 있어야함 여기서는 '''로 했음
        2) By Genre
        3) By Rotten Tomatoes Score
        4) By Worldwide Gross
        5) By Year
        6) Quit\n""")
    return column

def sanitize_column(column): #사용자의 값이 올바르면 true print 아니면 false
    """Return True if the user entered a valid number, else return False"""
    try:
        int(column)
        return int(column) >= 1 and int(column) <= 5
    except ValueError:
        return False
'''사용자의 값이 올바르기 위한 조건 1. must be a number 2. input에서 오는 int는 string으로 캠쳐됨
따라서 6은 int로 가능하지만 cat은 안됨 칼럼을 int로 인식 못하면 ValueError 
따라서 try&except사용한다. 또한 에러나니까 false출력 또한 true는 1=<x<6이어야 함'''

def ask_order(): #ask_columm과 거의 유사 하지만 1,2를 입력하도록 요청
    """Ask the user how they want the data sorted: ascending or descending"""
    order = input("""How do you want the movie data ordered?
            1) Ascending Order
            2) Descending Order\n""")
    return order

def sanitize_order(order): #sanitize_column 유사하지만 ask_order가 1인지2인지만 확인
    """Return True if the user entered a valid number, else return False"""
    try:
        int(order)
        return int(order) >= 1 and int(order) <= 2
    except ValueError:
        return False


전체코드

import csv, operator

movie_csv = "student_folder/.labs/movie_data.csv"

def fetch_movie_data(movie_csv):
    """Return movie data from a CSV file"""
    with open(movie_csv, "r") as movie_file:
        reader = csv.reader(movie_file)
        movie_info = []
        for row in reader:
          movie_info.append(row)
        return movie_info

def get_money(gross):
    return float(gross[3])

def print_movie_data(data):
    """Print the movie data in easy to read columns"""
    for title, genre, rotten, gross, year in data:
        print("{:36} {:10} {:18} ${:16} {}".format(title, genre, rotten, gross, year))
    
def sort_movie_data(data, index, descending):
    """Sort movie data based on the column data"""
    header = data[0]
    sorted_movies = data[1:]
    if index == 3:
        sorted_movies.sort(key=get_money)
    else:
        sorted_movies.sort(key=operator.itemgetter(index))
    if descending:
        sorted_movies.reverse()
    sorted_movies.insert(0, header)
    return sorted_movies

def ask_column():
    """Ask the user by which criteria they want to sort the data"""
    column = input("""How do you want to sort the movie data? Enter '6' to exit the program.
        1) By Film Title
        2) By Genre
        3) By Rotten Tomatoes Score
        4) By Worldwide Gross
        5) By Year
        6) Quit\n""")
    return column

def sanitize_column(column):
    """Return True if the user entered a valid number, else return False"""
    try:
        int(column)
        return int(column) >= 1 and int(column) <= 5
    except ValueError:
        return False

def ask_order():
    """Ask the user how they want the data sorted: ascending or descending"""
    order = input("""How do you want the movie data ordered?
          1) Ascending Order
          2) Descending Order\n""")
    return order

def sanitize_order(order):
    """Return True if the user entered a valid number, else return False"""
    try:
        int(order)
        return int(order) >= 1 and int(order) <= 2
    except ValueError:
        return False

def user_interface():
    """Ask user how they want to sort the movie data"""
    while True:
        column = ask_column()
        if column == "6":
            break
        if sanitize_column(column):
            order = ask_order()
            if sanitize_order(order):
                movie_data = fetch_movie_data(movie_csv) 
                print_movie_data(sort_movie_data(movie_data, int(column) - 1, int(order) == 2))
            else:
                print("Enter a number 1 or 2.\n")
        else:
            print("Enter a number 1 to 6.\n")

user_interface()
이게 전체 코드 실행하면 어떻게 sort할거냐 묻고 내림차 오름차 묻는다.
선택하면 최종 정리본

연습
1. 
문제 : Write a function called avg that takes two parameters. 
Return the average of these two parameters. If the parameters are not numbers, return the string, "Please use two numbers as parameters."

Expected Output
If the function call is avg(10,25), then the function would return 17.5
If the function call is avg(10, "cat"), then the function would return Please use two numbers as parameters

코드: 
def avg(n1,n2):
  try : #try/excpet는 거의 세트
    return(n1+n2)/2
  except TypeError :
    return("Please use two numbers as parameters")
해야할일 2개. parameter가 함께 add되고 devide되야 함

2. 
문제 :Write a function called "odds_or_evens" that takes a boolean and a list of integers as parameters. 
If the boolean parameter is True, return a list of only even numbers. 
If the boolean parameter isFalse, return a list of only odd numbers.

Expected Output
If the function call is odds_or_evens(True, [13, 22, 8, 31]), the the function would return [22, 8]
If the function call is odds_or_evens(False, [13, 22, 8, 31]), the the function would return [13, 31]

code:
def odds_or_evens(my_bool, nums):
    """Returns all of the odd or
    even numbers from a list"""
    return_list = [] #로컬 펑션 프린트는 이거 출력
    for num in nums:
      if my_bool: #boolena parameter가 참이면 목록 반복
          if num % 2 == 0:
              return_list.append(num)
      else:
          if num % 2 != 0:
              return_list.append(num)
                
    return return_list


3.
prob: 
Write a function called "search_list" that takes a list and a search term as parameters. 
If the search term is located in the list, return the index of the matching element. 
The function should work even if there is a difference in capitalization. 
If the search term is not in the list, return -1.
검색어가 목록에 있으면 일치하는 요소의 인덱스를 반환

Expected Output
If the function call is search_list(["dog", "fish", "cat"], "Cat"), the the function would return 2
If the function call is search_list(["water", "Toy", "house"], "toy"), then the function would return 1
If the function call is search_list(["box", "car", "hat"], "mouse"), the the function would return -1

코드
def search_list(lst, term):
    """Search for item in a list
    Return the index if found
    Return -1 if not found"""
    for item in lst: #list를 반복해서 맞는 단어를 찾는다.
        if item.lower() == term.lower(): #두 문자열을 갖은 대소문자에 넣는다. 긍까 대소문자에 달라지지 않도록
            return lst.index(item)
    return -1

4.
Problem
Write a function called "best_team" that takes a csv file as a parameter. 
Read the comma-delimited CSV file specified by the variable "mlb_data". 
The CSV file has a list of all of the MLB teams and their performance from the 2019 season. 
The function should return the team name for the team with the most wins. 
Important, the CSV file has a header of "Tm,Lg,G,W,L", which stands for team name, league, games played, wins, and losses. 
Below are the file name and file path variables you will need for this exercise.

Expected Output
The function call should look like this,
 best_team(file), and the function should return "HOU". 
 However, your function will be tested with other CSV files in which different teams will have the highest win total.

코드
import csv

mlb_data = "student_folder/.exercises/mlb_data.csv"

def best_team(file):
    """Read a CSV of baseball data.
    Return the team name with the most wins"""
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader) #스킵해줘야함
        most_wins = 0
        best_team = ""
        for row in reader:
            if int(row[3]) > most_wins:
                most_wins = int(row[3])
                best_team = row[0]
        return best_team
글로벌 var필요함 mlb_data. 베스트 팀 선언하고 파일 열기 그리고 csv.reader사용해서 시작
2개의 var필요 1. track the most win 2. most win team
0으로 최다승 변수 걸고 팀 이름은 공백으로 둔다. 그리고 반복 row elemet는 3여야 함 
모든 data는 csv에 string으로 저장됨 type cast필수

5.
Write a function called "is_palindrome" that takes a string as a parameter. 
The function will return True if the string is a palindrome (is the same forward and backward). 
The function will return False if the string is not a palindrome.

Expected Output
If the function call is is_palindrome("level"), the the function would return True
If the function call is is_palindrome("house"), the the function would return False

코드
def is_palindrome(string):
    reversed_string= "" #확인위해 reverse시키셈
    position = len(string) - 1 #원래 문자와 역 문자를 비교
    while position >= 0: 
        reversed_string += string[position]
        position -= 1 #위치변수에서 하나빼줘야함
    if string == reversed_string: #비교
        return True
    else:
        return False
빈 string을 만들면 string reverse가능. string은 0부터 카운트
따라서 string의 마지막은 -1이어야함