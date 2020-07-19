import json
import time
import boto3
import os

def hello(event, context):
   client = boto3.client('lambda')
   response = client.list_functions()
   print("Hello you are in handler fn")
   time.sleep(4)
   return os.environ["FIRST_NAME"]