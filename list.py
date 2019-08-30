number = [2, 4, 6]
increased_one = [n + 1 for n in number]
print(increased_one)

numbers = [0, 3, 4, 0, 22, 1]
non_zero_num = [num for num in numbers if num != 0]
print(non_zero_num)

class_name = ['ITEC 2560', 'BTEC 1010', 'ITEC 2905']
non_ITEC_c = [non_ITEC for non_ITEC in class_name if 'ITEC' in non_ITEC]
print(non_ITEC_c)


