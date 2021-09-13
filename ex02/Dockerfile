# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリを変更
WORKDIR /tmp/mydir

# ファイルのコピー
# ・ホストからファイルをコンテナ内にコピー
# ・コピー先：作業ディレクトリ
COPY requirements.txt ${pwd}

# RUN
# ・docker image buildを行う際に実行するコマンドを記述
# ・モジュールのインストールなど
# pythonのパッケージをインストール
RUN pip install -r requirements.txt

# ”Dockerfile内でのみ使える”一時変数の定義
# ・使用する際は「$ 変数名」
# ・一時変数の値は「build」時に「build-arg」で指定
ARG wdir

# 作業ディレクトリを変更
WORKDIR $wdir