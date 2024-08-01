# Agency Manifesto

## Overview Functionality
- Have system write code to format the API response into an edifact message
- Run the API response through the adapter to see if the code actually produces the proper response
    - If response is valid
        - Go to next test case
    - Else
        - Ask the EDIFACT agent what is wrong with the message
        - Tell the coder agent to fix the code based on what is wrong
- Repeat until all test cases are passed

## Roles y Responsabilidades
### CEO
- Coordina la comunicación y asigna tareas a Devid.
- Supervisa la calidad y cumplimiento de los objetivos.

### Devid (Desarrollador)
- Escribe y entrega código según las especificaciones.
- Colabora con Debugger para corregir errores.

### Debugger
- Depura el código de Devid utilizando la herramienta `DebuggerTool`.
- Informa sobre errores y sugiere correcciones.

## Proceso de Trabajo
1. **Asignación:** El CEO asigna tareas a Devid.
2. **Desarrollo:** Devid escribe el código y lo envía a Debugger.
3. **Depuración:** Debugger revisa, corrige e informa a Devid.
