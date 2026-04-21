def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6:
        return False
    elif len(s) < 2:
        return False
    elif s.isalnum() == False:
        return False
    elif alphafirst(s):
        return False
    elif numberbetween(s):
        return False
    elif zerocheck(s):
        return False
    else:
        return True
    
def alphafirst(s):
    if s[0].isdigit(): 
        return True
    elif s[1].isdigit():
        return True
    else:
        return False
    
def zerocheck(s):
    for i in range(len(s)-1):
        if s[i].isalpha(): 
            if s[i+1] == '0':
                return True
        else:
            return False
        
def numberbetween(s):
    i = 0
    while i < len(s):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return True
            else:
                break
        i += 1
            


main()