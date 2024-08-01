from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import openai  # Asumimos que el cliente OpenAI está configurado

# Asegúrate de que el directorio generado exista
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../../generated_code')
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

class EdifactEncoderTool(BaseTool):
    """
    Tool to generate EDIFACT encoding function code and save it to a file.
    """
    edifact_input: str = Field(description="Input EDIFACT message")
    api_response: str = Field(description="API response data")
    edifact_output: str = Field(description="Expected output EDIFACT message")

    def run(self):
        # Define the SYSTEM_PROMPT and any other relevant settings
        SYSTEM_PROMPT = f"""Purpose
You are an expert programmer specializing in python and edifact

# Instructions
- Based On:
    - An input edifact message
    - API Response
    - Proper Output Edifact Response
- Write code to format the edifact response based on inputs

# Rules
- The code must be adaptive and work for ALL possible inputs
- Only hardcode values that 100% NEED to be hardcoded
    - Always pass values where applicable

# Input
- Input Edifact Message
- API Response
- Proper Output Edifact Response

# Output
- Encoding Function
        """
        
        # Define your format_examples function as well
        def format_examples(examples):
            ...
        
        structured_examples = [
            {
                "edifact_input": self.edifact_input,
                "api_response": self.api_response,
                "edifact_output": self.edifact_output,
            }
        ]
        
        # Genera la función de codificación utilizando la API de OpenAI
        edifact_encoder_response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": format_examples(structured_examples)},
            ],
            temperature=0.0,
            max_tokens=4096,
        )

        encoding_function_code = edifact_encoder_response['choices'][0]['message']['content']

        # Determina el número del intento y guarda el archivo
        attempt_number = len(os.listdir(OUTPUT_DIR)) + 1
        file_name = f"intent_{attempt_number}.py"
        file_path = os.path.join(OUTPUT_DIR, file_name)

        with open(file_path, 'w') as file:
            file.write(encoding_function_code)

        return f"Encoding function saved to {file_path}"
