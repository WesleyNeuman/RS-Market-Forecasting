import requests
import pandas as pd
import json

class ApiHandler(object):
    """Class for interacting with the Runescape APIs"""

    # 
    def ImportByCategory(self, category, alpha, page):
        endpoint = "https://services.runescape.com/m=itemdb_rs/api/catalogue/items.json"
        params = {
            'category' : '0',
            'alpha' : 'a',
            'page' : '1'
            }
        response = requests.get(endpoint, params)
        jtext = response.json()
        response_df = pd.DataFrame.from_dict(jtext['items'])
        response_df = response_df[['id','type','name','members']]
        return response_df


