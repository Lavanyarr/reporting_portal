

REQUEST_BODY_JSON = """
{
    "sort_type": [
        "ASC"
    ],
    "filter_type": [
        "REPORTED"
    ],
    "sort_field": [
        "REPORTED_ON"
    ]
}
"""


RESPONSE_200_JSON = """
{
    "total_observations_count": 1,
    "observation_details": [
        {
            "observation_id": 1,
            "title": "string",
            "reported_on": "2099-12-31",
            "severity": "HIGH",
            "status": "ALL",
            "due_date": "2099-12-31",
            "show_due_date": true,
            "reported_by": {
                "user_id": 1,
                "name": "string",
                "phone_no": 1,
                "profile_pic": "string"
            },
            "messages_count": 1
        }
    ]
}
"""

