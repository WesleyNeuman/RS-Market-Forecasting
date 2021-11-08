#Import External Modules

#Import Local Modules
import DataManagement.ApiHandler as ah 
import DataManagement.MicrosoftSqlDbHandler as mssql

#handler = ah.ApiHandler()
#handler.ImportByCategory()

dbLogger = mssql.MicrosoftSqlDbHandler()
dbLogger.CreateConnection()
