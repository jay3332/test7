from flask import Flask, request, Response
import requests
app = Flask(__name__)
BASE = 'https://turbovue-api.jay3332.tech'
BASE_2 = 'https://api.adapt.chat'
@app.route('/req', methods=['GET', 'OPTIONS', 'POST'])
def req():
    res = requests.request(method=request.method, url=BASE + request.args['path'],
        headers={k: v for k, v in request.headers if k.lower() != 'host'},
        data=request.get_data(), cookies=request.cookies, allow_redirects=False)
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(k, v) for k, v in res.raw.headers.items() if k.lower() not in excluded_headers]
    response = Response(res.content, res.status_code, headers)
    return response
@app.route('/req2', methods=['GET', 'OPTIONS', 'POST'])
def req2():
    res = requests.request(method=request.method, url=BASE2 + request.args['path'],
        headers={k: v for k, v in request.headers if k.lower() != 'host'},
        data=request.get_data(), cookies=request.cookies, allow_redirects=False)
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(k, v) for k, v in res.raw.headers.items() if k.lower() not in excluded_headers]
    response = Response(res.content, res.status_code, headers)
    return response
if __name__ == '__main__':
    app.run()
