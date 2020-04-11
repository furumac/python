import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():

    while True:
        number = input('いくつまでの数字の素数を調べますか？')
        if not number:
            print('数字が未入力です。')
        else:
            break
    
    for i in range(int(number)):
        if is_prime(i):
            print(i, end=' ')
    print('')


if __name__ == '__main__':
    main()