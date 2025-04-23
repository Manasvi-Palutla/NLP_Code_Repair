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
    [= 1
            else:low_mid] = 0#0
            else:=(] = 1 #for i in< len ( digit_list )2:- 11==for i# 2
XSD if= 11if0:] = 0
           2= ( 1= 0
            ifelse:
