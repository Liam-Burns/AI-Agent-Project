import os

from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_target_filepath = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_target_filepath.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_target_filepath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # Read's the content from the file itself and determines if it's longer than 10k chars
    MAX_CHARS = 10000

    try:
        with open(abs_target_filepath, "r") as f:
            file_content_string = f.read()

            if len(file_content_string) > MAX_CHARS:
                return file_content_string + f'[...File "{file_path}" truncated at 10000 characters]'
            else:
                return file_content_string
    except Exception as e:
        return f"Error: {e}"
    
#This is the schema for when the LLM will try and decide to call the get_files_content function
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the content of a certain file up to 10000 characters if it exists in the working directory",
    parameters=types.Schema(
        required=["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to list the contents from, relative to the working file path",
            ),
        },
    ),
)
    
    