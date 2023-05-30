# moodle_login

### 初期設定

login_url = "ログインページのURL"

login_info= [["コースページのURL", "出席ボタンのURL", "自動出欠ファイルのURL", "ログイン時間", "曜日", "ログファイルの名前"]]





### 実行

nohup python3 moodle_login.py &

(サーバーでsshから実行する場合はタイムアウトしてプロセスが終了してしまうため、バックグラウンド実行が必要。終了はkillコマンドで。)

### 終了

kill 1290847 (実行時に表示される番号がプロセスID)

![image](https://github.com/shima1203/moodle_login/assets/107593704/b7d6cde1-7b09-4de3-a3ce-364e783749e5)



ps aux　(実行中のタスク一覧)
