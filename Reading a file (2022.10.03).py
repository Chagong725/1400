Reading a file (2022.10.03)

"r"사용. 새로운 파일은 안만듬

read_file = open("student_folder/text/read_practice.txt", "r")
print(read_file)
read_file.close()
이런 식으로 하면 파일을 읽는 것이 아니라, 
<_io.TextIOWrapper name='student_folder/text/read_practice.txt' mode='r' encoding='UTF-8'>
이렇게 name, mode, and encoding 이 나옴

내용을 알고 싶으면, 
read_file = open("student_folder/text/read_practice.txt", "r")
print(read_file.readlines())
read_file.close()
'''readlines 사용해야함 '''

File Iteration - For Loop
단순 readlines는 \n 로 모든 줄이 합쳐나옴 하지만 루프 쓰면 개별 줄에 나옴
with open("student_folder/text/read_practice.txt", "r") as read_file:
    for line in read_file.readlines():
      print(line)

print(line.upper()) = 전부 대문자로 나옴

with open("student_folder/text/read_practice.txt", "r") as read_file:
    for line in read_file.readlines():
      print(line, end="")
이렇게 하면 줄간격이 좁아짐
Python was created by Guido van Rossum.

It was named for the TV show Monty Python's Flying Circus.
            이거에서
Python was created by Guido van Rossum.
It was named for the TV show Monty Python's Flying Circus.
이렇게

print(line, end="!") 이렇게 바꾸면 모든 줄에 !생김


Readline vs. Readlines
readlines는 모든 text가 list로 나오지만, readline은 한줄만 나옴

with open("student_folder/text/read_practice.txt", "r") as read_file:
    print(read_file.readline(), end="")
    print(read_file.readline(), end="")
    이렇게 쓰면 두줄 나옴

with open("student_folder/text/read_practice.txt", "r") as read_file:
    line = read_file.readline()
    while line != "":
        print(line)
        line = read_file.readline()

이거는 while써서 루프 시키는 방법
line = read_file.readline()=루프 Variable
while line != "": =stop condition(""필수)
마지마 line = read_file.readline() = increment 이거 없으면 무한 으로 감(첫줄만)


Seek Method
with open("student_folder/text/read_practice.txt", "r") as read_file:
    read_file.seek(30)
    print(read_file.readline())
    read_file.seek(0)
    print(read_file.readline())
요러게 위치 찾는다.

멀티플로 seek사용하면 두번 이상 읽을 수도 있다.
with open("student_folder/text/read_practice.txt", "r") as read_file:
    print("First Time")
    for line in read_file.readlines():
        print(line, end="")
    read_file.seek(0)
    print("\n\nSecond Time")
    for line in read_file.readlines():
        print(line, end="")

 First Time
Python was created by Guido van Rossum.
It was named for the TV show Monty Python's Flying Circus.
Version 1 was released in January 1994.
Python 2.0 was released in October 2000.
The third version came out in December 2008.

Second Time
Python was created by Guido van Rossum.
It was named for the TV show Monty Python's Flying Circus.
Version 1 was released in January 1994.
Python 2.0 was released in October 2000.
The third version came out in December 2008.
요렇게 나옴

Read from One File and Write to Another

with open("student_folder/text/read_practice.txt", "r") as source, open("student_folder/text/destination.txt", "w") as dest:
    for line in source.readlines():
        dest.write(line)
요렇게 하면은 하나는 읽기로 하는 쓰기로 엸 있다,

write vS writeline
writeline은 single string or list sring 사용 가능 but, write는 signle string만 가능

write(line.upper()) 다 대문자로 나옴

10.05
seek으로 다시읽는 방법도 있지만 다른 방법도 있음
text = []

with open("student_folder/.labs/files-lab1.txt", "r") as input_file:
    text = input_file.readlines()

print(text[0])
이렇게 하면 읽어줌 0은 0번째 줄에 있는 걸 읽어줌  1은 1번쨰(index기준)
print(text[0].upper())
이거 추가하면 두번 읽어주고 두번쨰는 대문자로 나옴

