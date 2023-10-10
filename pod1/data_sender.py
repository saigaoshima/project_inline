import requests

# 動画データを読み込む
with open("sample_movie.mp4", "rb") as file:
    video_data = file.read()

# pod2に動画データを送信
url = "http://pod-2-service:8020/app"
headers = {"Content-Type": "video/mp4"}  # ヘッダーに適切なContent-Typeを設定

response = requests.post(url, data=video_data, headers=headers)

if response.status_code == 200:
    print("動画データの送信が成功しました。")
else:
    print(f"動画データの送信が失敗しました。ステータスコード: {response.status_code}")