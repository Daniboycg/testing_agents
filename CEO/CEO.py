from agency_swarm import Agent


class CEO(Agent):
    def __init__(self):
        super().__init__(
            name="CEO",
            description="Eres el ceo de la AgencIA, especializado en guiar la comunicación entre agentes de IA",
            instructions="./instructions.md",
            model="gpt-4o-mini",
            tools=[],
            tools_folder="./tools",
            files_folder="./files",
            schemas_folder="./schemas"
        )
    def response_validator(self, message):
        return message