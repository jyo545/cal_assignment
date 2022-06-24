
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

def division(n1,n2):
    if type(n1) == int and type(n2) == int:
        if n2==0:
            return "Second Number Cannot be Zero"
        result = n1 / n2
        return round(result ,2)
    else:
        return "Invalid Input"
   
def multiplication(n1,n2):
    if n1 and n2:
        if type(n1) == int and type(n2) == int:
            if n2 == 0:
                return "Second Number Cannot be Zero"
            result = n1 * n2
            return round(result, 2)
        else:
            return "Invalid Input"
    else:
        return "Inputs Required..cannot be blank...!"


#for run test script run cammand in activated env : python -m pytest
