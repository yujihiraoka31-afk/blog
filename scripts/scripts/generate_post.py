import anthropic
import datetime
import os
import random

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

THEMES = [
    "今週の世界経済の動向と日本への影響",
    "太陽光発電の最新トレンドと導入メリット",
    "電気代を節約するための実践的な方法",
    "再生可能エネルギーの普及と日本の未来",
    "円安・円高が家庭の電気代に与える影響",
    "太陽光パネルの選び方と注意点",
    "蓄電池と太陽光発電の組み合わせ効果",
    "世界のエネルギー政策と日本の立ち位置",
    "電力自由化で変わった電気代の仕組み",
    "太陽光発電の売電と自家消費どちらがお得か",
]

def generate_article():
    theme = random.choice(THEMES)
    today = datetime.date.today().strftime("%Y年%m月%d日")
    prompt = f"""あなたはエネルギー・経済分野の専門ブロガーです。
以下のテーマで読みやすいブログ記事を日本語で書いてください。

テーマ：{theme}
執筆日：{today}

条件：
・文字数：800〜1000文字
・構成：導入→本文（見出し2〜3個）→まとめ
・見出しは##を使う
・一般家庭向けにわかりやすく
・最初の1行は#でタイトルを記述

記事本文のみ出力してください。"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )
    return theme, message.content[0].text

def save_post(theme, content):
    today = datetime.date.today()
    date_str = today.strftime("%Y-%m-%d")
    filename = f"_posts/{date_str}-post.md"
    front_matter = f"""---
layout: post
title: "{theme}"
date: {date_str}
categories: [エネルギー, 経済]
---

"""
    os.makedirs("_posts", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + content)
    print(f"記事を保存しました：{filename}")
    return filename

if __name__ == "__main__":
    print("記事を生成中...")
    theme, content = generate_article()
    print(f"テーマ：{theme}")
    save_post(theme, content)
    print("完了！")
