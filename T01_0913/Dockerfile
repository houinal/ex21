# ベースイメージ
FROM python:3.9-slim

# タイムゾーンを日本に設定
RUN apt-get update \
    && apt-get install -y tzdata \
    && rm -rf /var/lib/apt/lists/*

# モジュールのインストール
WORKDIR /tmp/work
COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt

# 環境変数の定義
ENV TZ = Asia/Tokyo
ENV USER user

# 一般権限ユーザーの追加
RUN useradd -m ${USER} --uid 1000
RUN gpasswd -a ${USER} sudo
RUN echo "${USER}:password" | chpasswd

# ユーザーの切り替え
USER ${USER}