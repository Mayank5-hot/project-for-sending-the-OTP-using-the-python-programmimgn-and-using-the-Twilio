import twilio
from twilio.rest import Client

    account_sid = 'ACae453e4ecd7b0b691cb98a2a32e05cd8'
            auth_token = 'f9eb9af854c8ae6c79948bdf4709c943'
            client = Client(account_sid, auth_token)
        
            message = client.messages.create
            (
                body= 'Yeh jo mohabbat hai yeh unaka hain kam',
                from_='+12015146040',to= '+918939600640'
            )
            print(message.sid)

 
        