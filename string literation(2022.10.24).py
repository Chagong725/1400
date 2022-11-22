string literation(2022.10.24)

Iterating Over Strings(문자열 반복) with for loop
인덱스 0부터 시작하는 반복
my_string = "Hello world"
for char in my_string:  # char: presents each character in {my_string}
    print(char)

my_string, "Hello world": string to literate over
char: var
"""H
e
l
l
o

w
o
r
l
d"""
이렇게 나옴

my_string = "\u25A3\u25A8\u25D3\u25CC\u25A2"
for cha in my_string:
    print(cha)
# 이모티콘 나옴 ㅎ

my_string = "hello world"
for cha in my_string:
    print(my_string)
"""hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world"""
헬로 월드 인덱스가 11임


Iteration - While Loop(대부분for씀)

my_string = "Calvin and Hobbes"
length = len(my_string)
i = 0

while i < length:
    print(my_string[i])
    i += 1
# 캘빈클라인 세로로 나옴

my_string = "Calvin and Hobbes"
length = len(my_string)
i = 0

while i < length:
    print(i)
    i += 1
# 캘빈 인덱스만큼 숫자가 나옴 0~16 왜? i=0이라고 선언했으니까

literating over string 에서는 while보다는 for가 더 유용함
length = len(my_string),    같은 length를 변수로 삼지 않아도 됨
i = 0 index string도 필요없음
i += 1 increment도 필요없음
모든건 in이 해결해줌


String Comparison

Comparing with ==
==를 숫자와 bool에 사용하는 것처럼 string에도 가능

string1 = "It's Friday!"
string2 = "It's Friday!"  # 대소문자 구분함
print(string1 == string2)
# True

string1 = "it's Friday!"
string2 = "it\'s Friday!"  # \얘는 상관 없음 true로 나옴
print(string1 == string2)

Comparing with !=

string1 = "It's Friday!"
string2 = "It's Monday."
print(string1 != string2)
# False

Comparing with Is: == 랑 같음

string1 = "It's Friday!"
string2 = "It's Friday!"
print(string1 is string2)  # True

string1 = ""
string2 = ""
print(string1 is string2)  # True 공백도 체크함

Comparing with Is Not: != 랑 같음

string1 = "It's Friday!"
string2 = "It's Monday."
print(string1 is not string2)  # True

string1 = "\""
# string2 = """
print(string1 is not string2)  # EOF에러 남 #은 주석처리 안하기 위해서 씌움(내가 임의로)


string1 = "\""
string2 = '"'
print(string1 is not string2)  # Flase

== vs. Is

is는 개체의 id를 비교하고 == 는 값을 비교함
is: compare with string and other objects
==: compare floats and integers
문자열을 == 로 해도 오류나지 않지만 is를 사용하는 습관을 기르자


User Input(Capitalization)
dog, Dog은 다른 언어임. 파이썬은 모든 user input을 string으로 처리한다.

text = input("Type something and press 'Return': ")  # 얘는 터미널을 사용하는 방법
# text: var to store user input
# input: ask user for input
# 괄호 내부: 터미널에서 유저에게 보일 메세지
# Type something and press 'Return' 이렇게 나옴
print(text)
# 내가 입력한 것이 출력 됨

터미널에서 ctrl + c는 exit임


Comparing Text, Not Capitalization
lower method 사용하면 cap무시하고 비교가능. 모든 텍스트를 소문자로 변환함

# 터미널로 비교할때 대소문자 구별말고 하는 방법
print("This program will check to see if two values are the same.")
string1 = input("Enter a value: ").lower()  # lower을 upper로 바꿔도 됨
string2 = input("Enter another value: ").lower()
if string1 == string2:
    print("They are the same!")
else:
    print("They are not the same.")

# 실행하면 터미널에서 This program~~나오고 입력하라고 함
# 나는 hello넣고 Hello넣음 결과는 same나옴


Alphabetical Order(대소문자 구별. 소문자가 더 먼저)
알파벳 순서로 어떤 것이 먼저 오는지 파악

string1 = "apple"
string2 = "cat"
if string1 < string2:
    print("{} comes before {}".format(string1, string2))
elif string1 is string2:
    print("{} is the same as {}".format(string1, string2))
else:
    print("{} comes after {}".format(string1, string2))
# apple comes before cat


Lab1
String Methods

.isupper(): string이 upper이면 true lower이면 False
.islower: (): 소문자면 참 대문자면 거짓

얼마나 많은 대문자가 string에 존재하는가. 얼마나 많은 소문자가 string에 존재하는가(특수문자는 무시)
대소문자 갯수 확인
lower_count = 0  # 모든 소문자 count
upper_count = 0  # 모든 대문자 count
my_string = "Roses are Red, Violets are Blue"  # var

