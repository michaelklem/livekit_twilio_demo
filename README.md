# livekit_twilio_demo
Working source for this video https://www.youtube.com/watch?v=2HmqSXHYMJ8

Go through the video to set up your twilio phone number first, then:
1. copy .env_example to .env
2. populate with your values
3. python -m venv venv
4. source venv/bin/activate
5. pip install -r requirements.txt
6. python3 inbound_trunk.py
   1. Should not have any errors
7. python3 dispatch_rule.py
   1. Should not have any errors
8. cd agent
9. python3 agent.py dev
   1. Should not have any errors

Call your twilio number and it should connect to your room and have a conversation with the agent.