import os 
import chainlit as cl 
from dotenv import load_dotenv
from typing import Optional, Dict
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tools import function_tool

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)


model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

@function_tool("get_weather")
def get_weather(location: str, unit: str = "C") -> str:
    """
    Fetch the Weather for a given location, return the weather
    """
    return f"The weather in {location} is 22 degree {unit}"


agent = Agent(
    name="Greeting Agent",
    instructions="You are a Greeting Agent, Your task is to greet the user with a friendly message, when someone says hi you've reply back with salam from Sadia Batool, if someone says bye then say allah hafiz from asharib ali,if someone asks about weather then use the get_weather tool to get the weather, when someone asks other than greeting and weather then say Sadia Batool is here just for greeting and weather, I can't answer anything else, sorry.",
    model=model,
    tools=[get_weather]
)

@cl.oauth_callback
def oauth_callback(
    provider_id: str, 
    token: str, 
    raw_user_data: Dict[str, str],  
    default_user: cl.User,  
) -> Optional[cl.User]:  
    """
    Handle the OAuth callback from GitHub
    Return the user object if authentication is successful, None otherwise
    """

    print(f"Provider: {provider_id}") 
    print(f"User data: {raw_user_data}")  

    return default_user  

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", []) 

    await cl.Message(
        content="Hello! How can I help you today?"
    ).send()


@cl.on_message
async def handle_message(message: cl.Message):

    history = cl.user_session.get("history")  

    history.append(
        {"role": "user", "content": message.content}
    )  

    result = await cl.make_async(Runner.run_sync)(agent, input=history)

    response_text = result.final_output
    await cl.Message(conntent=response_text).send()

    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)
