def input_nums():
    num = [int(x) for x in input().split()]
    return num


def calculate_average(avarage):
    s = sum(avarage)
    res = s // len(avarage)
    print(res)

calculate_average(input_nums())