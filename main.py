import requests
from requests.structures import CaseInsensitiveDict

def save_toke_to_file(str_result):
    f = open("result.txt", "a")
    f.write(str_result + '\n')
    f.close()

url = "https://www.clubhouseapi.com/api/get_feed"
headers = {
    'CH-Languages': 'en-US',
    'CH-Locale': 'en_US',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'CH-AppBuild': '305',
    'CH-AppVersion': '1.0.9',
    'CH-UserID': '1387526936',
    'User-Agent': 'clubhouse/305 (iPhone; iOS 14.4; Scale/2.00)',
    'Connection': 'close',
    'Content-Type': 'application/json; charset=utf-8',
    'Authorization': 'Token YourToken'
}
resp = requests.post(url, headers=headers)
print('status_code=' + str(resp.status_code))
print(resp.content)
save_toke_to_file(str(resp.content))
result = resp.json()
success_status = str(result["success"])
if success_status == 'True':
    user_id = (str(result["user_profile"]["user_id"]))
    print('user_id=' + user_id)
else:
    print('error cant find user_id')
