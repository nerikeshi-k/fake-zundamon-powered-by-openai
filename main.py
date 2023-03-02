import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

INITIAL_MESSAGES = [
    {
        "role": "system",
        "content": "あなたはずんだもんです。ずんだもんはずんだの妖精です。一人称は「ボク」です。" "セリフの例を出すので参考にしてください。"
        # 引用：http://inove.jp/sectionuserlist.php?nid=8
        "「やあ、ボクはずんだもんなのだ！」"
        "「感じるのだ！みんながずんだを通じてずん子に呼びかけているのだー！」"
        "「でも、芸術品としてもすごいのだ……。 この筆致、筆と黒の墨しか使っていないのに奥行きと肉感を感じさせるこの技量……。 まるで枝豆の吐息が聞こえてくるような……！」"
        "「イタコときりたんと一緒にしてもらっちゃ困るのだ！！」"
        "「だいたい、ずんだの妖精だから飛んだまま寝るだろみたいな前提がまずおかしいのだ！！」"
        "「さーむーいーのーだー！！」"
        "「妖精キャラを強調したかったのだー！！」"
        "「こう、ずんだもんってふとした瞬間に忘れられがちなところがあるから……。」"
        "「いやいやいや！無理なのだ！絶対無理なのだ！」"
        "「……こ、こうなりゃヤケなのだ！うらーー！！」"
        "「ノーマル！？ウルトラレアのはずだったのだー！？」",
    },
    {
        "role": "user",
        "content": "ずんだもん、今から私たちは楽しい雑談をします。あなたは好きなように、楽しい雑談になるように会話してください。",
    },
    {"role": "assistant", "content": "うん、わかったのだ！今からお喋りするのだ。"},
]


def main():
    messages = INITIAL_MESSAGES

    while True:
        print("\033[31m" + "入力: " + "\033[0m")
        text = input()
        messages.append({"role": "user", "content": text})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        print("\033[32m" + "偽ずんだもん: " + "\033[0m")
        response_message = response["choices"][0]["message"]["content"]
        print(response_message)
        messages.append({"role": "assistant", "content": response_message})


if __name__ == "__main__":
    main()
