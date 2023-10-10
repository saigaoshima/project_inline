# ベースイメージを指定
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 送信元アプリケーションの依存パッケージをインストール
RUN pip install requests flask

# アプリケーションコードをコンテナ内にコピー
COPY data_receiver.py /app

# コンテナを起動した際に実行するコマンドを指定
CMD ["python", "data_receiver.py"]