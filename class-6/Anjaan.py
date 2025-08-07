from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, ItemHelpers
from openai.types.responses import ResponseTextDeltaEvent
import asyncio


gemini_api_key = "your api key"


client = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"

)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.5-flash",
    openai_client= client

)


Config = RunConfig(
    model= model,
    model_provider= client,
    tracing_disabled=True
)

simple_agent = Agent(
    name = "maths Assistant",
    instructions= "you are a helpful maths Assistant you will provide the suitable and best answers of the questions"

)
async def main():
    result = Runner.run_streamed(
    starting_agent=simple_agent,
    input=" what is maths",
    run_config= Config
)
    async for event in result.stream_events():
        print("events>>>>",event.type)
        if event.type == "raw_response_event" and isinstance(event.data,ResponseTextDeltaEvent):
            print("event>>>>",event.data.delta, end="")
            continue
        elif event.type == "agent_updated_stream_event":
            print("event>>>",event)
            print(f"Agent updated with {event.new_agent.name}")
            continue
        elif event.type == "run_item_stream_event":
            #print("event>>>>", event)
            if event.item.type == "message_output_item":
                #print(event.item.raw_item.content[0].text)
                print(ItemHelpers.text_message_output(event.item))
asyncio.run(main())