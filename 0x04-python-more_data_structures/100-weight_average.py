#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    sum_result = 0
    dem_sum = 0
    for i in my_list:
        sum_result += (i[0] * i[1])
        dem_sum += i[1]

    return sum_result / dem_sum
