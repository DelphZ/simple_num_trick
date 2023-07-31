user_input = input("Enter your string (You hould only input number 0 - 9): ")
result_num_list = []
previous_unmemorized_digit = 0
for char in user_input:
    num_of_char = int(char) - int('0')
    last_memorized_digit = -1
    if len(result_num_list) > 0:
        last_memorized_digit = result_num_list[-1]
    num_of_char += previous_unmemorized_digit
    if num_of_char > last_memorized_digit:
        result_num_list.append(num_of_char)
        previous_unmemorized_digit = 0
    else:
        previous_unmemorized_digit = num_of_char * 10

print(f"The result trick num list is {result_num_list}")
