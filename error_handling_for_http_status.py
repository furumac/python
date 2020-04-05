import time
import random
import requests

# 代表的なHTTPステータスコード
STATUS_CODE = {
    # リクエストが継続している
    100 : 'Continue',
    # リクエストは成功した
    200 : 'OK',
    # リクエストしたリソースは恒久的に移動した
    301 : 'Moved Permanently',
    # リクエストしたリソースは一時的に移動した
    302 : 'Found',
    # リクエストしたリソースは更新されていない
    304 : 'Not Modified',
    # クライアントのリクエストに問題があるため処理できない
    400 : 'BadRequest',
    # 認証されていないため処理できない
    401 : 'Unauthorized',
    # リクエストは許可されていない
    403 : 'Forbidden',
    # リクエストしたリソースは存在しない
    404 : 'Not Found',
    # 一定時間内にリクエストの送信が完了しなかった
    408 : 'Request Timeout',
    # サーバー内部で予期せぬエラーが発生した
    500 : 'Internal Server Error',
    # ゲートウェイサーバーが背後のサーバーからエラーを受け取った
    502 : 'Bad Gateway',
    # サーバーは一時的にリクエストを処理できない
    503 : 'Service Unavailable',
    # ゲートウェイサーバーから背後のサーバーへのリクエストがタイムアウトした
    504 : 'Gateway Timeout',
}

# 一時的なエラーを表すステータスコード
TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)

# リトライする最大数
MAX_RETRIES = 3


def main():

    # dictからkey(status_code)だけのlistを作成する
    status_list = [str(key) for key, value in STATUS_CODE.items()]
    # URLアクセス用に(,)区切りで結合する
    status = ','.join(status_list)

    # HTTPクライアントのテスト用Webサービス。ランダムにステータスコードを返す
    response = fetch(f'http://httpbin.org/status/{status}')
    if 200 <= response.status_code < 300:
        print('Success!')
    else:
        print('Error')


def fetch(url: str) -> requests.Response:
    retries = 0  # 現在のリトライ回数
    while True:
        try:
            print(f'Retrieving {url}...')
            response = requests.get(url)
            print(f'Status: {response.status_code}')
            if response.status_code not in TEMPORARY_ERROR_CODES:
                # 一時的なエラーでなければresponseを返して終了
                return response

        except requests.exceptions.RequestException as ex:
            # ネットワークレベルのエラーの場合はログを出力してリトライする
            print(f'Network-level exception occured: {ex}')

        retries += 1  # リトライ処理
        if retries >= MAX_RETRIES:
            # リトライ回数の上限を超えた場合は例外を発生させる
            raise Exception('Too many retries.')

        wait = 2**(retries - 1)  # 指数関数的なリトライ間隔を求める
        print(f'Waiting {wait} seconds...')
        time.sleep(wait)


if __name__ == '__main__':
    main()
