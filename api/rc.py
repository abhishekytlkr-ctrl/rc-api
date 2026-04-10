import requests
import uuid
import json

def handler(request):
    try:
        rc = request.query.get("rc")

        if not rc:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "RC required"})
            }

        rc = rc.strip().upper()

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

        data = res.json().get("data", {})

        # 🔥 Clean structured response
        result = {
            "vehicle_number": rc,
            "owner": data.get("ownerName"),
            "father_name": data.get("fatherName"),
            "address": data.get("presentAddress"),
            "vehicle": {
                "model": data.get("makerModel"),
                "fuel": data.get("fuelType"),
                "color": data.get("color"),
                "class": data.get("vehicleClass"),
                "body_type": data.get("bodyType")
            },
            "registration": {
                "date": data.get("regDate"),
                "rto": data.get("registeredAt"),
                "state": data.get("state")
            },
            "insurance": {
                "company": data.get("insuranceCompany"),
                "expiry": data.get("insuranceUpto")
            },
            "technical": {
                "engine": data.get("engineNumber"),
                "chassis": data.get("chassisNumber"),
                "cc": data.get("cubicCapacity"),
                "norms": data.get("emissionNorms")
            },
            "finance": {
                "financer": data.get("financer"),
                "blacklist": data.get("blacklistStatus")
            }
        }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "success": True,
                "data": result
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
