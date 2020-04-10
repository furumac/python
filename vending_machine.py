import sys

MONEY = [5000, 1000, 500, 100, 50, 10, 5, 1]


def is_ok_input_price(input):
    return True if input.isdecimal() else False


def is_ok_product_price(product):
    return True if product.isdecimal() else False


def output(change):
    for i in MONEY:
        r = change // i
        change %= i
        print(f'{str(i)} : {str(r)}')


def main():
    input_price = input('入力金額: ')
    if is_ok_input_price(input_price) == False:
        print('整数を入力してください')
        sys.exit()

    product_price = input('製品金額: ')
    if is_ok_product_price(product_price) == False:
        print('整数を入力してください')
        sys.exit()

    change = int(input_price) - int(product_price)
    if change < 0:
        print('金額が不足しています')
        sys.exit()
        
    output(change)


if __name__ == '__main__':
    main()
