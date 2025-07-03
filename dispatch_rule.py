import asyncio
import os
from livekit import api
from dotenv import load_dotenv

async def main():
  load_dotenv()

  livekit_api = api.LiveKitAPI()

  rule = api.SIPDispatchRule(
    dispatch_rule_individual = api.SIPDispatchRuleIndividual(
      room_prefix = "call-"
    )
  )

  agent = api.RoomAgentDispatch(
    agent_name = "inbound-agent",
  )

  room_config = api.RoomConfiguration(
    agents = [agent]
  )

  request = api.CreateSIPDispatchRuleRequest(
    rule = rule,
    room_config = room_config,
  )

  dispatch = await livekit_api.sip.create_sip_dispatch_rule(request)

  await livekit_api.aclose()

if __name__ == "__main__":
  asyncio.run(main())