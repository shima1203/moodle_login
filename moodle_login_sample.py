import requests
import schedule
import time
import datetime
import bs4

# Moodleのログイン情報
username = "2889728404"
password = "t3F8w!RZxmhjUWg"

# ログインURLとコースのURL（適宜変更してください）
login_url = "https://moodle.s.kyushu-u.ac.jp/login/index.php"
course_url = "https://moodle.s.kyushu-u.ac.jp/course/view.php?id=50835"
attendance_form_url = "https://moodle.s.kyushu-u.ac.jp/blocks/autoattend/semiautoattend.php?course=50835&attsid=535970"
attendance_url = "https://moodle.s.kyushu-u.ac.jp/blocks/autoattend/semiautoattend.php"

# ログイン時間
login_times = ["16:41", "16:43", "16:45", "16:50", "16:54", "17:10"]
# login_times = ["18:00", "18:01", "18:02", "18:03", "18:04", "18:05", "18:06", "18:07", "18:08", "18:09", "18:10", "18:11", "18:12", "18:13", "18:14", "18:30", "18:00", "02:30", "03:00" , "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30" , "07:00", "07:30", "08:00", "08:30", "09:00", "09:30" , "10:00", "10:30", "11:00", "11:30", "12:00", "12:30" , "13:00", "13:30", "14:00", "14:30", "15:00", "15:30"]




# セッションオブジェクトを作成
session = requests.Session()
f = open('log_dhizitaru.txt', 'w', encoding='UTF-8')

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
    response1 = session.post(attendance_form_url)
    soup = bs4.BeautifulSoup(response1.text, "html.parser")
    response2 = session.post(attendance_url)
    try:
        course_data = {
                "sesskey" : soup.find('input', attrs={'name':'sesskey'}).get('value'),
                "attsid": soup.find('input', attrs={'name':'attsid'}).get('value'),
                "course": soup.find('input', attrs={'name':'course'}).get('value'),
                "class": soup.find('input', attrs={'name':'class'}).get('value'),
                "submit" : "送信"
            }
        print("course_data : ", course_data)
        response2 = session.post(attendance_url, data=course_data)
    
    
        
    except:
            print("accseeに失敗しました")
            f.write("accessに失敗しました\n")
            
    # アクセスが成功したかを確認
    if response2.status_code == 200:
        print("アクセスに成功しました")
        f.write("アクセスに成功しました\n")
    else:
        print("アクセスに失敗しました")
        f.write("アクセスに失敗しました\n")
    # 出席情報を取得＆ログファイル出力
    soup = bs4.BeautifulSoup(response2.text, "html.parser")
    elems = soup.find('title')
    print(elems)
    
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")
    # elems_ = soup.find_all("div", class_="card-body p-3")
    elems__ = soup.find_all("div", class_="container-fluid d-print-block")
    print(elems__)
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
for login_time in login_times:
    schedule.every().day.at(login_time).do(login_moodle)
    schedule.every().day.at(login_time).do(access_moodle)

while True:
    schedule.run_pending()
    time.sleep(1)
