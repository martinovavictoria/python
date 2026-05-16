nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

result = [num for two_d in nice_list for one_d in two_d for num in one_d]

print(result)
