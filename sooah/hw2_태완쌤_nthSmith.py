def is_prime(n):
    if n < 1 : return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False

    return True

def digit_sum(n):
    sum = 0

    while (n > 0):
        cur_digit = n % 10
        sum += cur_digit
        n = n // 10

    return sum

def isSmithNumber(n):
    if n < 3 : return False
    elif (is_prime(n)): return False
    sum_n = digit_sum(n)

    sum_factor = 0
    while (not is_prime(n)):
        for new_factor in range(2, int(n ** 0.5) + 1):
            if (n % new_factor == 0) & (is_prime(new_factor)):
                sum_factor += digit_sum(new_factor)
                n = n / new_factor
                break

    sum_factor += digit_sum(n)

    return (sum_n == sum_factor)


def nthSmithNumber(n):
    cur_n = -1
    cur_num = -1

    while (cur_n < n):
        cur_num += 1
        if isSmithNumber(cur_num): cur_n += 1

    return cur_num