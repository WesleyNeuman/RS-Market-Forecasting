import pandas as pd
from sqlalchemy import create_engine

class MicrosoftSqlDbHandler(object):

    con = None

    def CreateConnection(self):
        self.con = create_engine('mssql+pyodbc://MSI\\SQLEXPRESS/RsMarketForecasting?trusted_connection=yes')
    
    def LogDF(self, pandas, alch_engine):
        pass




