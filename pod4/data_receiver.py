from flask import Flask, request

app = Flask(__name__)

@app.route("/receive4", methods=["POST"])
def receive_video():
    try:
        video_data = request.data  # 動画データを受信

        # ここで動画データを処理するか、保存するなどの操作を行うことができます

        # 受信が成功したことを知らせるレスポンス
        return "Video data received successfully", 200

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)