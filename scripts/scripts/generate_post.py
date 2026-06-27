image_tag = f"![記事のイメージ画像]({image_url})\n\n"

    cta = """
---

## 🏠 太陽光発電の導入をご検討の方へ

この記事をご覧いただき、太陽光発電に興味をお持ちになりましたか？

**株式会社テクノホーム**では、太陽光パネルの設置から蓄電池の導入まで、
お客様のご自宅に最適なプランをご提案しています。

✅ 無料相談・無料お見積もり実施中  
✅ 愛知・東海・関東・関西エリア対応  
✅ 補助金・助成金のご案内も対応  

**まずはお気軽にInstagramのDMからご連絡ください👇**

[![InstagramのDMはこちら](https://img.shields.io/badge/Instagram-DMで無料相談-E1306C?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/techno__home__?igsh=MW1jaXN2aGZ0eW1yeg%3D%3D&utm_source=qr)

> 「ブログを見た」とDMいただくとスムーズです😊

---
"""

    os.makedirs("_posts", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + image_tag + content + cta)
