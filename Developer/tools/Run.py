from agency_swarm.tools import BaseTool
from pydantic import Field
import subprocess


class PythonCodeRunnerTool(BaseTool):
    """
    Herramienta para ejecutar y depurar código Python. Permite al Developer ejecutar scripts de Python y revisar el output o errores generados.
    """

    code: str = Field(..., description="Código Python que será ejecutado.")

    def run(self) -> str:
        """
        Ejecuta el código Python proporcionado y retorna la salida o errores.
        """
        try:
            # Ejecuta el código en un proceso separado y captura la salida.
            result = subprocess.run(
                ["python", "-c", self.code], capture_output=True, text=True, check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            # Si ocurre un error, captura el error y lo retorna.
            return e.stderr


# Ejemplo de uso:
# tool = PythonCodeRunnerTool(code="print('Hola Mundo!')")
# print(tool.run())
