# -*- coding: utf-8 -*-
"""
Build-time helper: generates the 12 static works/*.html pages from the data
below. Not required to view or deploy the site (the output is plain static
HTML) — kept only as a convenience if content needs to be regenerated.
Run: python3 generate_works.py
"""
import os

WORKS = [
    {
        "slug": "lp4",
        "title": "税理士LP",
        "badge": "LP制作",
        "tags": ["LP", "design", "cording", "responsive"],
        "img": "lp4.webp",
        "alt": "税理士LP",
        "desc": [
            "会計事務所のランディングページ。デザインとコーディングを担当。「イラストを用いたやわらかい印象で」とのご要望にあわせて、暖かみのあるイメージに仕上げました。",
            "新規事業立ち上げのターゲット層に向けて、会計事務所への問い合わせに対するハードルが高くならないよう優しいタッチに。",
        ],
        "tools": "Figma / Illustrator",
        "coding": "HTML / SCSS",
        "duration": "約２週間程度",
        "urls": ["https://www.sumida-feel.com/lp/", "https://www.sumida-feel.com/lp2/"],
    },
    {
        "slug": "lp5",
        "title": "美容医療LP",
        "badge": "LP制作",
        "tags": ["美容医療", "LP", "design", "cording", "responsive"],
        "img": "lp5.webp",
        "alt": "美容医療LP",
        "desc": [
            "美容医療のランディングページ。デザインと部分的コーディングを担当。基本画像貼り付け型のLPページ、CTAボタンやQ&Aなど部分的にコーディングを併用。",
        ],
        "tools": "Figma / Illustrator",
        "coding": "HTML / SCSS",
        "duration": "約２週間程度",
        "urls": [],
    },
    {
        "slug": "lp1",
        "title": "美容医療LP",
        "badge": "LP制作",
        "tags": ["LP", "design", "cording - partly"],
        "img": "lp1.webp",
        "alt": "美容医療LP",
        "desc": [
            "美容医療のランディングページ。デザインと部分的コーディングを担当。基本画像貼り付け型のLPページ、CTAボタンやQ&Aなど部分的にコーディングを併用。LPにあわせたInstagram広告用クリエイティブ制作も担当。",
            "クリニックのテーマであるボタニカルイメージをベースに、ターゲット層である30代前後に向けて落ち着きの中にも遊び心を入れたデザインに。長めのコンテンツのため、読んでいて飽きさせないページ作りを意識しました。",
        ],
        "tools": "Illustrator",
        "coding": "HTML / SCSS",
        "duration": "約２週間程度",
        "urls": [],
    },
    {
        "slug": "website1",
        "title": "美容医療Webサイト",
        "badge": "Website制作",
        "tags": ["Website", "design", "cording", "responsive", "wordpress"],
        "img": "website1.webp",
        "alt": "美容医療Webサイト",
        "desc": [
            "美容医療のWebサイト、TOP＋下層3ページ。デザインとコーディングを担当。",
            "元々お客様側でSTUDIOにて途中まで作られていたデザインイメージをベースに、カンプを作成し、WordPressで再構築。ご要望のクールビューティをイメージに、ハイレベルな学びを得られる印象を持って頂けるようなデザインに仕上げました。",
        ],
        "tools": "Illustrator",
        "coding": "HTML / SCSS / JavaScript / WordPress",
        "duration": "約３週間程度",
        "urls": [],
    },
    {
        "slug": "website2",
        "title": "ITサービスWebサイト",
        "badge": "Website制作",
        "tags": ["Website", "design", "cording", "responsive"],
        "img": "website2.webp",
        "alt": "ITサービスWebサイト",
        "desc": [
            "ITサービスのWebサイト。デザインとコーディングを担当。",
            "シンプルなデザインとのご要望にあわせ、白を基調にしたビジネスライクなデザインに。アニメーションを多く取り入れ、動きをつけることで、シンプルさの中にも遊びがみえるページにしました。",
        ],
        "tools": "Illustrator",
        "coding": "HTML / SCSS / JavaScript",
        "duration": "約３週間程度",
        "urls": [],
    },
    {
        "slug": "lp6",
        "title": "分譲地LP",
        "badge": "LP制作",
        "tags": ["分譲地", "LP", "design", "cording", "responsive"],
        "img": "lp6.webp",
        "alt": "分譲地LP",
        "desc": [
            "田舎暮らしの分譲地ランディングページ。デザインとコーディングを担当。",
            "あまりセールス感が出過ぎないよう、できるだけシンプルなデザインを、とのご要望にあわせてでも飽きさせないようにスライドギャラリーなどを配置しながら、写真を多めに。",
            "都会の喧騒から離れてゆったりとした暮らしをしたい、そんなイメージが膨らむようなデザインにしました。",
        ],
        "tools": "Figma / Illustrator",
        "coding": "HTML / SCSS",
        "duration": "約２週間程度（家族層＋セカンドライフ層の２ページ作成）",
        "urls": ["https://fujiokakoumuten.com/lp/family/"],
    },
    {
        "slug": "portfolio",
        "title": "Portfolio Site",
        "badge": "Portfolio Site",
        "tags": ["Portfolio", "design"],
        "img": "portfolio.webp",
        "alt": "Portfolio Site",
        "desc": [
            "当サイト、ポートフォリオ。",
            "得意カラーのイエロー ✕ ブラックを基調としてシンプルですっきりとした印象のサイトにデザインしました。",
        ],
        "tools": "STUDIO",
        "coding": "Canva（サムネイル制作）",
        "duration": "３時間",
        "urls": [],
    },
    {
        "slug": "logo-1",
        "title": "パーソナルジムロゴ",
        "badge": "LOGO制作",
        "tags": ["LOGO", "design"],
        "img": "logo1.webp",
        "alt": "パーソナルジムロゴ",
        "desc": [
            "パーソナルジムのロゴ制作。",
            "キーカラーに緑＋女性向け＋スタイリッシュなイメージとのご要望のもと、ジムらしいパワフルさも取り入れたデザインにしました。",
            "大変気に入っていただき、Tシャツ等のグッズ展開も。",
        ],
        "tools": "Illustrator",
        "coding": "",
        "duration": "１週間程度",
        "urls": ["https://ausportgym.com/"],
        "url_label": "オスポールジム",
    },
    {
        "slug": "standbyscreen-1",
        "title": "配信待機画面",
        "badge": "StandbyScreen",
        "tags": ["StandbyScreen", "design"],
        "img": "standbyscreen1.gif",
        "alt": "配信待機画面",
        "desc": [
            "Youtubeの配信待機画面。差分として「配信準備中」「サーバー移動中」「配信終了」の３パターン。",
            "ゲーム配信らしいポップさと、依頼者のメインタイトルゲームであるゲームカラーに合わせた「赤・青・緑」をキーカラーにしてデザインしました。",
        ],
        "tools": "Illustrator / After Effects",
        "coding": "",
        "duration": "１日程度",
        "urls": [],
    },
    {
        "slug": "lp2",
        "title": "美容医療LP",
        "badge": "LP制作",
        "tags": ["LP", "design", "cording - partly"],
        "img": "lp2.webp",
        "alt": "美容医療LP",
        "desc": [
            "美容医療のランディングページ。デザインと部分的コーディングを担当。基本画像貼り付け型のLPページ、CTAボタンやQ&Aなど部分的にコーディングを併用。",
            "ターゲット層の30代に向けてシックで上品なイメージに。クリニックのベースカラーであるベージュを基調にしながら、柔らかさも兼ねたデザインに仕上げました。",
        ],
        "tools": "Figma",
        "coding": "HTML / SCSS",
        "duration": "約２週間程度",
        "urls": [],
    },
    {
        "slug": "website3",
        "title": "医療系Webサイト",
        "badge": "Website制作",
        "tags": ["Website", "design", "cording", "responsive"],
        "img": "website3.webp",
        "alt": "医療系Webサイト",
        "desc": [
            "医療系のWebサイト。デザインとコーディングを担当。",
        ],
        "tools": "Illustrator",
        "coding": "HTML / SCSS",
        "duration": "約１～２週間程度",
        "urls": [],
    },
    {
        "slug": "lp3",
        "title": "美容医療LP",
        "badge": "LP制作",
        "tags": ["LP", "design", "cording - partly"],
        "img": "lp3.webp",
        "alt": "美容医療LP",
        "desc": [
            "美容医療のランディングページ。デザインと部分的コーディングを担当。基本画像貼り付け型のLPページ、CTAボタンやQ&Aなど部分的にコーディングを併用。",
            "ピンクを基調とした可愛いイメージに仕上げ、ターゲット層である学生に向けてポップさを取り入れたデザインに。",
        ],
        "tools": "Illustrator",
        "coding": "HTML / SCSS",
        "duration": "約２週間程度",
        "urls": [],
    },
    {
        "slug": "ays-osaka",
        "title": "あいす・おおさか",
        "badge": "Website制作",
        "tags": ["Website", "design", "cording", "responsive", "wordpress"],
        "img": "ays-osaka.webp",
        "alt": "あいす・おおさか",
        "desc": [
            "一般財団法人 大阪市青少年活動協会「あいす・おおさか」の、協会公式サイトとキャンプ申込み用のイベントサイトの2サイトを制作。デザインとコーディングを担当。",
            "1957年発足の青少年活動団体としての歴史と信頼感を伝える協会公式サイトと、こどもキャンプ・ファミリーキャンプ・アウトドアクラブなど数多くのプログラムを探して申し込みやすく整理したイベントサイトとで、役割の異なる2サイト構成にしました。自然の中でこどもたちがのびのびと活動する写真を中心に、あたたかみと安心感が伝わるデザインに仕上げています。",
        ],
        "tools": "Illustrator / Figma",
        "coding": "HTML / CSS / WordPress",
        "duration": "約１ヶ月程度",
        "url_items": [
            {"label": "協会公式サイト", "url": "https://ays-osaka.jp/"},
            {"label": "イベントサイト（キャンプ申込み）", "url": "https://camp.ays-osaka.jp/"},
        ],
        "extra_images": [
            {"img": "ays-osaka-camp.webp", "alt": "あいす・おおさか イベントサイト"},
        ],
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | AN. design &amp; cording</title>
  <meta name="description" content="{desc0}">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{title} | AN. design &amp; cording">
  <meta property="og:description" content="{desc0}">
  <meta property="og:image" content="../assets/images/{img}">

  <link rel="icon" type="image/svg+xml" href="../assets/icons/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Asap+Condensed:wght@300;400;500;700;800&family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>

  <header class="site-header">
    <div class="container">
      <a href="../index.html" class="brand">
        <span class="material-symbols" aria-hidden="true">important_devices</span>
        <span>AN Design &amp; Cording</span>
      </a>
      <nav class="nav">
        <ul class="nav-links">
          <li><a href="../index.html#about">ABOUT</a></li>
          <li><a href="../index.html#skills">SKILLS</a></li>
          <li><a href="../index.html#works">WORKS</a></li>
        </ul>
        <button class="nav-toggle" aria-label="メニューを開く" aria-expanded="false">
          <span class="material-symbols" aria-hidden="true">menu</span>
        </button>
      </nav>
    </div>
    <a href="../index.html#contact" class="nav-cta">CONTACT</a>
  </header>

  <main>
    <section class="work-hero section">
      <div class="container">
        <a href="../index.html#works" class="work-back reveal">
          <span class="material-symbols" aria-hidden="true" style="font-size:16px;">arrow_back</span>
          WORKS一覧へ戻る
        </a>
        <div class="work-tags reveal">
{tags_html}
        </div>
        <h1 class="work-title reveal">{title}</h1>

        <div class="work-image reveal">
          <img src="../assets/images/{img}" alt="{alt}" loading="eager">
        </div>
{extra_images_html}
        <div class="work-body">
          <div class="work-desc reveal">
{desc_html}
          </div>
          <aside class="work-meta reveal">
            <dl>
              <dt>使用ツール</dt>
              <dd>{tools}{coding_row}</dd>
              <dt>制作時間</dt>
              <dd>{duration}</dd>
{urls_html}
            </dl>
          </aside>
        </div>

        <div class="work-pager reveal">
          <a href="{prev_slug}.html" class="prev">
            <span class="material-symbols" aria-hidden="true" style="font-size:16px;">arrow_back</span>
            {prev_title}
          </a>
          <a href="{next_slug}.html" class="next">
            {next_title}
            <span class="material-symbols" aria-hidden="true" style="font-size:16px;">arrow_forward</span>
          </a>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <a href="../index.html" class="brand">
        <span class="material-symbols" aria-hidden="true">important_devices</span>
        <span>AN Design &amp; Cording</span>
      </a>
      <ul class="footer-links">
        <li><a href="../index.html#about">ABOUT</a></li>
        <li><a href="../index.html#skills">SKILLS</a></li>
        <li><a href="../index.html#works">WORKS</a></li>
        <li><a href="../index.html#contact">CONTACT</a></li>
      </ul>
      <p class="footer-copy">©︎ 2023 AIKO N.</p>
    </div>
  </footer>

  <script src="../js/main.js" defer></script>
</body>
</html>
"""

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def build():
    out_dir = os.path.join(os.path.dirname(__file__), "works")
    n = len(WORKS)
    for i, w in enumerate(WORKS):
        tags_html = "\n".join(f"          <span>{esc(t)}</span>" for t in w["tags"])
        desc_html = "\n".join(f"            <p>{esc(p)}</p>" for p in w["desc"])

        coding_row = f"<br>{esc(w['coding'])}" if w.get("coding") else ""

        url_items = w.get("url_items")
        if url_items:
            items = []
            for it in url_items:
                u = it["url"]
                label = it.get("label")
                text = f"{esc(label)} - {esc(u)}" if label else esc(u)
                items.append(
                    f'              <dd><a class="live-link" href="{esc(u)}" target="_blank" rel="noopener">{text}</a></dd>'
                )
            urls_html = '              <dt>URL</dt>\n' + "\n".join(items)
        else:
            urls = w.get("urls") or []
            if urls:
                label = w.get("url_label")
                items = []
                for j, u in enumerate(urls):
                    text = f"{esc(label)} - {esc(u)}" if (label and j == 0) else esc(u)
                    items.append(
                        f'              <dd><a class="live-link" href="{esc(u)}" target="_blank" rel="noopener">{text}</a></dd>'
                    )
                urls_html = '              <dt>URL</dt>\n' + "\n".join(items)
            else:
                urls_html = ""

        extra_images = w.get("extra_images") or []
        if extra_images:
            imgs_html = "\n".join(
                f'            <img src="../assets/images/{esc(ei["img"])}" alt="{esc(ei.get("alt", ""))}" loading="lazy">'
                for ei in extra_images
            )
            extra_images_html = f'        <div class="work-gallery reveal">\n{imgs_html}\n        </div>\n'
        else:
            extra_images_html = ""

        prev_w = WORKS[(i - 1) % n]
        next_w = WORKS[(i + 1) % n]

        html = TEMPLATE.format(
            title=esc(w["title"]),
            desc0=esc(w["desc"][0]),
            img=w["img"],
            alt=esc(w["alt"]),
            tags_html=tags_html,
            extra_images_html=extra_images_html,
            desc_html=desc_html,
            tools=esc(w["tools"]),
            coding_row=coding_row,
            duration=esc(w["duration"]),
            urls_html=urls_html,
            prev_slug=prev_w["slug"],
            prev_title=esc(prev_w["title"]),
            next_slug=next_w["slug"],
            next_title=esc(next_w["title"]),
        )

        path = os.path.join(out_dir, f"{w['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", path)


if __name__ == "__main__":
    build()
