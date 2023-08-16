import random
import time
import requests

class ProxyManager:
    def __init__(self, proxy_list):
        self.proxy_list = proxy_list
        self.current_proxy = random.choice(proxy_list)
        self.last_rotation_time = time.time()

    def rotate_proxy(self):
        # Rotate proxy if 10 minutes have passed
        if time.time() - self.last_rotation_time >= 600:
            self.current_proxy = random.choice(self.proxy_list)
            self.last_rotation_time = time.time()

    def proxy_request(self, url):
        self.rotate_proxy()
        print(f"********* PROXY", self.current_proxy)
        proxies = {
            "http": self.current_proxy,
            "https": self.current_proxy
        }

        # Proxy the request through the selected proxy server
        response = requests.get(url, proxies=proxies)
        return response.content.strip(), response.status_code
