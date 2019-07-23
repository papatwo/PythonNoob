in_str = "Help, my keyboard is not working"
# in_str = "Hi my name is Adam Levine"
a_idx = []
out_str = ""
upper_flag = -1

# sentence = in_str.split('')

# print(sentence)
# for i, c in enumerate(in_str):
#     if c == 'a' or c == 'A':
#         a_idx.append()

for c in in_str:
    if c is not 'a' and c is not 'A':
        if upper_flag == -1:
            out_str += c
            print(out_str)
        else:
            out_str += c.upper()

    else:
        upper_flag *= -1
print(out_str)

# Hi my nME IS dM LEVINE
# Help, my keyboRD IS NOT WORKING



'''
The 'a' key on the keyboard is not working correctly. Instead of typing 'a' or
'A', it toggles the CapsLock.  Return the value of a string that is typed into
a keyboard on such a faulty keyboard. Note: If shift is pressed when CapsLock
is on characters will be printed in lower case

e.g.  Input: "Help, my keyboard is not working" Output: "Help, my keyboRD IS
NOT WORKING"

Input: "Hi my name is Adam Levine" Output: "Hi my nME IS dM lEVINE" 
'''
