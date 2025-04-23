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
    - 1return[ 1(=if digit_list[low_mid]if<= high_mid:+ 1
            low_midif- 1
 attack_list [ high_midif high_mid10digit_list( int ((= 2= 1) if!=:++1
            high_mid = ( high_mid
