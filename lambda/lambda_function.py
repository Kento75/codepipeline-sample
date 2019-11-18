# lambda_function.py
from datetime import datetime, timedelta, timezone

def lambda_handler(event, context):
    JST = timezone(timedelta(hours=+9), 'JST')
    time = datetime.now(JST)
    print("What time is it now...?")
    print(time)
