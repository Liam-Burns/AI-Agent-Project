import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_path = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_path, file_path))
        if os.path.commonpath([abs_working_path, abs_file_path]) != abs_working_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", abs_file_path]
        if args:
            command.extend(args)
        command_result = subprocess.run(
            command,
            cwd=abs_working_path,
            capture_output=True,
            timeout=30,
            text=True
        )
        output = []
        if command_result.returncode != 0:
            output.append(f'Process exited with code {command_result.returncode}')
        if not command_result.stdout and not command_result.stderr:
            output.append("No output produced")
        if command_result.stdout:
            output.append(f"STDOUT:\n{command_result.stdout}")
        if command_result.stderr:
            output.append(f"STDERR:\n{command_result.stderr}")
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
#This is the schema for when the LLM will try and decide to call the run_python_file function.
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the python file found within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "args"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path in which to access and run the .py file",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Includes any optional CLI arguments the user will pass",
                ),
                description="Includes any CLI arguments that the user may pass to the function",
            ),
        },
    ),
)



    