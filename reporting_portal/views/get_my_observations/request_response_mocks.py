

REQUEST_BODY_JSON = """
{
    "sort_type": "ASC",
    "filter_type": "REPORTED",
    "sort_field": "REPORTED_ON"
}
"""


RESPONSE_200_JSON = """
{
    "total_observations_count": 1,
    "observation_details": [
        {
            "observation_id": 1,
            "title": "string",
            "reported_on": "2099-12-31 00:00:00",
            "severity": "HIGH",
            "status": "ALL",
            "due_date": "string",
            "assigned_to": {
                "user_id": 1,
                "name": "string",
                "phone_no": 1,
                "profile_pic": "string"
            },
            "show_due_date": true,
            "messages_count": 1
        }
    ]
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "https_status_code": 1,
    "res_status": "Invalid Limit"
}
"""

