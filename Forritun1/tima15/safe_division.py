def divide_safe(num1_str, num2_str):
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        result = num1 / num2
        is_float = isinstance(result, float)
        if is_float:
            return round(result, 5)
        
    except ValueError:
        return
    
    except ZeroDivisionError:
        return 

a = input()
b = input()

print(divide_safe(a,b))