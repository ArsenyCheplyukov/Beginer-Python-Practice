import datetime

a = datetime.datetime.today().strftime("%Y%m%d")
print(a) # '20170405'

today = datetime.datetime.today()
print( today.strftime("%m/%d/%Y") ) # '04/05/2017'

print( today.strftime("%Y-%m-%d-%H.%M.%S") ) # 2017-04-05-00.18.00
