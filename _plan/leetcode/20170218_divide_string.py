IN_COUNT = 2
OUT_STR_LEN = 8
FILL_PATTERN = '0'


def divide_string():
    for i in range(IN_COUNT):
        in_str = raw_input()
        if len(in_str) > 100:
            print "input string is larger than 100"
            return
        while len(in_str) > OUT_STR_LEN:
            out_str = in_str[0:OUT_STR_LEN]
            in_str = in_str[OUT_STR_LEN:]
            print out_str
        if len(in_str) > 0:
            print in_str.ljust(OUT_STR_LEN, FILL_PATTERN)


str1 = raw_input()
str2 = raw_input()


def divide_string2(in_str):
    if len(in_str) > 100:
        print "input string is larger than 100"
        return
    spare_str_len = len(in_str) % OUT_STR_LEN
    if spare_str_len > 0:
        in_str += FILL_PATTERN * (OUT_STR_LEN - spare_str_len)
    for i in range(len(in_str)):
        print i[OUT_STR_LEN * i:OUT_STR_LEN * i + 8]


if __name__ == '__main__':
    # divide_string()
    divide_string2(str1)
    divide_string2(str2)
