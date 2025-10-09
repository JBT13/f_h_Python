def parse(s):
    return [int(x) for x in s.split()]

def min(nums):
    m = 0
    for n in nums:
        if n < m:
            m = n
    return m

def main():
    data = parse(input())
    print(min(data))

main()

list = [1,2,3,4,5]
sq_list = []
for i in list:
    last = list[-1]
    each = i * last
    sq_list.append(each)

print(sq_list)
print(list)




def sum_digits(digits):
    suma = 0
    for i in digits:
            if i.isdigit():
                i = int(i)
                suma += i
    return suma

a = input().split(" ")
digit_sum = sum_digits(a)
print(digit_sum)


def parse_int(s):
    return [int(x) for x in s.split()]

def min_(nums):
    m = nums[-1]
    for n in nums:
        if n < m:
            m = n
    return m

def main():
    data = parse_int(input())
    print(min_(data))

main()