만약 print(text[0])을 print(text) 이걸로 바꾸면?!
['Having had some time at my disposal when in London, I had visited the British Museum, and made search among the books and maps in the library regarding Transylvania; it had struck me that some foreknowledge o\n', 'f the country could hardly fail to have some importance in dealing with a nobleman of that country. I find that the district he named is in the extreme east of the country, just on the borders of three states, Transylvania, Moldavia and Bukovina, in the midst of the Carpathian mountains; one of the wildest and least known portions of Europe. I was not able to light on any map or work giving the exact locality of the Castle Dracula, as there are no maps of this country as yet to compare with our own Ordnance Survey maps; but I found that Bistritz, the post town named by Count Dracula, is a fairly well-known place. I shall enter here some of my notes, as they may refresh my memory when I talk over my travels with Mina.']
이렇게 나옴
모든 게 다 나옴 \n이런 것도 나옴 하지만[0]은 스페셜 기호는 안나옴


comma delimited
import csv

with open("student_folder/.labs/files-lab2.csv", "r") as input_file: #파일 열기
    reader = csv.reader(input_file)
    '''nested loop'''
    for row in reader:
        total = 0
        for num in row:
            total += int(num) # 토탈 변수 선언해서 각 숫자를 row에 넣기
        print("The total value is: {}".format(total))#inner loop로 내부 채우기 

The total value is: 10
The total value is: 151
The total value is: 63
The total value is: 127
이게 결과 원본 파일은

1,4,5
18,34,99
0,12,51
37,29,61
이캐 생겼음

reader = csv.reader(input_file, delimiter="!") 이것도 delimit방법임


특정 문구 기입시 loop가 멈추는 함수(이거는 stop이 이름일때 멈춤)

import csv

with open("student_folder/csv/superheroes.csv", "w") as output_file:
    writer = csv.writer(output_file, lineterminator="\n") # lineterminator to \n 왜냐면 avoid the mixed line endings warning.
    writer.writerow(["Superhero", "Power"])
    print("Enter `stop` to quit the program") # 160 colum까지 유저한테 타입하라고 만드는 함수
    name = input("Enter the superhero's name: ")
    power = input("Enter their superpower: ")
    while True: # for loop는 정해진 시간만 되기때문에 while더 좋음 왜냐면 이거는 무한 루프이기 때문
        writer.writerow([name, power]) #파일 line을 적는 것 계속 새로운 이름과 초능력을 적음. 
        name = input("Enter the superhero's name: ")
        if name == "stop":
            break #break 조건이 164열임
        power = input("Enter their superpower: ")

시저 암호화
문자, 숫자, !, ?, . 사용가능하다. key는(0~25)

with open("student_folder/.labs/source.txt", "r") as source, open("student_folder/text/encrypted.txt", "w") as destination:
    key = 13 # key setting
    mode = "encrypt" # encrypt or decrypt 2개있음
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.-;" #심볼이 대문자인 이유는 constant이기 때문
    new_text = ""

    line = source.readline() #파일 첫줄 읽기 시작함
    while line != "":
        for char in line:
            if char in SYMBOLS:
              char_index = SYMBOLS.find(char)
              
              if mode == "encrypt": # symbol만 암호화 한다. 텍스트르 암호화하면 키값을 index에 추가한다(뭐소리..)
                  new_index = char_index + key
              elif mode == "decrypt":
                  new_index = char_index - key
'''char index가 0보다 작거나 심볼 length보다 클 수 있다. 이러면 오류남
따라서 char i가 음수면 심볼 길이에 추가해주고 심볼도가 크면 심볼길이를 빼야함'''
              if new_index >= len(SYMBOLS):
                  new_index = new_index - len(SYMBOLS)
              elif new_index < 0:
                  new_index = new_index + len(SYMBOLS)
              new_text += SYMBOLS[new_index]

        destination.write(new_text) # 문자 변화했으니 new_text에 문자 추가
        line = source.readline() #source의 다음줄 읽는다

요상한 언어로 암호화됨

이제 해독(decrypting)
with open("student_folder/text/encrypted.txt", "r") as source, open("student_folder/text/decrypted.txt", "w") as destination:
        mode = "decrypt"

파일 읽기로 글자 바꾸기
Bruma--- Myanmar로 바꿀거임

