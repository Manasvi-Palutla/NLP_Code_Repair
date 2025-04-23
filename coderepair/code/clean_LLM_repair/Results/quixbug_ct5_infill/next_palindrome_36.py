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
    [ low_mid ]1
           ifhigh_midhigh_mid ] = 11high_mid2
Formula else:2
Formula= 0+101:8
Formula0 :1:1=1
Formula digit_list [ 8] = 0
Formula digit_list0 : 22
Formula digit_list [= 2=] = 0
