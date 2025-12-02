from tasks import chat, create_documentation
from dotenv import load_dotenv
import logging
from prompt_toolkit import prompt

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)

load_dotenv() 

def main():
    print("Write:\n \
          1 - to ask questions about code \n \
          2 - to generate documentation ")

    
    user_input = prompt(">>> ")
    selection  = user_input
    print("Enter the path to the folder with the code")
    user_input = prompt(">>> ")
    code_directory  = user_input
    if selection == "1":
        chat.chat()   
    elif selection == "2":
        create_documentation.generate_documentation(code_directory)

                 

if __name__ == "__main__":
    main()