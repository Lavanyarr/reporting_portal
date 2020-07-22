

REQUEST_BODY_JSON = """
{
    "observation_id": 1
}
"""


RESPONSE_200_JSON = """
[
    {
        "observation_id": 1,
        "title": "string",
        "reported_on": "2099-12-31",
        "severity": [
            "HIGH"
        ],
        "status": [
            "ALL"
        ],
        "due_date": "2099-12-31",
        "show_due_date": true,
        "categories": [
            {
                "id": 1,
                "name": "string",
                "subcategories": [
                    {
                        "id": 1,
                        "name": "string"
                    }
                ]
            }
        ],
        "description": "string",
        "assigned_to": [
            {
                "user_id": 1,
                "name": "string",
                "phone_no": 1,
                "profile_pic": "string"
            }
        ],
        "attachments": [
            "string"
        ],
        "due_date_privacy": true
    }
]
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "https_status_code": 1,
    "res_status": "string"
}
"""

