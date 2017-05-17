import twilio.rest as tr

account_sid = "AC78b06741090d40d9ecaea4cc2bd59415"
auth_token = "a48cec43c92d3ef6d84ec35edf9dd03f"
client = tr.TwilioRestClient(account_sid, auth_token)
message = client.messages.create(to="+86你的号码",  
                                 from_="+你的twilio的号码", 
                                 body="你们宿舍有贼，回来抓贼！！")