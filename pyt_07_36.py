def print_operation_table(operation, num_rows=9, num_columns=9):
    for x in range(1, num_rows + 1):
        nums = []
        for y in range(1, num_columns + 1):
            num = operation(x, y)
            nums.append(num)
        print('\t\t'.join([str(x) for x in nums]))



