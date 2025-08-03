# 学習済モデルを使って単語同士がどのくらい似ているかを判断する。
# りんご、みかん　＞＞　高得点
# りんご、車　＞＞　低得点
from transformers import BertJapaneseTokenizer, BertModel
import torch

tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese')
model = BertModel.from_pretrained('cl-tohoku/bert-base-japanese')

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    # 文ベクトルを最後の隠れ状態の平均で取得
    return outputs.last_hidden_state.mean(dim=1)

vec1 = get_embedding(input("単語１:"))
vec2 = get_embedding(input("単語２:"))

similarity = torch.cosine_similarity(vec1, vec2, dim=1)
print(f"Cosine similarity: {similarity.item():.4f}")
