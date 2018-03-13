from celery import Celery
#import requests

app = Celery('tasks', broker='redis://localhost')

#API_BASE = ''

@app.tasks
def add(x, y):
    """
    body = {}
    apiPath = ""
    r = requests.post(API_BASE + apiPath, data=body)

    res_sec = r.elapsed.total_seconds()

    res_data = r.json()
    res_data['res_sec'] = res_sec
    return res_data
    """
    return x + y