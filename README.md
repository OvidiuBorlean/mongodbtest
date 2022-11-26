# Azure MongoDBtest

The objective of this script is to test connectivity with a Azure MongoDB Instance and measure the latency of that operation in a loop.

# Prerequisites

The following packages needs to be installed in order to run this script:

Python3
Python3-pip
pymongo (PIP Package)

# Installation

```
apt update
apt install python3 -y
apt install python3-pip -y
pip3 install pymongo
```
As the library is using CosmosDB ConnectionString for initializing connection, we need to obtain this from Azure Portal and add into our script.

# Source Code

```
import pymongo
import time

def mongoTest():
  st = time.time()
  ConnStr = "Add here your Connection String"
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
```
This script will run in a continuous loop and will measure and display the connectivity time of the connect
