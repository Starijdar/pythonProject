def get_multiplied_digits(numbers):
    str_number = str(numbers)
    if len(str_number) != 1:
        first = int(str_number[:1])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        first = int(str_number)
        return first









result = get_multiplied_digits(40203)
print(result)