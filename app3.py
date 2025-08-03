import fugashi

tagger = fugashi.Tagger()

# 文節を構成する基本品詞
BREAK_POS = {'名詞', '動詞', '接頭詞', '副詞', '感動詞', '形容詞', '形容動詞', '連体詞'}

def is_no_break(word, prev_features):
    pos1 = word.feature.pos1
    pos2 = word.feature.pos2
    aConType = getattr(word.feature, 'aConType', '')  # 安全に取得

    no_break = False
    if "接尾" in (pos2 or ""):
        no_break = True
    if "非自立" in (pos2 or ""):
        no_break = True
    if prev_features.get("is_prefix", False):
        no_break = True
    if prev_features.get("is_sahen_noun", False) and pos1 == "動詞" and aConType == "サ変・スル":
        no_break = True

    return no_break


def bunsetsu_wakachi(text):
    words = list(tagger(text))
    result = []
    chunk = ""

    prev_features = {
        "is_prefix": False,
        "is_sahen_noun": False,
    }

    for word in words:
        pos1 = word.feature.pos1
        pos2 = word.feature.pos2
        aConType = getattr(word.feature, 'aConType', '')  # unidic用

        should_break = pos1 in BREAK_POS and not is_no_break(word, prev_features)

        if should_break and chunk:
            result.append(chunk)
            chunk = ""

        chunk += word.surface

        prev_features = {
            "is_prefix": (pos1 == "接頭詞"),
            "is_sahen_noun": (pos1 == "名詞" and pos2 == "サ変接続"),
        }

    if chunk:
        result.append(chunk)

    return result


if __name__ == "__main__":
    text = input("分かち書きしたい文章: ")
    print("文節分割:", bunsetsu_wakachi(text))
