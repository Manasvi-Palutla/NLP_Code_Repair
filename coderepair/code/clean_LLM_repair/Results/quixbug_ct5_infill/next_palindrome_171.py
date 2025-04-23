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
    [ low_mid ] + 1+ 1
            if low_mid: if9:
                if9:
               else:
                digit_list[high_mid]1:1:1:1] if>= 0:+= 1:1:11:1]if low_mid >= 0:= 0:11:1]) return 0