with open("student_folder/.labs/myanmar.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        if "Burma" in line:
            print(line.replace("Burma", "Myanmar"), end="") #end=""옵션 그저 텍스트 사이 빈줄 없도록 한다
        else:
            print(line, end="")#end =""는 옵션

파일 읽고 number of 캐릭더 & number of line 리턴하기
import sys

test_file = sys.argv[1] # 얘는 그냥 시스템이 준 값임

line_count = 0 #변수 두개 하나는 캐릭터 하나는 라인
char_count = 0

with open(test_file, "r") as input_file:
    line = input_file.readline() #한줄씩 읽기 시작함
    while line != "": #text파일의 라인이 ""와 같은지 확인
        line_count += 1
        char_count += len(line)
        line = input_file.readline()

print("{} lines".format(line_count)) #두 변수를 텍스트와 함께 인쇄
print("{} characters".format(char_count))

4 lines
231 characters
이캐 나옴 원본이 어캐 생겼는지는 모름..

콤마로 디리밋된 파일을 4개 columm으로 읽고 각 칼럼의 평균을 구하라
import sys, csv

test_file = sys.argv[1]

total1 = 0
total2 = 0
total3 = 0
total4 = 0
row_count = 0 #칼럼 4개니까 변수 4개 걸고, row가 얼마나 있는지 추적하기 위해 row도 변수 선언

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file)
    for num1, num2, num3, num4 in reader: #"pull apart"method 사용 각각 분리한다(unpack method)
        row_count += 1 
        total1 += int(num1) # csv에서 읽는 모든 파일은 string으로 나옴! 그래서 int(or float)로 바꿈
        total2 += int(num2) # num은 for에서 선언한 변수고 total은 위에서 한 변수
        total3 += int(num3)
        total4 += int(num4)

print("{} {} {} {}".format(total1/row_count, total2/row_count, total3/row_count, total4/row_count))
# 다 끝나면 total넘버를 row넘버로 나눈 값을 내야함

10.0 8.0 6.0 20.0 아웃풋

읽고 인쇄내용 역순으로 출력
import sys

test_file = sys.argv[1]

with open(test_file, "r") as input_file:
    lines = input_file.readlines() #모든 라인을 한번에 읽는게 더 유용
    lines.reverse() #리버스
    for line in lines: 
        print(line)

tab 디리밋된 거 읽고 제일 나이많은 사람 출력

Name	Age	Career
Peter	38	Doctor
Paul	41	Lawyer
Mary	32	Systems Engineer 
요것이 csv파일

import sys, csv

test_file = sys.argv[1]
oldest_age = 0 #두개 이상의 변수가 필요 하나는 나이를 track 나머지는 늙은사람 이름은 track
oldest_name = "" # 나이는 0으로 하고 이름은 비워둔다

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file, delimiter="\t") #탭으로 디리밋 됐으니 꼭 인지 시켜주기
    next(reader) # 맨 위 row는 쓸모없음 그래서 스킵해야함
    for name, age, career in reader: # 아까했던 unpack method사용
        if int(age) > oldest_age: #역시 int로 바꿔주고 a가 oa보다 크면 oa가 a도 업데이트 된다
            oldest_age = int(age)
            oldest_name = name #여기도 세팅해줌
            
print("The oldest person is {}.".format(oldest_name)) # 프린트
The oldest person is Paul. 이렇게 출력됨

콤마 디리밋트 파일이고 남반구의 도시를 인쇄한다. (위도가 음수면 남반구임)

City	Country	Latitude	Longitude
Beijing	China	   39	      116
Perth	Australia -57	      115
Port    Moresby	Papua New Guinea	-25	147
Tokyo	Japan	35	139
원본

import sys, csv

test_file = sys.argv[1]
cities = []

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file)
    next(reader)
    for city, country, latitude, longitude in reader:
        if int(latitude) < 0:
            cities.append(city) #위 조건이 충족되면 시티쓰에다가 추가하는 작업임
            
print("The following cities are in the Southern Hemisphere: ", end="") #두개가 출력되야하는게 이것이 첫번째 string임
for city in cities: #interlate해줌. 도시를 인쇄하려면 도시 인쇄후 쉼표나 공백을 넣어주거나(뒤에 도시가 또 나와야하니까) 마침표를 넣어줘야함
    if city == cities[-1]: #얘가 마침표 근데 -1은 마지막 인덱스라는 표시임
        print(city + ".")
    else:
        print(city, end=", ")
