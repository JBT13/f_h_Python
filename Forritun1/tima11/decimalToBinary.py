def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"

    list = []
    while decimal > 0: 
        remainder = decimal % 2
        list.append(remainder)
        decimal = decimal // 2

    list.reverse()
    binary = "".join(str(bit) for bit in list )
    return binary