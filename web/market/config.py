web_DB = 'sqlite:///market.db'

web_User = 'admin' #os.environ.get()

web_Pass = 'admin'

DB = 'market'

web_Host = 'localhost'

web_Port = 5001

prod_DB = f'postgresql://{web_User}:{web_Pass}@{web_Host}:{web_Port}/{DB }'