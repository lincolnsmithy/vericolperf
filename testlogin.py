import requests

cookies = {
    'ASP.NET_SessionId': 'wubg0tohoxnbnrbauwclyqmk',
    '/lead/insert/': '/lead/Default.aspx',
}

headers = {
    'authority': 'demo.vericol.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ASP.NET_SessionId=wubg0tohoxnbnrbauwclyqmk; /lead/insert/=/lead/Default.aspx',
    'origin': 'https://demo.vericol.com',
    'pragma': 'akamai-x-cache-on,akamai-x-cache-remote-on,akamai-x-check-cacheable,akamai-x-get-cache-key,akamai-x-get-true-cache-key,akamai-x-get-extracted-values,akamai-x-get-request-id,akamai-x-get-client-ip,akamai-x-feo-trace,akamai-x-feo-state,akamai-x-extension-on',
    'referer': 'https://demo.vericol.com/security/login/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

data = {
    '__EVENTTARGET': 'ctl00$cp_master$lbtn_login',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': 'oPh5Suw1W/T9kExXrhuupoK1d5diY9DafF/2tq9WNHJtQLD9F3cm6ItVwQPVl2HXLyDFevW6hvIHNHrbWFxOoAofjbxJ80njIz7Vj19x9WU=',
    '__VIEWSTATEGENERATOR': 'B16483BC',
    '__EVENTVALIDATION': 'WYgurkMgMSSaOLcqjgTael429XT24eAd3cwX2BqXq9ijkH4WxZGYsCN5w+g3iivnHF5S1vCb/3MsLwFgNgoMPe8ywcK9wXYGyKayC/NM6ZPPzl2LCXpAhD5Tm3eDwSMHTFf+GKkpVCi0xBR4U1NYEvdhkDTeiU60Kju7VI3MHfdv6/mAA6jWJgSvsOMWXIa9',
    'ctl00$cp_master$txt_username': 'john.raymond',
    'ctl00$cp_master$txt_password': 'vericol1',
}

response = requests.post('https://demo.vericol.com/security/login/', cookies=cookies, headers=headers, data=data)
print(response.status_code)
print(response.content)
print(response.url)