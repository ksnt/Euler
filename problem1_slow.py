def sum_3_or_5(num_list):
    result = 0
    for n in num_list:
        if n % 3 == 0 or n % 5 == 0:
            result += n
        else:
            pass
    return result


if __name_ == "__main__"
    num = 1000
    num_list = [i for i in range(num)]
    return sum_3_or_5(num_list)