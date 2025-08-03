# 単語をローマ字に変換し、母音を抽出
from pykakasi import kakasi # 日本語　＞＞　ローマ字
import re  # 文字列操作を行うため

kks = kakasi() 
result = kks.convert(input("ひらがな:"))

romaji = ''.join([item['hepburn'] for item in result])

def convert_n_to_nn(text):
    return re.sub(r'n(?=[^aeiouy]|$)', 'nn', text) # nの後ろがaiueoy以外だったらnnにする

romaji = convert_n_to_nn(romaji)
print("ローマ字:", romaji)

# 1. nが連続したら1つにまとめる
romaji = re.sub(r'n+', 'n', romaji) # nが連続した場合n一つにする
# 例: 'onn' → 'on', 'nni' → 'ni'

# 2. 抽出対象の文字（母音 + n）
target_chars = 'aeioun'

# 3. 母音＋nのみ抽出
extracted = [c for c in romaji if c in target_chars]

print(extracted)