09.21.2022

final_result =[]
for number in numbers:
    if number % 2 == 0:
      final_result.append("even")
    else:
      final_result.append("odd")
print(final_result)
#(odd,even,odd,even) 요따위로 나옴

''' 만약 보기가 [30,1,20,4]면 10보다 큰 수는 별로나옴'''
for number in numbers:
    if number > 10:
        numbers[numbers.index(number)] = '*'

print(numbers)

#leng이 5보다 작으면 3번 아니면 1번
if len(my_list) < 5:
  print(my_list * 3)
else:
  print(my_list)

#숫자비어있을때 순서대로 숫자 채우기 ㄷㅌ: numbers = [1, 2, 3, 4] 넣으면 123456나옴 맨 뒤 에서 +1하고 range 2개 이므로
  for i in range(2):
  new_number = numbers[-1] + 1
  numbers.append(new_number)
print(numbers)


for row in range(number):
  for column in range(number):
    if row == column:
      data[row][column] = 1
    print(f"{data[row][column]} ", end="")
  print()