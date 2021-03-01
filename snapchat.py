import requests, json, time


def check(targ, xsrf):
    url = "https://accounts.snapchat.com/accounts/get_username_suggestions"
    cookies = {
            "xsrf_token": xsrf
    }
    headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar,en;q=0.9,en-US;q=0.8",
    "content-type": "application/x-www-form-urlencoded; charset=utf-8",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36"
    }
    payload = {"requested_username": targ, "xsrf_token": xsrf}
    req = requests.post(url,data=payload,headers=headers,cookies=cookies).json()
    text = str(req)
    if "error_message" not in text:
        print(f"{targ} is available!")
    else:
        print(f"{targ} is not available!")
    main()

    
def main():
    targ = input("name: ")
    qwer = requests.get("https://accounts.snapchat.com/accounts/login")
    xsrf = qwer.cookies.get_dict()["xsrf_token"]
    check(targ, xsrf)

    
if __name__ == "__main__":
    main()

