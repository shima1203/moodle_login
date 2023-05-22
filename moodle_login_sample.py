import requests
import schedule
import time
import datetime
import bs4

# Moodleのログイン情報
username = "ユーザー名"
password = "パスワード"

# ログインURLとコースのURL（適宜変更してください）
login_url = "https://moodle.s.kyushu-u.ac.jp/login/index.php"
course_url = "https://moodle.s.kyushu-u.ac.jp/course/view.php?id=50835"

# ログイン時間
login_times = ["15:52", "15:53", "15:54", "15:55", "15:56"]






# ログインセッションを確立するためのセッションオブジェクトを作成
session = requests.Session()
f = open('log.txt', 'w', encoding='UTF-8')

def login_moodle():
    print(datetime.datetime.now())
    f.write(str(datetime.datetime.now()))
    f.write("\n")
    # ログイン情報をPOSTデータに設定
    response = session.post(login_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    
    try:
        login_data = {
            "logintoken" : soup.find('input', attrs={'name':'logintoken'}).get('value'),
            "username": username,
            "password": password
        }
        # ログインリクエストを送信
        response = session.post(login_url, data=login_data)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        elems = soup.find('title')
        print(elems)
        
    except:
        print("ログインに失敗しました")
        f.write("ログインに失敗しました\n")

    # ログインが成功したかを確認
    if response.status_code == 200 and "ログインに失敗しました" not in response.text:
        print("ログインに成功しました")
        f.write("ログインに成功しました\n")
    else:
        print("ログインに失敗しました")
        f.write("ログインに失敗しました\n")
    

def access_moodle():
    # コースページにアクセス
    response = session.get(course_url)
    # アクセスが成功したかを確認
    if response.status_code == 200:
        print("アクセスに成功しました")
        f.write("アクセスに成功しました\n")
    else:
        print("アクセスに失敗しました")
        f.write("アクセスに失敗しました\n")

    # 必要な処理を実行（例: ページの解析や特定の操作）
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    elems = soup.find('title')
    print(elems)
    
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")
    # elems_ = soup.find_all("div", class_="card-body p-3")
    elems__ = soup.find_all("div", class_="card-text content mt-3")
    print(elems__)
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")
    
    f.write("--------------------------------------------------------------------\n")
    f.write("--------------------------------------------------------------------\n")
    f.write(str(elems__))
    f.write("\n")
    f.write("--------------------------------------------------------------------\n")
    f.write("--------------------------------------------------------------------\n")
    
    # ログアウト（任意のタイミングでログアウトする場合）
    logout_url = "https://moodle.s.kyushu-u.ac.jp/login/logout.php"
    session.get(logout_url)

# ログインとアクセスをスケジュール
for login_time in login_times:
    schedule.every().day.at(login_time).do(login_moodle)
    schedule.every().day.at(login_time).do(access_moodle)

while True:
    schedule.run_pending()
    time.sleep(1)
