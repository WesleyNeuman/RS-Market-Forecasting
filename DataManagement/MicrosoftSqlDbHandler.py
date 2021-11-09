# Import External Modules
import pandas as pd
import pyodbc
from sqlalchemy import create_engine
import logging

# Import Local Modules
import DataManagement.ApiHandler as api
import DataManagement.ApiIteratedData as iter

class MicrosoftSqlDbHandler(object):

    con = None
    api_handler = None
    alpha = None
    category = None

    def __init__(self):
        self.con = create_engine('mssql+pyodbc://MSI\SQLEXPRESS/RsMarketForecasting?driver=SQL Server?Trusted_Connection=yes')
        self.api_handler = api.ApiHandler()
        self.alpha = iter.get_alpha()
        self.category = iter.get_category()

    # Main function for gathering API results and databasing them
    def PopulateIDs(self):
        
        # Need code here to compare found categories with the full category search arrays for resuming a busted query
        Get_Categories()
        alpha_rev = self.alpha
        category_rev = self.category

        for c in category_rev:
            page_totals = self.api_handler.DeterminePageCount(c, 0)
            for a in alpha_rev:
                pages = page_totals[a] / 10 # Currently assuming a page item count of 10
                cat_df = self.api_handler.ImportByCategory(c, a, pages)
                self.Log_Category(cat_df)
        

    # Logs the results of the categorical Item ID queries to the database
    def Log_Category(self, cat_df):
        cat_df.to_sql('placeholder', self.con, if_exists='append', index=False)

    def Log_Graph(self):
        pass


    # Identify categories in database. This allows identification of stopping point for resuming pulls
    def Get_Categories(self):
        pass







