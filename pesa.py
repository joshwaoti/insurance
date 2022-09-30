import base64
import requests
import keys
from datetime import datetime as dt
from requests.auth import HTTPBasicAuth


str_time = dt.now().strftime("%Y%m%d%H%M%S")

data = keys.businessShortCode + keys.lipa_na_mpesa_passkey + str_time
encoded = base64 = base64.b64encode(data.encode())
decoded = encoded.decode('utf-8')

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
# api_url = {"https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"}

# r = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
# print(r.text)

url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
querystring = {"grant_type":"client_credentials"}
payload = ""
headers = {
    "Authorization": "Basic SWZPREdqdkdYM0FjWkFTcTdSa1RWZ2FTSklNY001RGQ6WUp4ZVcxMTZaV0dGNFIzaA=="
}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
print(response.text)

# def lipa_na_mpesa():

#     access_token = "Access-Token"
#     api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#     headers = {"Authorization": "Bearer %s" %access_token}

#     request = {
#         "BusinessShortCode":keys.businessShortCode,    
#         "Password": decoded,    
#         "Timestamp":str_time,    
#         "TransactionType": "CustomerPayBillOnline",    
#         "Amount":"1",    
#         "PartyA":keys.phone_number,    
#         "PartyB":keys.businessShortCode,    
#         "PhoneNumber":keys.phone_number,    
#         "CallBackURL":"https://mydomain.com/pat",    
#         "AccountReference":"123456878",    
#         "TransactionDesc":"Paying for Insurance",
#     }

#     response = requests.post(api_url, json= request, headers=headers)

#     print(response.text)
