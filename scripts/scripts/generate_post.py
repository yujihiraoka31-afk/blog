import anthropic
import datetime
import os
import random

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

THEMES = [
    {"ja": "今週の世界経済の動向と日本への影響", "en": "world economy japan"},
    {"ja": "太陽光発電の最新トレンドと導入メリット", "en": "solar panel energy"},
    {"ja": "電気代を節約するための実践的な方法", "en": "electricity saving home"},
    {"ja": "再生可能エネルギーの普及と日本の未来", "en": "renewable energy future"},
    {"ja": "円安・円高が家庭の電気代に与える影響", "en": "japan economy currency"},
    {"ja": "太陽光パネルの選び方と注意点", "en": "solar panel installation"},
    {"ja": "蓄電池と太陽光発電の組み合わせ効果", "en": "battery storage solar"},
    {"ja": "世界のエネルギー政策と日本の立ち位置", "en": "energy policy global"},
    {"ja": "電力自由化で変わった電気代の仕組み", "en": "electricity market reform"},
    {"ja": "太陽光発電の売電と自家消費どちらがお得か", "en": "solar energy savings"},
]

def get_image_url(keyword):
   return f"https://picsum.photos/seed/{keyword.replace(' ', '')}/1200/630"

def generate_article(theme_ja):
    today = datetime.date.today().strftime("%Y年%m月%d日")
    prompt = f"""あなたはエネルギー・経済分野の専門ブロガーです。
以下のテーマで読みやすいブログ記事を日本語で書いてください。

テーマ：{theme_ja}
執筆日：{today}

条件：
・文字数：1,800〜2,200文字
・構成：導入（200字）→本文（見出し3〜4個、各300〜400字）→まとめ（200字）
・見出しは##を使う
・小見出しは###を使う
・一般家庭向けにわかりやすく
・具体的な数字や事例を入れる
・最初の1行は#でタイトルを記述
・タイトルは記事内容を反映した魅力的なものにする

記事本文のみ出力してください。"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

def save_post(theme, content, image_url):
    today = datetime.date.today()
    date_str = today.strftime("%Y-%m-%d")
    filename = f"_posts/{date_str}-post.md"
    front_matter = f"""---
layout: post
title: "{theme['ja']}"
date: {date_str}
categories: [エネルギー, 経済]
image: "{image_url}"
---

![記事のイメージ画像]({image_url})

"""
    os.makedirs("_posts", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + content)
    print(f"記事を保存しました：{filename}")
    return filename

if __name__ == "__main__":
    print("記事を生成中...")
    theme = random.choice(THEMES)
    print(f"テーマ：{theme['ja']}")
    image_url = get_image_url(theme['en'])
    content = generate_article(theme['ja'])
    save_post(theme, content, image_url)
    print("完了！")
