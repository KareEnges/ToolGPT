import os

OPENAI_API_KEY = ""
verbose = True
model = "gpt-3.5-turbo"
streaming = True
max_token_limit = 3000
language = "尽可能的chinese，少量english"
uiTitle = "XZAITool"


def init():  # not neccessary
    os.environ["GOOGLE_API_KEY"] = ""
    os.environ["GOOGLE_CSE_ID"] = ""
    os.environ["LANGCHAIN_TRACKING"] = "true"
    os.environ["SERPER_API_KEY"] = ""
