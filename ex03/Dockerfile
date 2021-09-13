# ベースイメージの取得
FROM ubuntu:20.04

# Nginxのインストール
# ・apt-get：Ubuntuのパッケージ管理システム
# 　※ Dockerfileでは「apt」ではなく「apt-get」を使用
# ・apt-get update：インストール可能なパッケージ一覧を更新
# 　※apt-get installの前に実行
RUN apt-get update && apt-get install -y \
    nginx\
    tzdata\
&& rm -rf /var/lib/apt/lists/*


# 環境変数の定義
# ・ARGと異なり「build」時に値を指定できない
# ・「${}」のように使用
# タイムゾーンを設定する環境変数
ENV TZ=Asia/Tokyo

# ポートの指定
# ・コンテナのアプリで使用するポート番号を指定
EXPOSE 80

# ファイルのコピー
COPY src/index.html /var/www/html

# CMD
# ・「docker run」の際に実行するコマンドを記述
# Nginxの起動
CMD ["nginx", "-g", "daemon off;"]