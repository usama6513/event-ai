from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
import asyncio

gemini_api_key = "your api key"

client = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/" 

)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.5-flash",
    openai_client=client
)


config = RunConfig(
    model = model,
    model_provider= client,
    tracing_disabled=True
)
simple_agent = Agent(
    name = "Adviser Assistant",
    instructions = "you  are a helpful Adviser Assistant you will provide the suitable and best answers the questions"

)
async def main():
    result = await Runner.run(
    starting_agent=simple_agent, 
    input= "Aslamualikum dear how are you, you Advise me that what can i do for my future's best ",
    run_config= config
)
    print("result>>>>>", result.final_output)

asyncio.run(main())