# Import External Modules
import logging

# Import Local Modules
import DataManagement.ApiHandler as ah 
import DataManagement.MicrosoftSqlDbHandler as mssql

# Initialize program logging
logging.basicConfig(filename='RS_Logger.log', level=logging.INFO)
logging.info('Initializing...')

dbLogger = mssql.MicrosoftSqlDbHandler()
dbLogger.CreateConnection()
