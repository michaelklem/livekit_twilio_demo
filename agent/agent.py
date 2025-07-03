from __future__ import annotations
import os 
import logging
from livekit import rtc
from livekit.agents import (AutoSubscribe, JobContext, WorkerOptions, cli, llm)
from livekit.agents.multimodal import MultimodalAgent
from livekit.plugins import openai
from dotenv import load_dotenv


load_dotenv()

log = logging.getLogger("voice_agent")
log.setLevel(logging.INFO)

#load instructions for ai agent
instructions_doc = open("instructions.txt", "r").read()
log.info(f"instructions: {instructions_doc}")

async def main_entry(ctx: JobContext):
  log.info(f"Initializing agent")
  open_api_key = os.getenv("OPENAI_API_KEY")

  await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

  participant = await ctx.wait_for_participant()

  ai_model = openai.realtime.RealtimeModel(
    instructions=instructions_doc,
    voice="shimmer",
    temperature=0.7,
    modalities = ["audio","text"],
    api_key=open_api_key,
  )

  multimodal_assistant = MultimodalAgent(model=ai_model)
  multimodal_assistant.start(ctx.room)

  session_instance = ai_model.sessions[0]
  session_instance.conversation.item.create(
    llm.ChatMessage(
      role="user",
      content="Begin the conversation by introducing yourself as an AI assistant and asking the caller how you can help them."
    )
  )

  session_instance.response.create()


if __name__ == "__main__":
  log.info("Starting agent")
  cli.run_app(WorkerOptions(
    entrypoint_fnc=main_entry,
    agent_name="inbound-agent",
  ))