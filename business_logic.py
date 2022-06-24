
def addition(n1,n2):
    if n1 and n2:
        if type(n1) in [int ,float ,complex] and type(n2) in [int ,float ,complex]:
            result = n1 + n2
            return result
        else:
            return "Invalid Input"
    else:
        return "Inputs Required..cannot be blank...!"

def subtraction(n1,n2):
    result = n1 - n2
    return result

def division(num1, num2):
    if num1 and num2:
        if type(num1) == int and type(num2) == int:
            if num2 == 0:
                return "Second Number Cannot be Zero"
            result = num1 / num2
            return round(result, 2)
        else:
            return "Invalid Input"
    else:
        return "Inputs Required..cannot be blank...!"

def multiplication(num1, num2):
    if num1 and num2:
        if type(num1) == int and type(num2) == int:
            if num2 == 0:
                print("Second Number Cannot be Zero")
            result = num1 * num2
            return round(result, 2)
        else:
            return "Invalid Input"
    else:
        return "Inputs Required..cannot be blank...!"


#for run test script run cammand in activated env : python -m pytest



