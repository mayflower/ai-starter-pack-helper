from langchain_openai import ChatOpenAI


class get_llm:
    @staticmethod
    def gpt4(apikey):
        return ChatOpenAI(verbose=True, model="gpt-4", api_key=apikey, streaming=True)

    @staticmethod
    def gpt4turbo(apikey):
        return ChatOpenAI(verbose=True, model="gpt-4-1106-preview", api_key=apikey, streaming=True)

    @staticmethod
    def gpt35turbo(apikey):
        return ChatOpenAI(verbose=True, model="gpt-3.5", api_key=apikey, streaming=True)
