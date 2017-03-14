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
data_obj={
  "WLDoubleBondBTemperatureSensor":{
    "filter":{'device_id': '5149013103542553'},
    "update":{'nick_name':'體溫感測', 'temperature_sensing': '60',
     'microwave_sensitivity_set': '25', 'G_sensor_status': '1', 
     'serialVersionUID': 0,
      'msg_send_strong_set_manual': '70%', 
      'connection_time_set': '0', 'action_count_time': '10', 
      'temperature_sensing_gap': '20', 'device_id': '5149013103542553', 
      'microwave_set': '0', 'msg_send_strong_set': '1', 'infrared_set': '1', 
      'msg_send_strong_set_manual_gap': '25', 
      'transmission_distance_set_manual': '700', 
      'transmission_distance': '1', 'battery_low_power_set': '70', 
      'G_sensitivity': '70%', 'action_count_frequency': '25', 
      'terminating_impedance': '30%', 'battery_low_power_gap': '10'}
  }
}
'''
data_obj={
  "WLDoubleBondBTemperatureSensor":{
    "filter":{'device_id': '5149013103542553'},
    "update":{'nick_name':'體溫感測', 
     'temperature_sensing': '60',
     'microwave_sensitivity_set': '25', 
     'G_sensor_status': '1' 
    }
  }
}

##########################################################################################
json_str=json.dumps(data_obj)
#print("data str=" + json_str)
hash_str = gen_hash(json_str)
#print("hash_str=" + hash_str)
API_HEADER['sapido-hash']=hash_str
API_HEADER['api-version']='0.01'

print("data str=" + json_str)
r=requests.post(LOCALHOST_URL + '/api/update/', headers=API_HEADER,  data=json_str)

print("Status Code:"+str(r.status_code) )
print("----------------------------------------------------------")
print(json.dumps(r.json()))

print("----------------------------------------------------------")