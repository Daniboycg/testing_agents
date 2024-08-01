from agency_swarm import Agent, Agency, get_openai_client
from dotenv import load_dotenv
from CEO import CEO
from Devid import Devid
from Debugger import Debugger

load_dotenv()
client = get_openai_client()

ceo = CEO()
devid = Devid()
debugger = Debugger()

agency = Agency([
    devid,# Devid puede comunicarse con el Debugger y viceversa
], 
shared_instructions='./agency_manifesto.md')


agency.run_demo()
