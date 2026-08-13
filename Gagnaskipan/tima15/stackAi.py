def polish(text:str,dic:dict):
    stack = []
    for value in text:
        if value == " ":
            continue

        if value.isdigit():
            stack.append(int(value))

        elif value in dic:
            stack.append(dic[value])
                       
        elif value == "+":
            if len(stack) != 2:
                return False

            a = stack.pop()
            b = stack.pop()
            num = a + b
            stack.append(num)

        elif value == "-":
            if len(stack) != 2:
                return False
            
            a = stack.pop()
            b = stack.pop()
            num = b - a
            stack.append(num)

        elif value == "/":
            if len(stack) != 2:
                return False

            a = stack.pop()
            b = stack.pop()
            num = b // a
            stack.append(num)

        elif value == "*":
            if len(stack) != 2:
                return False

            a = stack.pop()
            b = stack.pop()
            num = a * b
            stack.append(num)

    if len(stack) >= 2:
        return False
    
    return stack

dic = {}
text = "a"
text2 = ""
while text != "":
    text = input()
    for i in text:
        if i == "=":
            dic[text[0]] = int(text[4])
            continue
    
        elif i in "+*/-":
            text2 = text
            text = ""
            break

print(polish(text2,dic))
