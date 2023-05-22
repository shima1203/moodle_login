# moodle_login

### 初期設定

・username : ユーザー名

・password : パスワード

・login_url : ログイン画面のURL(IDとパスワードを入力する画面)

・course_url : コース画面のURL(出欠登録する科目の画面)

・login_times : ログインする時間(好きな回数分だけリストに追加)




### 実行

nohup python3 moodle_login.py &

(サーバーでsshから実行する場合はタイムアウトしてプロセスが終了してしまうため、バックグラウンド実行が必要。終了はkillコマンドで。)
