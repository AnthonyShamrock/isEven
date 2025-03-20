def isEven(input):
    # Guard Clause: check if digits
    if not input.isdigit():
        print("Must be digits only")
        return __init()
    
    isEvenNumber = [True, False, True, False, True, False, True, False, True, False, True, False] # You get the point...
    return isEvenNumber[int(input)]

def __init():
    print("Number is Even" if isEven(input("Enter Number to Check if Even Or Odd:\n").strip()) == True else "Number is Odd")
    return __init()
__init()