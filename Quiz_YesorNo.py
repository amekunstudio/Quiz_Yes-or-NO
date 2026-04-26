# 「q」と「Questions」と「Q_Answers」を増やすことで使えます
# qは問題数です
q = 2
score = 0
Player_answer = 0
Questions = ["これは例題である",
             "これは例題ではない"]
Q_Answers = ["yes","no"]

def let_start():
    global score
    while True:
        is_start = input("クイズを始めますか？(yes/no): ").lower().strip()

        if is_start == "yes":
            print("では始めます！")
            score =0
            Main()
            break

        elif is_start == "no":
            print("また遊んでね！")
            break

        else:
            print("yesかnoで答えてね！")


def Main():
    global score
    for i in range(q):
        print(f"\n第{i+1}問目: "+Questions[i])
        Player_answer = input("回答(yes/no): ").lower().strip()

        if Player_answer == Q_Answers[i]:
            print("正解です！")
            score += 1

        else:
            print("残念！")

    print(f"\n終了！あなたのスコアは{score}点です！")

    if score == q:
        print("おめでとう！満点です！")

    is_Retry()


def is_Retry():
    global score
    while True:
        retry = input("\nもう一度遊びますか？(yes/no)").lower().strip()

        if retry == "yes":
            print("ありがとう！")
            score = 0
            let_start()
            break

        elif retry == "no":
            print("また遊んでね！")
            break
        else:
            print("yesかnoで答えてね！")

let_start()

