import string

print("To quit this program anytime,  enter 'q' as an input: \n")

def nameValidator():
    name = input('Enter your fullname separated with a space separation: ')
    check = False
    array_name = name.split()

    if name == 'q':
        quit()

    # First constraint and Second constraint
    for letter in name:
        if  letter in string.ascii_letters and len(array_name) == 2 :
            check = True
    if check == False:    
        print("Invalid input, enter fullname separated by a single space and must be a character.")       
        nameValidator()  
    
    # Third constraint
    if ( len(array_name[0]) >= 5  and len(array_name[0]) <= 20 ) and ( len(array_name[1]) >= 5  and len(array_name[1]) <= 20 ):
        print("Kudos!! You entered a valid fullaname")
    else:
        print("Invalid fullname, first name and lastname must ge greater than or equal to 5 each and not less than or equal to 20.")
        nameValidator()

nameValidator()