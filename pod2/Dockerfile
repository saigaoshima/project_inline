# ベースイメージを指定
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 受信アプリケーションの依存パッケージをインストール
RUN pip install flask ffmpeg requests

# アプリケーションコードをコンテナ内にコピー
COPY first_half_reduction_processing.py /app

# コンテナを起動した際に実行するコマンドを指定
CMD ["python", "first_half_reduction_processing.py"]