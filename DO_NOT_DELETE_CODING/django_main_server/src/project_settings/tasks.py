from project_settings import celery_app
import csv
import io
import uuid
import json
import requests
from project_settings.pretty_printing import dumps, jprint
import os

from django.contrib.auth import get_user_model
User = get_user_model()


@celery_app.task
def debug_task(dbhost,dbname,username,passwd,table,user_id):

    data = {
        "token" :"XYZ",
        "dbhost" :dbhost,
        "dbname" :dbname,
        "username" :username,
        "passwd" : passwd,
        "table" : table,
        "port":"58028"
    }
    url='http://fast.host.docker.internal:8028/'

    try:
        r = requests.get(
            url,
            params=data
        )
        r.raise_for_status()
        print(r.content)
        buff = io.StringIO(r.text)
        dr = csv.DictReader(buff)
        for row in dr:
            print(row)
        filename = f"{uuid.uuid4().hex}.csv"
        with open(os.path.join("/home/simha/app/src/media/csv_files/", filename), 'wb') as f:
            f.write(r.content)

        user = User.objects.get(id=user_id)
        user.data_file_name = filename
        user.save()

    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
        print(jprint(errh.response.json()))
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
    print(f"Hare Krishna")