import time
import requests
from urllib.parse import urljoin

REGIONS = {
    'AU1': 'app.au1.sysdig.com',
    'EU1': 'eu1.app.sysdig.com',
    'US1': 'secure.sysdig.com',
    'US2': 'us2.app.sysdig.com',
    'US3': 'app.us3.sysdig.com',
    'US4': 'app.us4.sysdig.com',
}

class SDCAdmin():
    def __init__(self, region) -> None:
        self.baseurl = REGIONS[region]
        self.session = requests.session()
        with open('sdc-admin-token','r') as f:
            self.sdc_admin_token = f.read()

    def _send(self, method, **kwargs):
        if 'url' not in kwargs.keys():
            if 'path' not in kwargs.keys():
                raise RuntimeError("either path or url must be specified")
            else:
                url = urljoin(f"https://{self.baseurl}", kwargs.pop('path'))

        else:
            url = kwargs['url']

        # Define the headers
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.sdc_admin_token
        }

        # Send the request
        response = self.session.request(method, url, headers=headers)
        return response

    def get_customers(self, platform=False, secure=False):
        querystring = {
            "platform": platform,
            "offset": secure,
        }

        response = self._send("GET", path="/api/admin/customers/activeCustomerIds", params=querystring)
        return response.json()

    def get_customer_users(self, customer_id):
        status = None
        while status is None or status != 200:
            response = self._send("GET", path=f"/api/admin/customers/{customer_id}/users")
            status = response.status_code
            if status != 200:
                time.sleep(1)

        return response.json()

    def get_user_tokens(self, username):
        status = None
        while status is None or status != 200:
            response = self._send("GET", path=f"/api/admin/users/{username}/tokens")
            status = response.status_code
            if status != 200:
                time.sleep(1)

        return response.json()
