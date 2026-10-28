from client.llm_client import LLMClient
import asyncio

async def main():
  client = LLMClient()
  messages = [{
    "role": "user",
    "content": "What is 2 + 2"
  }]
  async for event in  client.chat_completion(messages=messages, stream=False):
    print(event)
  print("done")
asyncio.run(main())