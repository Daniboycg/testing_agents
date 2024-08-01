from agency_swarm import Agent, Agency, get_openai_client
from dotenv import load_dotenv
from CEO import ceo
from Developer import Developer
from Devid import Devid

load_dotenv()
client = get_openai_client()

ceo = ceo()
developer = Developer()
devid = Devid()

agency = Agency(
    [
        ceo,  # El CEO será el punto de entrada para la comunicación con el usuario
        [ceo, developer],
        devid,  # El CEO puede iniciar comunicación con el Developer
    ]
)


agency.run_demo()
