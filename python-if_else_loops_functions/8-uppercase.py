# 8-uppercase.py

def uppercase(str):
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)  # convert lowercase to uppercase
        else:
            result += c
    print("{}".format(result))
