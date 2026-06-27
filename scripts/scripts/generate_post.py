import anthropic
import datetime
import os
import random

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

THEMES = [
    {"ja": "今週の世界経済の動向と日本への影響", "en": "worldeconomyjapan"},
    {"ja": "太陽光発電の最新トレンドと導入メリット", "en": "solarpanelenergy"},
    {"ja": "電気代を節約するための実践的な方法", "en": "electricitysavinghome"},
    {"ja": "再生可能エネルギーの普及と日本の未来", "en": "renewableenergyfuture"},
    {"ja": "円安・円高が家庭の電気代に与える影響", "en": "japaneconomycurrency"},
    {"ja": "太陽光パネルの選び方と注意点", "en": "solarinstallation"},
    {"ja": "蓄電池と太陽光発電の組み合わせ効果", "en": "batterystorage"},
    {"ja": "世界のエネルギー政策と日本の立ち位置", "en": "energypolicyglobal"},
    {"ja": "電力自由化で変わった電気代の仕組み", "en": "electricitymarket"},
    {"ja": "太陽光発電の売電と自家消費どちらがお得か", "en": "solarenergysavings"},
]

def get_image_url(keyword):
    seed = abs(hash(keyword)) % 1000
    return f"https://picsum.photos/seed/{seed}/1200/630"

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

def save_post(theme, content):
    today = datetime.date.today()
    date_str = today.strftime("%Y-%m-%d")
    filename = f"_posts/{date_str}-post.md"

    image_url = get_image_url(theme["en"])

    front_matter = (
        "---\n"
        "layout: post\n"
        f'title: "{theme["ja"]}"\n'
        f"date: {date_str}\n"
        "categories: [エネルギー, 経済]\n"
        f'image: "{image_url}"\n'
        "---\n\n"
    )

    image_tag = f"![記事のイメージ画像]({image_url})\n\n"

    os.makedirs("_posts", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + image_tag + content)

    print(f"記事を保存しました：{filename}")
    print(f"画像URL：{image_url}")
    return filename

if __name__ == "__main__":
    print("記事を生成中...")
    theme = random.choice(THEMES)
    print(f"テーマ：{theme['ja']}")
    content = generate_article(theme["ja"])
    save_post(theme, content)
    print("完了！")
