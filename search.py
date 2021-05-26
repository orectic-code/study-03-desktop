import pandas as pd
import eel

#デスクトップ作成
def s03_search(word, csv_name):
    df = pd.read_csv("./{}".format(csv_name))
    source = list(df["name"])

    #検索
    if word in source:
        print(f"{word}はあります")
        #js関数呼び出し
        eel.view_log_js(f"{word}はあります")
    else:
        print(f"{word}はありません")
        #JS呼び出し
        eel.view_log_js(f"{word}はありません")
        #追加
        source.append(word)
        eel.view_log_js(f"{word}を追加しました")

    #csvに書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./{}".format(csv_name),encoding="utf_8-sig")
    print(source)

