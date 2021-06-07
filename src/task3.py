def dictComp(stop, step):
    dict_list = {}
    count = 1
    new_count = 0

    array_list = [ array for array in range(1, stop+1) ]
    
    for digit in array_list:
        
        if len(dict_list) == 0:
            dict_list["items-{}".format(count)] = [digit,]
            
        elif len(dict_list.keys()[-1]) < step:
            last_key = dict_list.keys()[-1]
            dict_list[last_key].append([digit])


    print(len(dict_list.keys()[-1]))
    print(dict_list)


stop = int(input("Enter a number as the limit for your array/list: "))
step = int(input("Enter the digit to use as a step"))


dictComp(stop, step)