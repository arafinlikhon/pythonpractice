input_str = input("Enter comma-separated values: ")
lst = input_str.split(',')

lstindex = len(lst) - 1
index = 0
ondex = index + 1

result_list = []  # Initialize an empty list to store the results
only = int(lst[0])
result_list.append(only)

while index < lstindex:
    result = int(lst[index]) + int(lst[ondex])
    result_list.append(result)  # Append the result to the list
    index += 1
    ondex += 1

print(result_list)
