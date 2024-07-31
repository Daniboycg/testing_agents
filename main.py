from agency_swarm import Agent, Agency, get_openai_client
from dotenv import load_dotenv
from CEO import ceo


load_dotenv()
client = get_openai_client()

ceo = ceo()

agency = Agency(
    [ceo],
)

agency.demo_gradio()