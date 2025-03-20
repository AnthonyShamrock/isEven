def isEven(input):
    # Guard Clause: check if digits
    if not input.isdigit():
        print("Must be digits only")
        return __init()
    
    
    lastDigit = input[-1]
    oddNumbers = ["1","3","5","7","9"]
    return not lastDigit in oddNumbers

def __init():
    print("Number is Even" if isEven(input("Enter Number to Check if Even Or Odd:\n").strip()) == True else "Number is Odd")
    return __init()

__init()