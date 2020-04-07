import sys
import logging
from collections import Counter
from pathlib import Path
from typing import List, Iterator, TextIO

import MeCab

tagger = MeCab.Tagger('')
tagger.parse('')


def check_argv(argvs):
    '''
    コマンドライン引数をチェックする。
    引数は１つ。読み込むディレクトリ名を指定する
    '''
    argc = len(argvs)
    if (argc != 2):
        print(f'Usage: $python {argvs[0]} (dir_name)')
        quit()


def main():
    '''
    コマンドライン引数で指定したディレクトリ内のファイルを
    読み込んで、頻出単語を表示する
    '''
    argvs = sys.argv
    check_argv(argvs)
    input_dir = Path(argvs[1])
    
    # 単語の出現回数を保持する
    frequency = Counter()

    for path in sorted(input_dir.glob('*/wiki_*')):
        logging.info(f'Processing {path}...')

        with open(path) as file:
            # ファイルに含まれる記事内の単語の出現回数を数えす
            frequency += count_words(file)

    for word, count in frequency.most_common(30):
        print(word, count)


def count_words(file: TextIO) -> Counter:
    '''
    WikiExtractorが出力したファイルに含まれる全ての記事から
    単語の出現回数を数える
    '''
    frequency = Counter()
    num_docs = 0  # ログ出力用に処理した記事数を数える

    for content in iter_doc_contents(file):  # ファイル内の全記事
        words = get_words(content)  # 記事に含まれる名詞のリストを取得
        frequency.update(words)  # リストに含まれる値の出現数を一度に増やす
        num_docs += 1
    
    logging.info(f'Found {len(frequency)} words from {num_docs} documents.')
    return frequency


def iter_doc_contents(file: TextIO) -> Iterator[str]:
    '''
    ファイルオブジェクトを読み込んで、記事の中身（開始タグ <doc ...>>
    と終了タグ </doc> の間のテキスト）を順に返すジェネレーター関数
    '''
    for line in file:
        # 開始タグが見つかったらバッファを初期化
        if line.startswith('<doc '):
            buffer = []
        # 終了タグが見つかったらバッファの中身を結合してyieldする
        elif line.startswith('</doc>'):
            content = ''.join(buffer)
            yield content
        # 開始タグ・終了タグ以外の行はバッファに追加する
        else:
            buffer.append(line)


def get_words(content: str) -> List[str]:
    '''
    文字列内に出現する名詞のリスト(重複含む)を取得する
    '''
    words = []  # 出現した名詞を格納するリスト

    node = tagger.parseToNode(content)
    while node:
        # カンマ区切りの最初の２項目をpos, pos_sub1に代入
        pos, pos_sub1 = node.feature.split(',')[:2]
        # 固有名詞または一般名詞の場合のみwordsに追加する
        if pos == '名詞' and pos_sub1 in ('固有名詞', '一般'):
            words.append(node.surface)
        node = node.next
    
    return words


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
