import requests
import pandas as pd
import json
import time

import DataManagement.ApiIteratedData as iter

class ApiHandler(object):
    """Class for interacting with the Runescape APIs"""

    endpoint = "https://services.runescape.com/m=itemdb_rs/api/catalogue/items.json"
    short_delay = 5
    long_delay = 120

    # Lowest level of pull for category builder
    def ImportByChunk(self, category, alpha, page, recursion_level=0):
        params = {
            'category' : category,
            'alpha' : alpha,
            'page' : page
            }
        response = requests.get(self.endpoint, params)
        jtext = response.json()

        # Actions for if the response is bad
        if jtext == 'BAD' & recursion_level < 5:
            time.sleep(short_delay)
            recursion_df = self.ImportByChunk(category, alpha, page, recursion_level+1)
            return recursion_df
        elif jtext == 'BAD' & recursion_level == 5:
            time.sleep(long_delay)
            recursion_df = self.ImportByChunk(category, alpha, page, recursion_level+1)
            return recursion_df
        elif jtext == 'BAD' & recursion_level > 5:
            return None

        response_df = pd.DataFrame.from_dict(jtext['items'])
        response_df = response_df[['id','type','name','members']]
        return response_df


    # Determines the number of items for a given category by letter
    def DeterminePageCount(self, category, recursion_level=0):
        params = {
            'category' : category
            }
        response = requests.get(self.endpoint, params)
        jtext = response.json()

        # Actions for if the response is bad
        if jtext == 'BAD' & recursion_level < 5:
            time.sleep(short_delay)
            recursion_dict = self.DeterminePageCount(category, alpha, recursion_level+1)
            return recursion_dict
        elif jtext == 'BAD' & recursion_level == 5:
            time.sleep(long_delay)
            recursion_dict = self.DeterminePageCount(category, alpha, recursion_level+1)
            return recursion_dict
        elif jtext == 'BAD' & recursion_level > 5:
            return None

        cat_dict = jtext['alpha']
        return cat_dict


    # Import the entirety of IDs for a given category and letter
    def ImportByCategory(self, category, alpha, total_pages):
        df = pd.DataFrame()
        for i in range(1, total_pages):
            df = df.append(ImportByChunk(category, alpha, i))
        return df





