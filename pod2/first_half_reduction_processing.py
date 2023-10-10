from flask import Flask, request, jsonify
import subprocess
import os
import tempfile

app = Flask(__name__)

@app.route("/app", methods=["POST"])
def receive_video():
    try:
        video_data = request.data  # 動画データを受信

        # 一意のファイル名を生成
        input_file_path = os.path.join(tempfile.gettempdir(), "input.mp4")
        output_file_path = os.path.join(tempfile.gettempdir(), "output.mp4")

        # 動画データをファイルに保存
        with open(input_file_path, "wb") as file:
            file.write(video_data)

        # FFmpegを使用して最初の10秒を削除し、新しい動画ファイルを作成
        subprocess.run(["ffmpeg", "-ss", "10", "-i", input_file_path, "-c:v", "copy", "-c:a", "copy", output_file_path])

        # 削減後の動画をバイト列に変換
        with open(output_file_path, "rb") as file:
            processed_video_data = file.read()

        # ファイルを削除
        os.remove(input_file_path)
        os.remove(output_file_path)
        print("受信完了")

        # Pod3に動画データを送信
        #pod3_ip = "pod3-ip"  # pod3のIPアドレスを設定
        #response = requests.post(f"http://{pod3_ip}:8080/receive3", data=processed_video_data)

        #if response.status_code == 200:
        #    return jsonify({"message": "OK", "video_data": processed_video_data})
        #else:
        #    return jsonify({"error": "Failed to send data to Pod3"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8020)