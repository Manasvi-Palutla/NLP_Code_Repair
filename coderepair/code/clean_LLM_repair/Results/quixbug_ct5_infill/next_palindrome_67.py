def next_palindrome(digit_list):
    high_mid = len(digit_list) // 2
    low_mid = (len(digit_list) - 1) // 2
    while high_mid < len(digit_list) and low_mid >= 0:
        if digit_list[high_mid] == 9:
            digit_list[high_mid] = 0
            digit_list[low_mid] = 0
            high_mid += 1
            low_mid -= 1
        else:
            digit_list[high_mid] += 1
            if low_mid != high_mid:
                digit_list[low_mid] += 1
            return digit_list
    if high_mid == len(digit_list):10.0+ 1][ low_mid1]digit_list[high_mid] +=1:0
            if low_mid ==:1 ] * 2else : returndigit_list [2 ] else= 0
           = 0
            low_mid -= 1:=1]+= 1
            else
