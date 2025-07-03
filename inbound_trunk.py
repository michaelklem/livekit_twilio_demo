# When you call the twilio number, it will call the main function in this file.
import asyncio
import os
from livekit import api
from dotenv import load_dotenv

async def main():
  load_dotenv()

  livekit_api = api.LiveKitAPI()

  # Get phone numbers from environment variable
  numbers_env = os.getenv("TWILIO_NUMBERS")
  numbers = [num.strip() for num in numbers_env.split(",")]
  
  inbound_trunk = api.SIPInboundTrunkInfo(
    name = "LiveKit to Twilio Trunk",
    auth_username = os.getenv("TWIML_USERNAME"),
    auth_password = os.getenv("TWIML_PASSWORD"),
    krisp_enabled = True, #noise reduction,
    numbers = numbers,
  )

  request = api.CreateSIPInboundTrunkRequest(
    trunk = inbound_trunk,
  )

  # https://docs.livekit.io/sip/api/#createsipinboundtrunk
  inbound_trunk = await livekit_api.sip.create_sip_inbound_trunk(request)



  await livekit_api.aclose()


if __name__ == "__main__":
  asyncio.run(main())


