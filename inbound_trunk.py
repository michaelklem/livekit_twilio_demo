# When you call the twilio number, it will call the main function in this file.
import asyncio
import os
from livekit import api
from dotenv import load_dotenv

async def main():
  load_dotenv()

  livekit_api = api.LiveKitAPI(
    # url=os.getenv("LIVEKIT_URL"),
    # api_key=os.getenv("LIVEKIT_API_KEY"),
    # api_secret=os.getenv("LIVEKIT_API_SECRET"),
  )

  inbound_trunk = api.SIPInboundTrunkInfo(
    name = "LiveKit to Twilio Trunk",
    auth_username = os.getenv("TWIML_USERNAME"),
    auth_password = os.getenv("TWIML_PASSWORD"),
    krisp_enabled = True, #noise reduction,
    numbers = ["+18582218294"],
  )

  request = api.CreateSIPInboundTrunkRequest(
    trunk = inbound_trunk,
  )

  # https://docs.livekit.io/sip/api/#createsipinboundtrunk
  inbound_trunk = await livekit_api.sip.create_sip_inbound_trunk(request)
  # inbound_trunk = livekit_api.create_sip_inbound_trunk(request)
  # inbound_trunk = livekit_api.CreateSIPInboundTrunk(
  #   name = "LiveKit to Twilio Trunk",
  #   numbers = ["+18582218294"],
  #   auth_username = os.getenv("TWIML_USERNAME"),
  #   auth_password = os.getenv("TWIML_PASSWORD"),
  #   krisp_enabled = True #noise reduction
  # )


  await livekit_api.aclose()


if __name__ == "__main__":
  asyncio.run(main())


