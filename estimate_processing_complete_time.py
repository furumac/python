import os
import sys

def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def main():
    print('='*100)

    # 未入力の場合はカレントディレクトリを対象とする
    target_path = input('測定するディレクトリ: ')
    if not target_path: target_path = '.'

    while True:
        index_size = input('指標サイズ (MB): ')
        if index_size: break

    while True:
        index_min = input('指標時間 (分): ')
        if index_min: break

    total_size_kb = round(float(get_dir_size(target_path) / 1024), 0)
    total_size_mb = round(float(total_size_kb / 1024), 0)
    total_size_gb = round(float(total_size_mb / 1024), 1)

    total_min = round((total_size_mb * float(index_min) / float(index_size)), 1)
    total_hour = round(float(total_min / 60), 1)
    total_day = round(float(total_hour / 24), 1)

    print('='*100)
    print(f'対象ファイル総量 (MB):    {int(total_size_mb)} MB    [{total_size_gb}GB]')
    print(f'推定総時間      (分):     {int(total_min)} 分     [{total_hour}時間] [{total_day}日]')
    print('='*100)

if __name__ == '__main__':
    main()