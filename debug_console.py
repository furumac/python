import time

def debug(msg = '-'):
    '''
    デバッグ情報を出力する
    '''
    now = time.ctime()
    exe_time = time.strptime(now)
    exe_time = time.strftime("%Y/%m/%d %H:%M:%S", exe_time)
    print(f"{exe_time}  [{msg}]")


def main():

    debug('処理開始')
    debug('処理終了')

if __name__ == '__main__':
    main()