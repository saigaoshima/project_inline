# ベースイメージを指定
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# データ処理アプリケーションの依存パッケージをインストール
RUN pip install requests

# アプリケーションコードをコンテナ内にコピー
COPY data_sender.py /app
COPY sample_movie.mp4 /app

# コンテナを起動した際に実行するコマンドを指定
CMD ["python", "data_sender.py"]