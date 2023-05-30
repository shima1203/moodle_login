# moodle_login

### 初期設定

login_url = "ログインページのURL"

login_info= [["コースページのURL", "出席ボタンのURL", "自動出欠ページのURL", "ログイン時間", "曜日", "ログファイルの名前"]]

※login_infoの詳細は下を参照



### 実行

nohup python3 moodle_login.py &

(サーバーでsshから実行する場合はタイムアウトしてプロセスが終了してしまうため、バックグラウンド実行が必要。終了はkillコマンドで。)


### 終了

kill 1290847 (実行時に表示される番号がプロセスID)

![image](https://github.com/shima1203/moodle_login/assets/107593704/b7d6cde1-7b09-4de3-a3ce-364e783749e5)



ps aux　(実行中のタスク一覧)




### login_info 詳細

(例)

    login_info= [["https://moodle.s."YOUR Univ.".ac.jp/course/view.php?id=50835", "https://moodle.s."YOUR Univ.".ac.jp/blocks/autoattend/semiautoattend.php?course=50835&attsid=535970", "https://moodle.s."YOUR Univ.".ac.jp/blocks/autoattend/semiautoattend.php", ["16:41", "16:43", "16:45", "16:50", "16:54", "17:10"], "tuesday", 'log_dhizitaru.txt'],

            　　["https://moodle.s."YOUR Univ.".ac.jp/course/view.php?id=50807", "", "", ["10:31", "10:32", "10:33", "10:34", "10:35", "10:44"], "thursday", 'log_jouhouriron.txt'],
            
            　　["https://moodle.s."YOUR Univ.".ac.jp/course/view.php?id=51011", "", "", ["13:00", "13:01", "13:02", "13:03", "13:04", "13:05"], "tuesday", 'log_kakuritu.txt'],
            
            　　]
    ※コースページにアクセスするだけでよい場合は残りの2つは""で良い
              
![image](https://github.com/shima1203/moodle_login/assets/107593704/25025002-edfc-4945-b8ed-496b0910dbf3)
