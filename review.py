from configparser import Interpolation
from functools import total_ordering
import string


cs1400

The Format Method
파이썬에서 사용하는 새로운 Interpolation
중괄호로 비워주고 마지막에 변수 넣으면 됨
var1 = "today"
var2 = "luckiest"
print("Yet {} I consider myself the {} man on the face of this earth.".format(var1, var2))
# Yet today I consider myself the luckiest man on the face of this earth.

일반적으로는 순서대로 나옴 왼-오 하지만 인덱스로 순서 바꿀 수 있음
var1 = "today"  # 인덱스 0
var2 = "luckiest"  # 인덱스 1
print("Yet {1} I consider myself the {0} man on the face of this earth.".format(
    var1, var2))

var1 = "today"
var2 = "luckiest"
print("Yet {1} I consider myself the {0} man on the face of this earth.".format(
    var2, var1))
이렇게 바꾸면 반대로 나옴 왜냐면 var2가 인덱스 0이됨

F-string(fast...)
var1 = "Up"
var2 = "away"
my_string = f"{var1}, up and {var2}."
print(my_string)
새롭게 변수를 만드는 것(if사용할때는 불편함)

Multi-line F-Strings
name = "Calvin"
age = 6
occupation = "student"
sentence = f"My name is {name}. " \
           f"I am {age} years old. " \
           f"I am a {occupation}."
print(sentence)
이렇게 할 수 있음
name = "Calvin"
age = 6
occupation = "student"
sentence = f"""My name is {name}.
I am {age} years old.
I am a {occupation}."""
print(sentence)
이것도 가능 하지만 처음거는 같은 줄에 나오고 두번째는 다른 줄로 나옴
같은 줄에 나오게 하려면 \사용해야함 그리고 다중 문자열은 """만 적으면 됨


For loops
for i in range(5):
    print("Loop #" + str(i)) #0부터 시작함 하지만 5는 포함 안함
Loop 0~ Loop 4까지 나옴

for i in range(5):
    print("Loop #" + str(i+1))
1~5나옴

for i in range(3, 0, -1): #숫자를 내려가려면 처음숫자가 반드시 커야하고 세번쨰 숫자를 언급해야함
    print("Loop #" + str(i))
3,2,1 나옴

While loop

for과의 차이 (반복회수를 정하냐? 종료조건을 정하냐?)
예를 들어, 당첨 확률이 1%인 복권을 200장 사서 몇 번 당첨되었는지를 알고 싶을 때는
반복 횟수가 정해져있는 것이므로 for문을 사용하는 것이 좋고,
당첨이 될 때까지 복권을 몇 장 샀는지를 알고 싶을 때는
종료 조건이 정해져있는 것이므로 while문을 이용하는 것이 유리합니다.
While Loop	For Loop
Runs as long as a condition is true	       Runs a predetermined amount of times
You must declare a counting variable	    Counting variable is automatically declared
You must increment the counting variable	  The counting variable is already incremented
사실이라면 계속 반복,                            정해진 만큼만 작동
count변수 선언                                  count변수 자동선언
변수를 증가시켜줘야함                            역시 이미 되어있음

count = 0 # counting variable
while count < 5:
    print("Hello")
    count = count + 1 #increment 이거 없으면 무한루프 됨
얘는 반복해서 출력 정확한 횟수

while True:
    print("Hell")
    rand_num = random.randint(1,101)
    if rand_num >75:
        break
범위 안에서 출력

비교
count(78), rand_num(85)는 test되는 변수임
count < 5(79), if rand_num >75(86)은 end조건
count = count + 1(81), random.randint(1,101)(86)은 변하는 변수
Infinite Loops #break 쓰셈

total = 0
while True:
    total += 1 
    if total > 100: #100이랑 숫서 바뀌니 안됨
        break
