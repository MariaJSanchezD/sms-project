from twilio.rest import Client
import os

account_sid = os.environ['sid']
auth_token = os.environ['token']
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid=os.environ['m_s_i'],
    body='This is a SMS example',
    to=os.environ['to']
)

print(message.sid)
