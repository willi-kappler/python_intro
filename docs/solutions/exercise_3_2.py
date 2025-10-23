def get_numbers():
    all_numbers = []
    total_sum = 0
    
    while True:
        print(f"Total sum: {total_sum}")
        user_in = input("Enter a number: ")
    
        if user_in == "quit":
            break
    
        number = int(user_in)
        total_sum += number
        all_numbers.append(number)
        
    return all_numbers

numbers = get_numbers()

numbers.sort()
print(f"numbers: {numbers}")
1