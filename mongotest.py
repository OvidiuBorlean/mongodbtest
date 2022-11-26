import pymongo
import time

def mongoTest():
  st = time.time()
  ConnStr = ""
  client = pymongo.MongoClient(ConnStr)
  try:
    client.server_info()  # validate connection string
    et = time.time()
    elapsed_time = et - st
    print("Connected in ", elapsed_time, "seconds" )
  except (
    pymongo.errors.OperationFailure,
    pymongo.errors.ConnectionFailure,
    pymongo.errors.ExecutionTimeout,
    ) as err:
         sys.exit("Can't connect:" + str(err))
  except Exception as err:
      sys.exit("Error:" + str(err))

if __name__ == '__main__':
  print("Running MongoDB Testing script")  
  while True:
    mongoTest()


