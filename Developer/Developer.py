from agency_swarm import Agent


class Developer(Agent):
    def __init__(self):
        super().__init__(
            name="Developer",
            description="Eres el developer de la agencia, encargado con todo lo relacionado a la creacion de codigo",
            instructions="./instructions.md",
            model="gpt-4o-mini",
            tools=[],
            tools_folder="./tools",
            files_folder="./files",
            schemas_folder="./schemas",
        )

    def response_validator(self, message):
        return message
