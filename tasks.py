from celery import Celery
import requests

app = Celery('tasks', broker='redis://localhost')

@app.task
def check_api(api_monitor_request):
    api_base_url = api_monitor_request.api_base_url
    api_url = api_monitor_request.req_url
    method = api_monitor_request.req_method
    body = api_monitor_request.get_body()
    headers = api_monitor_request.get_headers()

    r = call_api(api_base_url, api_url, body, headers, method)

    if r is None:
        return

    res_sec = r.elapsed.total_seconds()
    res_data = r.json()
    res_data['res_sec'] = res_sec
    return res_data


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