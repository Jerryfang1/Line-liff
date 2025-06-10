from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return '這是金玥銀樓會員卡系統'

@app.route('/member')
def member_card():
    user_id = request.args.get('userId', 'Unknown')
    display_name = request.args.get('displayName', '訪客')
    # 模擬從資料庫查詢點數
    points = 100  # 假資料，可改成實際查詢
    return render_template('member_card.html', user_id=user_id, display_name=display_name, points=points)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
