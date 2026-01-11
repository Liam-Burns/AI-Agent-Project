import os
from google.genai import types

def write_file(working_directory, file_path, file_content_string):

    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_directory, file_path))

        if os.path.commonpath([abs_working_directory, abs_file_path]) != abs_working_directory:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(abs_file_path):
             return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        with open(abs_file_path, "w") as f:
                f.write(file_content_string)
        return (
            f'Successfully wrote to "{file_path}" ({len(file_content_string)} characters written)'
        )
    except Exception as err:
        return f"Error: {err}"
    
#This is the schema for when the LLM will try and decide to call the write_file function.
schema_write_file = types.FunctionDeclaration(
     name="write_file",
     description="Edits and writes against the current file selected from the working directory",
     parameters=types.Schema(
          type=types.Type.OBJECT,
          required=["file_path", "file_content_string"],
          properties={
               "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="File path in which the file is located that we will edit and re-write",
               ),
               "file_content_string": types.Schema(
                    type=types.Type.STRING,
                    description="The content that we will append to the selected file",
               ),
          },
     ),
)
    

    
