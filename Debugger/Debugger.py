from agency_swarm import Agent
from tools import DebuggerTool

class Debugger(Agent):
    def __init__(self):
        super().__init__(
            name="Debugger",
            description="Responsible for debugging code, running tests, and providing feedback.",
            tools=[DebuggerTool],  # Herramienta personalizada para debugging
            instructions="./instructions.md",
            model="gpt-4o-mini",
            tools=[],
            tools_folder="./tools",
            files_folder="./files",
            schemas_folder="./schemas",
        )

    def response_validator(self, message):
        return message
