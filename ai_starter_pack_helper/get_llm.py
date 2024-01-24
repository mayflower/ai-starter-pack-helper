from langchain_openai import ChatOpenAI


def get_llm(apikey):
    return ChatOpenAI(verbose=True, model="gpt-4", api_key=apikey, streaming=True)


def get_llm_gpt4_turbo(apikey):
    return ChatOpenAI(verbose=True, model="gpt-4-1106-preview", api_key=apikey, streaming=True)
