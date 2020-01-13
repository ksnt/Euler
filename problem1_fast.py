def sum_3_or_5():
    return sum_multiple(3) + sum_multiple(5) - sum_multiple(15)

def sum_multiple(mult):
    n = 999 // mult
    return 1/2 * n * (2 * mult + (n - 1) * mult)

if __name__ == "__main__":
    num = 1000
    print(sum_3_or_5())