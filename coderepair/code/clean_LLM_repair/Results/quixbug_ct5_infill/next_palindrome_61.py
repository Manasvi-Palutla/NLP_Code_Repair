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
    end11 := 0
            high_mid =# 2
SURFACE= (len(digit_list) -# 2
SURFACE else:++ high_midlow_mid =0 :high_mid + 1]10:: if low_mid> 0:10:+ 1
            low_mid1:
               1:
                digit_list[
