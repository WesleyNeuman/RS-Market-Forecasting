# Import External Modules
import requests
import pandas as pd
import json
import time

# Import Local Modules
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

        if recursion_level == 0:
            logging.info('Requesting data for %s, %s, %s at recursion level %s', category, alpha, page, str(recursion_level))
        else:
            logging.warning('Requesting data for %s, %s, %s at recursion level %s', category, alpha, page, str(recursion_level))
        
        response = requests.get(self.endpoint, params)

        # Actions for if the response is bad
        if response == 'BAD' & recursion_level < 5:
            time.sleep(short_delay)
            recursion_df = self.ImportByChunk(category, alpha, page, recursion_level+1)
            return recursion_df
        elif response == 'BAD' & recursion_level == 5:
            time.sleep(long_delay)
            recursion_df = self.ImportByChunk(category, alpha, page, recursion_level+1)
            return recursion_df
        elif response == 'BAD' & recursion_level > 5:
            logging.error('Request for %s, %s, %s has failed', category, alpha, page)
            return None
        
        jtext = response.json()
        response_df = pd.DataFrame.from_dict(jtext['items'])
        response_df = response_df[['id','type','name','members']]
        return response_df


    # Determines the number of items for a given category by letter
    def DeterminePageCount(self, category, recursion_level=0):
        params = {
            'category' : category
            }

        if recursion_level == 0:
            logging.info('Requesting page counts for %s at recursion level %s', category, str(recursion_level))
        else:
            logging.warning('Requesting page counts for %s at recursion level %s', category, str(recursion_level))

        response = requests.get(self.endpoint, params)

        # Actions for if the response is bad
        if response == 'BAD' & recursion_level < 5:
            time.sleep(short_delay)
            recursion_dict = self.DeterminePageCount(category, alpha, recursion_level+1)
            return recursion_dict
        elif response == 'BAD' & recursion_level == 5:
            time.sleep(long_delay)
            recursion_dict = self.DeterminePageCount(category, alpha, recursion_level+1)
            return recursion_dict
        elif response == 'BAD' & recursion_level > 5:
            logging.error('Page Count Request for %s has failed', category)
            return None
        
        jtext = response.json()
        cat_dict = jtext['alpha']
        return cat_dict


    # Import the entirety of IDs for a given category and letter
    def ImportByCategory(self, category, alpha, total_pages):
        df = pd.DataFrame()
        for i in range(1, total_pages):
            df = df.append(ImportByChunk(category, alpha, i))
        return df


    # Using an acquired Item ID, pull the last 180 days of trading data
    def ImportGraph(self, item_id, recursion_level):
        graph_endpoint = "https://services.runescape.com/m=itemdb_rs/api/graph/" + item_id + ".json"

        if recursion_level == 0:
            logging.info('Requesting graph data for %s at recursion level %s', item_id, str(recursion_level))
        else:
            logging.warning('Requesting graph data for %s at recursion level %s', item_id, str(recursion_level))

        response = requests.get(graph_endpoint)

        # Actions for if the response is bad
        if response == 'BAD' & recursion_level < 5:
            time.sleep(short_delay)
            recursion_df = self.ImportGraph(category, alpha, recursion_level+1)
            return recursion_dict
        elif response == 'BAD' & recursion_level == 5:
            time.sleep(long_delay)
            recursion_df = self.ImportGraph(category, alpha, recursion_level+1)
            return recursion_dict
        elif response == 'BAD' & recursion_level > 5:
            logging.error('Graph Request for %s has failed', item_id)
            return None

        jtext = response.json()
        response_df = pd.DataFrame.from_dict(jtext['average'])
        return response_df







