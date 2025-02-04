# sample-tavern-api-testing

## 概要

当リポジトリは、API自動テストツール「Tavern」のテスト結果を Allure Report で、GitHub Pages へ公開するためのサンプルコードです。  
GitHub Actions によって、Tavern による API テスト実施から Allure Report でのレポート公開までの一連の処理を自動で行います。

## 動作確認方法

当リポジトリを fork 後に GitHub Actions を起動頂くことで、動作確認が可能です。

## 仕様

[run_tavern.yaml](.github/workflows/run_tavern.yaml) に定義したワークフローによって実現しています。
- `main` ブランチへのプッシュ時、または手動実行により上記ワークフローが起動します。
- Python は v3.11, Pipenv 使用を前提としています。
- pytest により、`test` ディレクトリ配下のテストコードに対してテストを実行します。
  - ここではサンプルとして、[JSONPlaceholder](https://jsonplaceholder.typicode.com/) の API へのリクエスト・レスポンスを検証しています。
  - Tavern（pytest）実行時に Allure Report を生成できるようにするため、`allure-pytest` プラグインが必要です。
- 以下の外部アクションを使用しています。
  | # | 外部アクション名 | 用途 |
  |---|-----------------|------|
  | 1 |`actions/checkout`|ソースコードのチェックアウト|
  | 2 |`actions/setup-python`|Python 実行環境セットアップ|
  | 3 |`simple-elf/allure-report-action`|テスト結果ファイルを基にした Allure Report 生成|
  | 4 |`peaceiris/actions-gh-pages`|GitHub Pages への Allure Report デプロイ・公開、リポジトリへのレポートファイルのプッシュ|
- GitHub Pages 公開にあたっては `gh-pages` ブランチを使用する前提としています。

## ライセンス

当リポジトリは[MITライセンス](LICENSE)の下で公開されています。
