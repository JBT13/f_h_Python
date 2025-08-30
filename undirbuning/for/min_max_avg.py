count = int(input("How many numbers do you want to type in?:"))
numbers=[]

for i in range(count):
  num = int(input("Enter in a number: "))
  number = round(num)
  numbers.append(number) 
max_num = max(numbers)
min_num = min(numbers)
avg = sum(numbers) / len(numbers)
print(f"The max number is {max_num}, the min number is {min_num} and the average is {avg} " )
  