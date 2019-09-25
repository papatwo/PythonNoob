def reverse_num(num):
    if len(num) == 0:
        return ""
    return num[-1]+reverse_num(num[:-1])


if __name__ == '__main__':
    print(reverse_num('123456'))