The following cities are in the Southern Hemisphere: Perth, Port Moresby.      출력값


원본 파일 :
I've got a lovely bunch of coconuts
There they are, all standing in a row

쉬운 파일 읽기
with open('coconuts.txt', 'r') as file_object:
    contents = file_object.read() # read method 쓰면 다 읽어줌

"I've got a lovely bunch of coconuts\nThere they are, all standing in a row\n" 이게 결과

한줄씩 읽기
with open('coconuts.txt', 'r') as file_object:
    lines = file_object.readlines()
["I've got a lovely bunch of coconuts\n", 'There they are, all standing in a row\n'] # 리스트 형식으로 나옴, 줄마다 구분도 됨
lines = []
with open('coconuts.txt', 'r') as file_object:
    for line in file_object:
        lines.append(line)
이것도 똑같이 나옴

lines = []
with open('coconuts.txt', 'r') as file_object:
    for line in file_object:
        lines.append(line.strip()) #strip을 사용해서 앞뒤 공백을 지워줨
["I've got a lovely bunch of coconuts", 'There they are, all standing in a row'] # 이렇게 나옴 \n없어짐

with open('coconuts.txt', 'r') as file_object:
    lines = [line.strip() for line in file_object] 
이것도 같음


2. Dividing strings
split() 사용
with open('coconuts.txt', 'r') as file_object:
    words = file_object.read().split() 요렇게
["I've", 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts', 'There', 'they', 'are,', 'all', 'standing', 'in', 'a', 'row']
이렇게 나옴 전부다 split됨

Dividing on specific strings

import os

with open('coconuts.txt', 'r') as file_object:
    lines = file_object.read().strip().split(os.linesep) #strip()은 trailing space제거(후행공백) 안하면 뒤에 공백들어감

["I've got a lovely bunch of coconuts", 'There they are, all standing in a row', ''] 안하면 이렇게 나옴

,로 delimit되면 콤마로 나눠지니까 ㅗㅁ마가 매우 많음 그래서 split 써서 구분
새로운 csv파일 :
8, 11, 28, 19
21, 28, 29, 27
3, 19, 12, 9
30, 30, 4, 4
14, 10, 2, 10
16, 12, 26, 22
15, 26, 11, 11
20, 7, 8, 28
3, 12, 5, 30
17, 6, 23, 1

with open('values.csv', 'r') as file_object:
    rows = [row.split(',') for row in file_object] 이거하면 
[['8', ' 11', ' 28', ' 19\n'], ['21', ' 28', ' 29', ' 27\n'], ['3', ' 19', ' 12', ' 9\n'], ['30', ' 30', ' 4', ' 4\n'], ['14', ' 10', ' 2', ' 10\n'], ['16', ' 12', ' 26', ' 22\n'], ['15', ' 26', ' 11', ' 11\n'], ['20', ' 7', ' 8', ' 28\n'], ['3', ' 12', ' 5', ' 30\n'], ['17', ' 6', ' 23', ' 1\n']]
요렇게 나옴
with open('values.csv', 'r') as file_object:
    rows = [[int(value.strip()) for value in row.split(',')] for row in file_object] 이 방법 쓰면 깨끗해짐
[[8, 11, 28, 19], [21, 28, 29, 27], [3, 19, 12, 9], [30, 30, 4, 4], [14, 10, 2, 10], [16, 12, 26, 22], [15, 26, 11, 11], [20, 7, 8, 28], [3, 12, 5, 30], [17, 6, 23, 1]]
요렇게 나옴

summary:
Means of reading	         Description
file_object.read()              Read the entire contents of a file as a string

file_object.readlines()       Read the entire contents of a file as a list of strings, one for each line
 
file_object as an iterable      Access each line of the file in sequence


문제: 세미콜론으로(;) deli된 친구이다. 공백을 삭제하고 float값으로 변환하라
with open('contents.txt', 'r') as contents:
    values = []
    for value_str in contents.read().split(';'):  #애는 ;로 분활 됐으니 split(;)쓰면 됨
        values.append(float(value_str.strip()))

