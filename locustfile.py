import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/workforce/planner/board")
        self.client.get("/lead")
        self.client.get("/workforce/project")
        self.client.get("/workforce/vacancy")
        self.client.get("/workforce/assignment")
        self.client.get("/workforce/people")
        self.client.get("/report")



   # @task(3)
   # def view_items(self):
   #     for item_id in range(10):
   #         self.client.get(f"/item?id={item_id}", name="/lead")
   #         time.sleep(1)

    def on_start(self):
        logindata = {
            '__EVENTTARGET': 'ctl00$cp_master$lbtn_login',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': 'oPh5Suw1W/T9kExXrhuupoK1d5diY9DafF/2tq9WNHJtQLD9F3cm6ItVwQPVl2HXLyDFevW6hvIHNHrbWFxOoAofjbxJ80njIz7Vj19x9WU=',
            '__VIEWSTATEGENERATOR': 'B16483BC',
            '__EVENTVALIDATION': 'WYgurkMgMSSaOLcqjgTael429XT24eAd3cwX2BqXq9ijkH4WxZGYsCN5w+g3iivnHF5S1vCb/3MsLwFgNgoMPe8ywcK9wXYGyKayC/NM6ZPPzl2LCXpAhD5Tm3eDwSMHTFf+GKkpVCi0xBR4U1NYEvdhkDTeiU60Kju7VI3MHfdv6/mAA6jWJgSvsOMWXIa9',
            'ctl00$cp_master$txt_username': 'john.raymond',
            'ctl00$cp_master$txt_password': 'vericol1',
        }

        resp = self.client.post("/security/login/", data=logindata)
        print(resp.status_code)
        print(resp.url)
