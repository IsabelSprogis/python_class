my_list = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]
highest_value = 0
lowest_value = 0
even_numbers = []
odd_numbers = []
index_zero = 0
average = 0
below_zero = 0

print(my_list)

for index in range(0, len(my_list)):
    print(f'{index} : {my_list[index]}')
    if highest_value < my_list[index]:
        highest_value = my_list[index]
        print(f'New high value: {highest_value}')
    elif lowest_value > my_list[index]:
        lowest_value = my_list[index]
        print(f'New Low Value: {lowest_value}')
    elif my_list[index] == my_list[0]:
        index_zero += 1
    # Even or odd numbers to a separate list
    if my_list[index] % 2 == 0:
        even_numbers.append(my_list[index])
    else:
        odd_numbers.append(my_list[index])
    # Sum of below zero numbers
    if my_list[index] < 0:
        below_zero = below_zero + my_list[index]
    # Average sum of numbers in list
    average = average + my_list[index]
average = average / len(my_list)

print(f'Highest value: {highest_value}')
print(f'Lowest Value: {lowest_value}')
print(f'Even Int Numbers in list: {even_numbers}')
print(f'Odd Int Numbers in list: {odd_numbers}')
print(f'Number of times Index 0 [{my_list[0]}] repeats:  {index_zero} ')
print(f'Average number from the list: {average}')
print(f'Sum of below zero numbers: {below_zero}')
