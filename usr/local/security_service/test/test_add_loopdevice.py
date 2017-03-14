#coding=UTF-8

import requests
import datetime

import json
import hashlib

LOCALHOST_URL='http://127.0.0.1:5001'
#LOCALHOST_URL='http://192.168.159.159:5001'
JSON_FILE_PATH = '/usr/local/share/security_service/'
CUSTOMER_ID=''
API_HEADER = {'Content-Type': 'application/json'}

try:
  with open(JSON_FILE_PATH + "customer_id.json", "r") as f:
    file_content=json.load(f)
    CUSTOMER_ID=file_content['customer_id']
except IOError:
  print ("file doesn't exist. ignore it...")


# 128-byte random string by http://www.unit-conversion.info/texttools/random-string-generator/
HASH_SECRET='rEwIdbB9aHFHvdAheX4h7uNuh2fkNBr3WpDfFnyUqXipzOv2AVeKejc2ixffZARNAgNwCX678n0ZzrN6kRwGgd2xvxdJ17rzbRGO3KTAQRtWcWho47KAemZ8VBIwVKri'

def blending():
    customer_id=CUSTOMER_ID
    customer_id_len=len(customer_id)
    if customer_id_len > 0 :
        tmp_buffer=''
        index=0
        for bbb in HASH_SECRET:
           #print(bbb)
           # http://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python
           tmp_buffer += chr(ord(bbb) ^ ord(customer_id[index % customer_id_len])) 
           index += 1
           
        #print(tmp_buffer)            
        return tmp_buffer.encode('utf-8')  
    else:
        return HASH_SECRET.encode('utf-8')                


def gen_hash(data_Str):
    return gen_sha256(data_Str)


# http://pythoncentral.io/hashing-strings-with-python/
def gen_sha256(data_str):
    hash_object = hashlib.sha256(data_str.encode('utf-8') + blending())
    return hash_object.hexdigest()
    

def gen_md5(data_str):
    m = hashlib.md5()
    m.update((data_str+HASH_SECRET).encode('utf-8'))
    return m.hexdigest() 

################################################################################
'''
data_obj={"command":"set_customer_id","customer_id":"11345" }
json_str=json.dumps(data_obj)
#print("data str=" + json_str)
hash_str = gen_hash(json_str)
#print("hash_str=" + hash_str)
API_HEADER['sapido-hash']=hash_str
API_HEADER['api-version']='0.01'
r=requests.post(LOCALHOST_URL + '/api/send/', headers=API_HEADER,  data=json_str)
'''

data_obj={"register_all_devices":""}
json_str=json.dumps(data_obj)
hash_str = gen_hash(json_str)
API_HEADER['sapido-hash']=hash_str
API_HEADER['api-version']='0.01'
r=requests.post(LOCALHOST_URL + '/test/1/', headers=API_HEADER,  data=json_str)

# add loops
data_obj={"Loop":[{"loop_id":"1", "status":"0"}, {"loop_id":"2", "status":"0"}]}
json_str=json.dumps(data_obj)
#print("data str=" + json_str)
hash_str = gen_hash(json_str)
#print("hash_str=" + hash_str)
API_HEADER['sapido-hash']=hash_str
API_HEADER['api-version']='0.01'
r=requests.post(LOCALHOST_URL + '/api/new/', headers=API_HEADER,  data=json_str)

# add device to loop
data_obj={"LoopDevice":[{"loop_id":"1", "device_id":"xx"}, {"loop_id":"2", "device_id":"yy"}]}
json_str=json.dumps(data_obj)
#print("data str=" + json_str)
hash_str = gen_hash(json_str)
#print("hash_str=" + hash_str)
API_HEADER['sapido-hash']=hash_str
API_HEADER['api-version']='0.01'
r=requests.post(LOCALHOST_URL + '/api/new/', headers=API_HEADER,  data=json_str)

################################################################################                                                                               
print("Status Code:"+str(r.status_code) )
print("----------------------------------------------------------")
print(r.json())

print("----------------------------------------------------------")