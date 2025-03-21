def isEven(input):
    # Guard Clause: check if digits
    if not input.isdigit():
        print("Must be digits only")
        return __init()
    
    return not ".5" in str(float(input)/2)

def __init():
    print("Number is Even" if isEven(input("Enter Number to Check if Even Or Odd:\n").strip()) == True else "Number is Odd")
    return __init()
__init()