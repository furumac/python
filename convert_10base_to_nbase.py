# 2,8,16進数に変換
BASE_LIST = [2, 8, 16]

# 16進数変換dict
HEX_CONV = {
    10 : 'A',
    11 : 'B',
    12 : 'C',
    13 : 'D',
    14 : 'E',
    15 : 'F',
}


def convert(base10, n):
    result = ''

    while base10 > 0:
        result = str(base10 % n) + result
        base10 //= n

    return result


def convert16(base10):
    result = ''

    while base10 > 0:
        amari = base10 % 16
        if amari >= 10: amari = HEX_CONV[amari]
        result = str(amari) + result
        base10 //= 16
    
    return result


def main():
    base10 = int(input('10進数:'))

    for n in BASE_LIST:
        if n == 16:  # 16進数
            result = convert16(base10)
        else:  # 2,8進数
            result = convert(base10,n)

        print(f'{n}進数: {result}')


if __name__ == '__main__':
    main()