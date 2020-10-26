import requests
import urllib.parse
import lorem
import json
import re

count_folder = 2 #количество папок
count_courses = 2 #количество курсов
count_lesson = 2 #количество уроков

url = "https://auth.dev01.1iu.ru/api/account/login"

payload = [("consumer", "at"),
           ("login", "anonim1231_at@mail.ru"),
           ("password", "111")]

payload2 = '{"type":"simple"}'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.109 Safari/537.36',
    'Referer': 'https://at.dev01.1iu.ru/login',
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=urllib.parse.urlencode(payload)).json()

headers2 = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
    'Connection': 'keep-alive',
    'Accept-Language': 'en-us,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'https://at.dev01.1iu.ru/panel/courses',
    'Token': response['sid']
}

url_token = "https://at.dev01.1iu.ru/account/auth?token=" + response['sid']
print(url_token)
rez1 = requests.get(url_token, allow_redirects=False, headers=headers2)
headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept-Language': 'en-us,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://at.dev01.1iu.ru/panel/courses',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://at.dev01.1iu.ru',
    'X-Requested-With': 'XMLHttpRequest'
}

cookies1 = {'PHPSESSID': rez1.cookies['PHPSESSID'], '/panel/courses/index/': '%5B%5D'}

for i1 in range(count_folder):
    rez2 = requests.post('https://at.dev01.1iu.ru/panel/courses/groupadd', headers=headers3, data=payload2, cookies=cookies1, allow_redirects=False)
    headers4 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Connection': 'keep-alive',
        'Accept-Language': 'en-us,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://at.dev01.1iu.ru/panel/courses/add?group_id=' + str(rez2.json()["groupId"]),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://at.dev01.1iu.ru',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin'
    }
    #del_folder
    #rez3_del_folder = requests.post('https://at.dev01.1iu.ru/panel/courses/groupdel?group_id=190', headers=headers3, data={}, cookies=cookies1, allow_redirects=False)
    #del_folder

    #create_cours_in_folder
    for i2 in range(count_courses):
        data_create_cours_in_folder = [('group_id',rez2.json()["groupId"]),
                                       ('course[image]',''),
                                       ('file', ''),
                                       ('course[title]', lorem.sentence()),
                                       ('group_id', rez2.json()["groupId"]),
                                       ('course[description]', lorem.sentence()),
                                       ('course[phone]', ''),
                                       ('course[email]', ''),
                                       ('course[skype]', '')]
        data_create_cours_in_folder = urllib.parse.urlencode(data_create_cours_in_folder)

        create_cours_in_folder = requests.post('https://at.dev01.1iu.ru/panel/courses/edit', headers=headers4,
                                               data=data_create_cours_in_folder, cookies=cookies1, allow_redirects=True)
        new_course = re.findall('(?<=course_id=).*?(?=&)', create_cours_in_folder.url)
        print(new_course[0], create_cours_in_folder.json()[0]["id"])

        #add_student_data = '{"students":{"1":{"email":"e152f313f490@mail.ru","name":"e152f313f490","surname":"e152f313f490","phone":""}},"tags":[],"courses":[{"id":28630,"benefitId":0}],"plan":null,"language":"","lesson":686,"curator":0,"studentsGroup":0,"dateOfBlock":null,"reinvite":false}'
        #add_student = requests.post('https://at.dev01.1iu.ru/api/students/add?group_id=193', headers=headers4,
        #                                       data=add_student_data, cookies=cookies1, allow_redirects=False)

        for i3 in range(count_lesson):

            data_add_lesson_teory_first = 'course_id=' + new_course[0] + '&theme_id=' + str(create_cours_in_folder.json()[0]["id"]) + '&lesson_id=undefined&type=theory'
            add_lesson_teory_first = requests.post('https://at.dev01.1iu.ru/panel/lessons/add', headers=headers4, data=data_add_lesson_teory_first, cookies=cookies1, allow_redirects=False)
            add_lesson_teory_first_n = str(add_lesson_teory_first.headers['Location'])
            print(add_lesson_teory_first_n)

            add_lesson_teory_data = 'course_id=' + new_course[0] + '&theme_id=' + str(create_cours_in_folder.json()[0]["id"]) + '&lesson_id=' + add_lesson_teory_first_n.split("=")[-1] + '&lesson%5Bphoto%5D=&file=&lesson%5Btitle%5D=' + lorem.sentence() + '&lesson%5Bdescription%5D=' + lorem.paragraph() + '&lesson%5Bsettings%5D%5Btheory%5D%5Bhas_settings%5D=yes&lesson%5Bsettings%5D%5Btheory%5D%5Bchat_room%5D=no&lesson%5Bsettings%5D%5Btheory%5D%5Bhide_online%5D=no'
            add_lesson_teory = requests.post('https://at.dev01.1iu.ru/panel/lessons/edit', headers=headers4, data=add_lesson_teory_data, cookies=cookies1, allow_redirects=True)