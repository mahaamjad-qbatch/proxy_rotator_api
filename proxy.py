import time
import requests
import threading

class ProxyManager:
    def __init__(self, proxy_list):
        self.proxy_list = proxy_list
        self.current_proxy_index = 0
        self.lock = threading.Lock()
        self.rotation_interval = 600

        self.rotation_thread = threading.Thread(target=self.rotate_proxies)
        self.rotation_thread.daemon = True
        self.rotation_thread.start()

    def get_current_proxy(self):
        with self.lock:
            return self.proxy_list[self.current_proxy_index]

    def rotate_proxies(self):
        while True:
            time.sleep(self.rotation_interval)
            with self.lock:
                self.current_proxy_index = (self.current_proxy_index + 1) % len(self.proxy_list)

    def proxy_request(self, url):
        proxy = self.get_current_proxy()
        print(f"********* PROXY", proxy)
        proxies = {
            "http": proxy,
            "https": proxy
        }

        # Proxy the request through the selected proxy server
        response = requests.get(url, proxies=proxies)
        return response.content.strip(), response.status_code
