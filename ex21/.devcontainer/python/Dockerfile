# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリ
WORKDIR /tmp/work

# requirements.txtファイルを作業ディレクトリにコピー
COPY requirements.txt ${PWD}

# requirements.txtを「build」時にインストール
RUN pip install -r requirements.txt