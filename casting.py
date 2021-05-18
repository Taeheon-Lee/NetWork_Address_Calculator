"For casting Function"

def de_to_bi(input_num):
    """
    Casting decimal to binary
    """
    if input_num in (0, 1):
        return input_num
    if input_num < 0:
        raise ValueError("The number should be positive")
    answer = ""
    while input_num != 0:
        tmp = input_num % 2
        input_num = input_num // 2
        answer = str(tmp) + answer
    return answer

def bi_to_de(input_num):
    """
    Casting binary to decimal
    """
    if input_num in (0, 1):
        return input_num
    if input_num < 0:
        raise ValueError("The number should be positive")
    answer = 0
    fac = 0.5
    while input_num != 0:
        fac = fac * 2
        answer = answer + input_num % 10 * fac
        input_num = input_num // 10
    return answer
