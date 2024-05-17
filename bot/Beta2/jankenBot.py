import pandas as pd
import csv
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from openpyxl import Workbook
import random

# 準備
hands = [0]*4
count = 0
your_hand_now = 0
wb = Workbook()
ws = wb.active
df = pd.read_csv('C:/Users/rykts/Documents/JANKEN/bot/Beta2/hand.csv')

with open("C:/Users/rykts/Documents/JANKEN/bot/Beta2/hand.csv", 'a', newline='')as f:
    writer = csv.writer(f)
    f.truncate(0) #現在のファイルサイズを０にする

def randomJanken():
    for _ in range(3):
        your_hand_now = int(input("あなたの手: "))
        hands[0] = hands[1]
        hands[1] = hands[2]
        hands[2] = hands[3]
        hands[3] = your_hand_now
        if your_hand_now == random.randint(1, 3):

            with open('C:/Users/rykts/Documents/Codes/Projects/janken/result.csv', 'a', newline='\n') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow("w")
                # print("「{}」を書き込みました".format(hands))
            csvFile.close()
        else:
            with open('C:/Users/rykts/Documents/Codes/Projects/janken/result.csv', 'a', newline='\n') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow("l")
                # print("「{}」を書き込みました".format(hands))
            csvFile.close()
    for _ in range(10):
        your_hand_now = int(input("あなたの手: "))
        hands[0] = hands[1]
        hands[1] = hands[2]
        hands[2] = hands[3]
        hands[3] = your_hand_now
        # csvファイルに書き込み
        with open('C:/Users/rykts/Documents/JANKEN/bot/Beta2/hand.csv', 'a', newline='\n') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(hands)
            # print("「{}」を書き込みました".format(hands))
        csvFile.close()
        if your_hand_now == random.randint(1, 3):

            with open('C:/Users/rykts/Documents/Codes/Projects/janken/result.csv', 'a', newline='\n') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow("w")
                # print("「{}」を書き込みました".format(hands))
            csvFile.close()
        else:
            with open('C:/Users/rykts/Documents/Codes/Projects/janken/result.csv', 'a', newline='\n') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow("l")
                # print("「{}」を書き込みました".format(hands))
            csvFile.close()


# データ作成
randomJanken()

for i in range(87):
    your_hand_now = int(input("あなたの手: "))

    # データ読み込み
    X = df[["b3h", "b2h", "b1h"]]
    Y = df["hand"]

    # モデル作成
    clf = RandomForestClassifier(random_state=70)
    clf.fit(X, Y)

    # 予測
    hands[0] = hands[1]
    hands[1] = hands[2]
    hands[2] = hands[3]
    hands[3] = your_hand_now

    your_hand = pd.DataFrame(
        {"b3h": [hands[0]], "b2h": [hands[1]], "b1h": [hands[2]]})
    pred = clf.predict(your_hand)

    if your_hand_now == pred:

        with open('C:/Users/rykts/Documents/Codes/Projects/janken/result.csv', 'a', newline='\n') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow("w")
            # print("「{}」を書き込みました".format(hands))
        csvFile.close()
    else:
        with open('C:/Users/rykts/Documents/Codes/Projects/janken/result.csv', 'a', newline='\n') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow("l")
            # print("「{}」を書き込みました".format(hands))
        csvFile.close()

    with open('C:/Users/rykts/Documents/JANKEN/bot/Beta2/hand.csv', 'a', newline='\n') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(hands)
        # print("「{}」を書き込みました".format(hands))
        csvFile.close()

print("終了しました")
