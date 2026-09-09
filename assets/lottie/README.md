# ABOUTセクションのアニメーション

ABOUT セクション右側のイラストアニメーション用フォルダです。

現在 `about.json`（LottieFilesの「Designer」アニメーション、通常のLottie JSON形式）を
設置済みで、`index.html` にすでに組み込まれています。

## 仕組み

- 再生には [`@lottiefiles/dotlottie-wc`](https://www.npmjs.com/package/@lottiefiles/dotlottie-wc)
  という Web Component を使っています（`index.html` の `<script type="module">` でCDN読み込み済み）。
  このコンポーネントは通常のLottie JSONにも、dotLottie（`.lottie`）形式にもそのまま対応しています。
- `index.html` の ABOUT セクション内、`<div class="about-illustration">` の中に以下のように配置しています。

```html
<dotlottie-wc
  src="assets/lottie/about.json"
  autoplay
  loop
  style="width:100%;height:100%;"
></dotlottie-wc>
```

## 差し替え方法

別のアニメーションに差し替えたい場合は、

1. 新しい `.json`（または `.lottie`）ファイルをこのフォルダに置く
2. `index.html` 内の `<dotlottie-wc src="assets/lottie/about.json" ...>` の `src` を新しいファイル名に変更する

だけでOKです。

## 注意

- ファイルサイズが大きいアニメーション（複雑なベクターや多数のキーフレーム）は、ページの表示速度に影響することがあります。
- `dotlottie-wc` はCDN（jsDelivr）から読み込んでいるため、バージョンを固定しています
  （`@lottiefiles/dotlottie-wc@0.9.28`）。将来的に最新版へ更新したい場合は、
  [npmのバージョン一覧](https://www.npmjs.com/package/@lottiefiles/dotlottie-wc?activeTab=versions) を確認して
  `index.html` の `<script>` タグのバージョン番号を書き換えてください。
