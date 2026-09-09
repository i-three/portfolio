# AN. design & cording — Portfolio (ソースコード版)

STUDIO で作成していたポートフォリオ（https://an-designweb.studio.site/）を、
素の HTML / CSS / JavaScript に移行したものです。ビルドツール不要、VSCode で直接編集して
そのまま GitHub Pages 等にデプロイできます。

## フォルダ構成

```
index.html            トップページ（ABOUT / SKILLS / WORKS / CONTACT）
works/                作品詳細ページ（12件）
css/style.css         全ページ共通スタイル
js/main.js            モバイルメニュー・スクロール演出・お問い合わせフォーム制御
assets/images/        作品画像・トップの写真
assets/icons/         favicon
generate_works.py     works/*.html を再生成するためのビルド補助スクリプト（任意・必須ではありません）
```

## ローカルで確認する

ビルド不要ですが、`fetch` を使わないシンプルな構成なので `index.html` を直接ブラウザで開くだけで
ほぼ確認できます。ただし相対パスの挙動を本番に近づけたい場合は、フォルダ直下で簡易サーバーを立てるのがおすすめです。

```bash
# Python がある場合
python3 -m http.server 8000
# → http://localhost:8000 で確認

# Node がある場合
npx serve .
```

## 内容を編集する

- テキストや文言：各 `.html` ファイルを直接編集
- 色・フォント・余白などのデザイン：`css/style.css` の先頭 `:root` にある変数（`--color-accent` など）を編集
- 作品を追加・削除する：
  1. `assets/images/` に画像を追加
  2. `index.html` の WORKS グリッドにカードを1つ追加（既存のカードをコピーして書き換えるのが簡単です）
  3. `works/` に詳細ページを1つ追加（既存の `.html` をコピーして書き換え）
  - 12件分をまとめて管理したい場合は `generate_works.py` の `WORKS` リストに項目を追加して
    `python3 generate_works.py` を実行すると `works/*.html` が一括生成されます（使わなくても問題ありません）

## ABOUTセクションのイラスト（Lottieアニメーション）について

ABOUT セクション右側のイラストアニメーションは、元サイトで使われているアセット
（`assets/lottie/about.json`）を設置済みです。再生には
[`@lottiefiles/dotlottie-wc`](https://www.npmjs.com/package/@lottiefiles/dotlottie-wc) という
Web Component を使っており、`index.html` にCDN読み込み・埋め込みとも設定済みなので、
追加の作業なしでそのまま表示されます。差し替え方法など詳しくは `assets/lottie/README.md` を参照してください。

## お問い合わせフォームについて

GitHub Pages は静的ホスティングのため、PHP 等のサーバー処理は動きません。現状の実装は次のようになっています。

- `js/main.js` の `FORM_ENDPOINT` が空の間は、送信ボタンを押すとメールソフトが起動し、
  入力内容が本文にセットされた状態で `aiko.nakamura.pj@gmail.com` 宛のメールを作成します。
- [Formspree](https://formspree.io/) や [Getform](https://getform.io/) などのフォーム送信サービスに
  無料登録し、発行された送信先 URL を `FORM_ENDPOINT` に設定すると、訪問者側でメールソフトを開かずに
  そのまま送信できるようになります。

## 移行にあたっての注意点（元サイトの状態について）

移行時に元サイト（STUDIO版）を確認したところ、以下の作品ページで詳細ページ用の大きい画像が
読み込めなくなっていました（トップの WORKS 一覧に出ているサムネイル画像は正常だったため、
そちらを詳細ページにも流用しています）。

- Website制作×3（website1 / website2 / website3）
- Portfolio Site
- LOGO制作
- StandbyScreen

また、`lp1` の「クリニックのbefore/after的な画像」や `lp2` の実制作画面、`lp4` の `sumida-feel.com`、
`lp6` の `fujiokakoumuten.com` のキャプチャ画像など、外部の個人サーバー（xs809375.xsrv.jp など）に
置かれていた画像はこの移行作業時点でサーバーへの接続自体ができず、取得できませんでした。
のちほど元データや撮り直しのスクリーンショットをお持ちでしたら、`assets/images/` に追加のうえ
該当ページの `<img>` を差し替えてください。

トップページの黄色い壁の写真は STUDIO 版のテンプレート由来の Unsplash 素材（フリー素材）です。
ご自身の写真や制作実績のキャプチャに差し替えると、より「らしい」トップページになります。

## GitHub Pages へのデプロイ

1. このフォルダの中身を GitHub リポジトリのルート（または `docs/` フォルダ）にコミット
2. リポジトリの Settings → Pages で公開元のブランチ／フォルダを指定
3. 数分後に `https://<ユーザー名>.github.io/<リポジトリ名>/` で公開されます

独自ドメインを使う場合は、リポジトリ直下に `CNAME` ファイルを追加してください。
