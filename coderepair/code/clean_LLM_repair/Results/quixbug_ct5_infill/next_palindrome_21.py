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
    [ low_mid ]int ( high_mid )(high_mid0
           = 1
           int ( low_mid ) +2
 angr0
           digit_list [1
           ] = 2
Formula2
Formula ) else :if low_mid1
Formula112
Formula0:2
Formula )if high_mid > 0
