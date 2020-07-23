'''
categories and subcategories:

response = requests.get('http://localhost:8080/api/reporting_portal/get_categories_with_subcategories/v1/',json={},headers= {'Authorization': 'bearer token'})
response = requests.post('http://localhost:8080/api/reporting_portal/create_observation/v1/',json={'title':'devaitions','category_id':1,'sub_category_id':3,'severity':'HIGH','description':'devaitions in learning','att
   ...: achments':[]},headers= {'Authorization': 'bearer token'})
'''