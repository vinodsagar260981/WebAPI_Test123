from twilio.rest import Client 
 
account_sid = 'AC4052a342600ed0abb67b8dc8561cbcec' 
auth_token = '4512b1fc15e9e15c0e307d0660a9f9ce' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG3211d5784b97a33b6a689ddeca7ced4f', 
                              body='I am finding odd',      
                              to='+919900422483' 
                          ) 
 
print(message.sid)
