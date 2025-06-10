from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

# 假會員資料庫（記憶體）
mock_member_db = {
    "U1234567890": {"display_name": "小明", "points": 120},
    "U0987654321": {"display_name": "小華", "points": 80},
}

@app.route('/')
def home():
    return '金玥銀樓會員卡系統啟動成功'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user_id = data.get('userId')
    display_name = data.get('displayName')
    if user_id and user_id not in mock_member_db:
        mock_member_db[user_id] = {"display_name": display_name, "points": 0}
    return jsonify({"status": "ok"})

@app.route('/api/member')
def api_member():
    user_id = request.args.get('userId')
    member_data = mock_member_db.get(user_id, {"display_name": "訪客", "points": 0})
    return jsonify(member_data)

@app.route('/member')
def member_page():
    return render_template('member_card.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