for char in my_string:  # literate over the string
    if char.islower():  # 대소문자 check. 순서는 상관없음(여기서는 소문자 먼저)
        lower_count += 1
    elif char.isupper():  # else사용하면 정확한 값을 모름. 왜냐면 특수문자도 카운트함
        upper_count += 1  # 변수 증가시켜줘야함

print("There are {} lowercase characters.".format(lower_count))
print("There are {} uppercase characters.".format(upper_count))
"""There are 21 lowercase characters.
   There are 4 uppercase characters."""

Lab2
Reverse a String
string을 역순으로 출력 print

# original string since string is immutable
my_string = "The brown dog jumps over the lazy fox"
reversed_string = ""  # empty stirng

index = len(my_string) - 1 """ will us While so it needs an index var. normally we need index start 0
 but we will backward so need to start from last charac. length method return length of string.
 but  length of a string is always one greater than the last index. b/c starting from 0 """

while index >= 0:  # For will not work. index가 0이상이면 실행
    reversed_string += my_string[index]  # 제일 마지막 char을 끌고 와서 맨 앞으로 가져감.
    index -= 1  # 무한루프 피하기 위해 decrement한다.

print(reversed_string)
# xof yzal eht revo spmuj god nworb ehT

Lab 3
대소문자 변환 Swapping the Case of Characters. 대문자에서 소문자로 변환 바꾼다. 소문자에서 대문자로

original_string = "THE BROWN DOG JUMPS over the lazy fox"
modified_string = ""

for char in original_string:  # string의 beginning에서 하든 end에서 하든 상관없다. For이 쉬움
    if char.islower():  # 대소문자를 확인 하기 위해서
        # char을 new로 convert하기 위해서 사용. 참이면 modified_string에 대문자로 저장
        modified_string += char.upper()
    else:
        modified_string += char.lower()

print("The original string is: {}".format(original_string))
print("The modified string is: {}".format(modified_string))
"""  The original string is: THE BROWN DOG JUMPS over the lazy fox
  The modified string is: the brown dog jumps OVER THE LAZY FOX"""

Lab4
Count the Vowels, 모음(자음) 갯수 세기

my_string = "The Brown Dog Jumps Over The Lazy Fox"
vowels = "aeiou"
count = 0  # 모든 모음의 갯수

for char in my_string:
    # if char in vowels: vowels은 소문자로 되어있음 char가 대문자면 거짓을 출력함
    # char을 소문자로 convert한다. a있냐e있냐 각각 물어볼 수 있지만 vowel은 string이므로 in을 사용하면 쉽다.
    if char.lower() in vowels:
        count += 1  # char가 vowel을 찾으면 increment시킨다.

if count == 1:
    print("There is 1 vowel in the string")
else:
    print("There are {} vowels in the string".format(count))
"""There are 9 vowels in the string
"""

string에 특정한 글자가 있으면 그것을 바꾸기
my_string = "Hobbes"
vowels = "aeiou"

for vowel in vowels:  # if를 안쓴 이유는 if쓰면 하나의 string으로 인식 for사용하면 하나씩 비교함
    my_string = my_string.replace(vowel, "*")

print(my_string)


execusercustomize
input을 사용해서 단어의 첫번째 글자와 마지막 글자가 무엇인지 출력해라

txt = input()  # txt는 user input을 캡쳐하기 위해서 사용
first = txt[0]  # 변수 index
last = txt[-1]
print("{} is the first character and {} is the last character".format(first, last))

2
입력한 문자의 길이만큼 출력

txt = input()
for i in range(len(txt)):
    print(txt * len(txt))
"""
catcatcat
catcatcat
catcatcat    cat이 세글자이므로 3x3출력"""

"""
treetreetreetree
treetreetreetree
treetreetreetree
treetreetreetree  tree는 4글자 4x4"""

3
original string에 새로운 string을 만듬(u, l, - 사용). char가 대문자면 u 소문자면 l 그것이 아니면 - 출력

txt = input()
second_string = ""
for char in txt:
    if char.islower():
        second_string += "l"
    elif char.isupper():
        second_string += "u"
    else:
        second_string += "-"

print(second_string)


4
string의 반은 첫줄에 나머지는 다음 줄에 출력. string이 odd면 두번째 줄에는 extra char 추가

txt = input()
midpoint = len(txt) // 2  # 중간 값을 구한다  /만 사용하면 float나옴
first_half = txt[:midpoint]
second_half = txt[midpoint:]
print(first_half)
print(second_half)


5
짝수의 input을 넣으면 2개씩 짝지어서 위치를 바꾼다.(홀수는 제외한다)
ex) cars - --- acsr

txt=input()
length=len(txt)
swapped_string=""

for i in range(0, length - 1, 2):  # 한번의 두개의 문자를 교환해야 하므로 increment를 2개씩 증가시켜야함
    swapped_string += txt[i + 1]
    swapped_string += txt[i]

print(swapped_string)
