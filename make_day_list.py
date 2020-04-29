import datetime
import time
from datetime import datetime as dt
from datetime import timedelta

def get_today():
    '''
    今日の日付を取得する
    '''
    return datetime.date.today()


def get_today_yyyymmdd():
    '''
    今日の日付をyyyymmdd形式で取得する
    '''
    return get_today().strftime('%Y%m%d')


def get_day_list(s, e):
    '''
    指定の開始日から終了日までの日付リストを作成する
    '''
    strdt = dt.strptime(f'{s}', '%Y%m%d')
    enddt = dt.strptime(f'{e}', '%Y%m%d')
    days_num = (enddt - strdt).days + 1

    day_list = []
    for i in range(days_num):
        date = strdt + timedelta(days=i)
        day_list.append(date.strftime("%Y%m%d"))
    
    return day_list


def main():
    s = '20200401'
    e = get_today_yyyymmdd()
    print(get_day_list(s,e))


if __name__ == '__main__':
    main()

