from celery import Celery
import requests
import json

app = Celery('tasks', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')
app.conf.timezone = 'Asia/Seoul'


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    try:
        sender.add_periodic_task(30.0,
                                 check_api.s(api_base_url='https://www.grap.io/api',
                                             req_url='/v2/user/login',
                                             req_method='POST',
                                             req_body='{}'),
                                name='add every 30')
    except Exception as e:
        print(e)



@app.task
def test(arg):
    print(arg)

@app.task
def check_api(api_base_url, req_url, req_method, req_body, req_header="{}"):
    body = chage_json(req_body)
    headers = chage_json(req_header)

    try:
        r = call_api(api_base_url, req_url, body, headers, req_method)
        if r is None:
            return

        res_sec = r.elapsed.total_seconds()
        res_data = r.json()
        res_data['res_sec'] = res_sec
        return res_data
    except Exception as e:
        print(e)


def chage_json(str):
    try:
        return json.loads(str)
    except ValueError:
        return {}


def call_api(api_base_url, api_url, body, headers, method):
    if method is 'GET':
        return requests.post(api_base_url + api_url, data=body, headers=headers)
    elif method is 'POST':
        return requests.post(api_base_url + api_url, data=body, headers=headers)
    elif method is 'PUT':
        return requests.post(api_base_url + api_url, data=body, headers=headers)
    elif method is 'DELETE':
        return requests.post(api_base_url + api_url, data=body, headers=headers)
    else:
        return None
