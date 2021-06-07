def oddNumbers():
    start = 0
    stop = 0
    try:
        start = int(input("Enter the start range "))
        stop = int(input("ENter the stop range "))
        
    except NameError:
        print("Invalid input, please enter a number")
        
        oddNumbers()

    odd_numbers = [num for num in range(start, stop) if num % 2 != 0]
    print(odd_numbers)


oddNumbers()