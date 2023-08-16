from fastapi import FastAPI
from proxy import ProxyManager

app = FastAPI()

proxy_servers = [
    "http://38.154.17.191:8800",
    "http://38.154.17.122:8800",
    "http://38.154.17.33:8800",
    "http://38.154.17.69:8800",
    "http://38.154.17.125:8800",
    "http://38.154.17.25:8800",
    "http://38.154.17.26:8800",
    "http://38.154.17.80:8800",
    "http://38.154.17.20:8800",
    "http://38.154.17.131:8800",
]

proxy_manager = ProxyManager(proxy_servers)

@app.get("/")
def proxy_request():
    url = "http://ip.ip-check.net/"
    content, status_code = proxy_manager.proxy_request(url)
    return content, status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
