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

### 終了

kill 1290847 (実行時に表示される番号がプロセスID)

![image](https://github.com/shima1203/moodle_login/assets/107593704/b7d6cde1-7b09-4de3-a3ce-364e783749e5)



ps aux　(実行中のタスク一覧)
