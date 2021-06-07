def dictComp(stop, step):
    dict_list = {}
    count = 0


    array_list = [ array for array in range(1, stop+1) ]
    
    for digit in array_list:
        # Condition runs only on the first iteration when dict_list has no key value pair
        if len(dict_list) == 0:
            count += 1
            dict_list["items-{}".format(count)] = [digit]

        #   Condition when each value as a list is not greater than step 
        elif len(dict_list["items-{}".format(count)]) < step :
            dict_list["items-{}".format(count)].append(digit)
        
        #   Condition for creating new key value pair after the lenth of last pair is equal to step
        else:
            count += 1
            dict_list["items-{}".format(count )] = [digit]

    if len(dict_list["items-{}".format(count)]) < step:
        dict_list.popitem()

    print(dict_list)


try:
    stop = int(input("Enter a number as the stop limit for your array/list: "))
    step = int(input("Enter the digit to use as a step: "))
    print("\n")

    dictComp(stop, step)

except ValueError:
    print("\n")
    print("Invalid input, please enter only a number")
    print("\n")
    stop = int(input("Enter a number as the stop limit for your array/list: "))
    step = int(input("Enter the digit to use as a step: "))
    print("\n")

    dictComp(stop, step)
