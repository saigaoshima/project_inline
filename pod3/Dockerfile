# ベースイメージを指定
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 送信元アプリケーションの依存パッケージをインストール
RUN pip install flask ffmpeg requests

# アプリケーションコードをコンテナ内にコピー
COPY last_half_reduction_processing.py /app

# コンテナを起動した際に実行するコマンドを指定
CMD ["python", "last_half_reduction_processing.py"]