import requests
import uuid
import json

def handler(request):
    rc = request.query.get("rc")

    payload = {
        "regNo": rc,
        "sessionid": str(uuid.uuid4())
    }

    headers = {
        "Content-Type": "application/json",
        "Origin": "https://www.91wheels.com",
        "Referer": "https://www.91wheels.com/",
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.post(
        "https://api1.91wheels.com/api/v1/third/rc-detail",
        json=payload,
        headers=headers
    )

    data = res.json()

    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }
