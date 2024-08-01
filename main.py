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
    ceo,  # El CEO es el punto de entrada para la comunicación con el usuario
    [ceo, devid, debugger],  # El CEO puede iniciar la comunicación con Devid
    [ceo, debugger],  # El CEO puede iniciar la comunicación con el Debugger
    [devid, debugger]  # Devid puede comunicarse con el Debugger y viceversa
], 
shared_instructions='./agency_manifesto.md')


agency.run_demo()
