# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリ
WORKDIR /tmp/WORK

# ホーム⇒作業ディレクトリへコピー
COPY requirements.txt ${PWD}

# ビルド時に実行するコマンド
RUN pip install -r requirements.txt