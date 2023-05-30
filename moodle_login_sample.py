import requests
import schedule
import time
import datetime
import bs4

# Moodleのログイン情報
username = "ユーザー名"
password = "パスワード"

# ログインURLとコースのURL（適宜変更してください）
# login_url : ログインページのURL
# login_info : [コースページのURL, 出席ボタンのURL, 自動出欠ページのURL, ログイン時間, 曜日, ログファイルの名前]
login_url = "ログインページのURL"
login_info= [["コースページのURL", "出席ボタンのURL", "自動出欠ページのURL", "ログイン時間", "曜日", "ログファイルの名前"]]






def login_moodle(info):
    # セッションオブジェクトを作成
    session = requests.Session()
    
    # ログファイルを作成
    f = open(info[5], 'w', encoding='UTF-8')
    
    print(datetime.datetime.now())
    f.write(str(datetime.datetime.now()))
    f.write("\n")
    
    # ログイントークンを取得
    response_login_page = session.post(login_url)
    soup_login = bs4.BeautifulSoup(response_login_page.text, "html.parser")
    
    # moodleにログイン
    try:
        login_data = {
            "logintoken" : soup_login.find('input', attrs={'name':'logintoken'}).get('value'),
            "username": username,
            "password": password
        }
        # ログインリクエストを送信
        response_login = session.post(login_url, data=login_data)
        soup_login = bs4.BeautifulSoup(response_login.text, "html.parser")
        elems = soup_login.find('title')
        print(elems)
        f.write(elems)
        f.write("\n")
        
    except:
        print("・ログインに失敗したか、既にログインしています")
        f.write("・ログインに失敗したか、既にログインしています\n")
    # ログインが成功したかを確認
    if response_login.status_code == 200 and "ログインに失敗しました" not in response_login.text:
        print("・ログインに成功しました")
        f.write("・ログインに成功しました\n")
    else:
        print("・ログインに失敗しました")
        f.write("・ログインに失敗しました\n")
    

    # コースページにアクセス
    course_url = info[0]
    attendance_button_url = info[1]
    attendance_file_url = info[2]
    
    try:
        response_course = session.get(course_url)
    except:
        print("・コースページへのアクセスに失敗しました")
        f.write("・コースページへのアクセスに失敗しました\n")
    # アクセスが成功したかを確認
    if response_course.status_code == 200:
        print("・コースページへのアクセスに成功しました")
        f.write("・コースページへのアクセスに成功しました\n")
    # 自動出欠ファイルにアクセス
    try:
        response_attendance_file = session.get(course_url)
        if(attendance_button_url != ""):
            responce_attendance_button = session.get(attendance_button_url)
            soup_attendance_button = bs4.BeautifulSoup(responce_attendance_button.text, "html.parser")
            course_data = {
                    "sesskey" : soup_attendance_button.find('input', attrs={'name':'sesskey'}).get('value'),
                    "attsid": soup_attendance_button.find('input', attrs={'name':'attsid'}).get('value'),
                    "course": soup_attendance_button.find('input', attrs={'name':'course'}).get('value'),
                    "class": soup_attendance_button.find('input', attrs={'name':'class'}).get('value'),
                    "submit" : "送信"
                }
            response_attendance_file = session.post(attendance_file_url, data=course_data)
    except:
        print("・自動出欠に失敗しました")
        f.write("・自動出欠に失敗しました\n")
    # アクセスが成功したかを確認
    if response_attendance_file.status_code == 200:
        print("・自動出欠に成功しました")
        f.write("・自動出欠に成功しました\n")

    # 出席情報を取得＆ログファイル出力
    response_course = session.get(course_url)
    soup_course = bs4.BeautifulSoup(response_course.text, "html.parser")
    elems = soup_course.find('title')
    print(elems)
    
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")
    # elems_ = soup_course.select("div.container-fluid d-print-block")
    elems__ = soup_course.find_all("div", class_="card-text content mt-3")
    print(elems__)
    # print(elems_)
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")
    
    f.write("--------------------------------------------------------------------\n")
    f.write("--------------------------------------------------------------------\n")
    f.write(str(elems__))
    f.write("\n")
    f.write("--------------------------------------------------------------------\n")
    f.write("--------------------------------------------------------------------\n")
    
    # ログアウト
    logout_url = "https://moodle.s.kyushu-u.ac.jp/login/logout.php"
    session.get(logout_url)

# ログインとアクセスをスケジュール
for login_info_ in login_info:
    login_times = login_info_[3]
    day = login_info_[4]
    for login_time in login_times:
        if day == "monday":
            schedule.every().monday.at(login_time).do(login_moodle, login_info_)
        elif day == "tuesday":
            schedule.every().tuesday.at(login_time).do(login_moodle, login_info_)
        elif day == "wednesday":
            schedule.every().wednesday.at(login_time).do(login_moodle, login_info_)
        elif day == "thursday":
            schedule.every().thursday.at(login_time).do(login_moodle, login_info_)
        elif day == "friday":
            schedule.every().friday.at(login_time).do(login_moodle, login_info_)

while True:
    schedule.run_pending()
    time.sleep(1)
