from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "REDACTED"
# Your Auth Token from twilio.com/console
auth_token  = "REDACTED"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1REDACTED",
    from_="+1REDACTED",
    body="Hello from Python!")

print(message.sid)