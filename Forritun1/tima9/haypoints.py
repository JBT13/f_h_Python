a, b = map(int, input().split())

description = {}

money = []

for _ in range(a):
    job = input()
    name , salary = job.split()
    description[name] = int(salary)

for _ in range(b):
    sentence = input()
    words = sentence.split(sep=".")
    for word in words:
        if word in description:
            money.append(description[word])

print(sum(money))


