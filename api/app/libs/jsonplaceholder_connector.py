from flask import current_app, g

# from app.libs.analysers import Reporter
# from app.libs.util import get_timestamp, this_moment, strip_scheme
import requests


class Jsonplaceholder_connector(object):
    def __init__(self):
        self.baseurl = current_app.config["JSP_FQDN"] or "https://jsonplaceholder.typicode.com"
        self.timeout = int(current_app.config.get("JSP_CONNECT_TIMEOUT", 5))

    def get_users(self):
        payload = {}
        status, response = self.invoke(
            uri="/users",
            api_name="get_users",
            method="get",
            params=payload)
        # TODO: Add json schema validation source payload
        return response if status==200 else None

    def get_posts(self):
        payload = {}
        status, response = self.invoke(
            uri="/posts",
            api_name="get_posts",
            method="get",
            params=payload)
        # TODO: Add json schema validation source payload
        return response if status==200 else None
    
    def get_todos(self):
        payload = {}
        status, response = self.invoke(
            uri="/todos",
            api_name="get_todos",
            method="get",
            params=payload)
        # TODO: Add json schema validation source payload
        return response if status==200 else None

    def get_comments(self):
        payload = {}
        status, response = self.invoke(
            uri="/comments",
            api_name="get_comments",
            method="get",
            params=payload)
        # TODO: Add json schema validation source payload
        return response if status==200 else None

    def invoke(self, uri, api_name, method="post", params={},
                   body={}, header={}):
        url = "{base}{uri}".format(base=self.baseurl, uri=uri)
        header["Content-Type"] = "application/json;charset=utf-8"
        
        if method.upper()=="GET":
            body=None
        try:
            r = requests.request(
                method=method.upper(),
                url=url,
                json=body,
                params=params,
                headers=header,
                timeout=self.timeout)

            r.raise_for_status()
            response = r.json()
            r.close()
            return r.status_code, response

        except requests.ConnectionError as e:
            err_msg = "ConnectionError"
            return -1, err_msg

        except requests.Timeout as e:
            err_msg = "TimeoutError"
            return -1, err_msg
        except requests.HTTPError as e:
            return r.status_code,r.text
        except Exception as e:
            err_msg = "Unknown Exception: {}".format(str(e))
            return -1, err_msg
             