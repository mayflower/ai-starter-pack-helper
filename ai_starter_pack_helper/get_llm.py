from langchain_openai import ChatOpenAI, AzureChatOpenAI


class GetLLM:
    @staticmethod
    def gpt4(apikey):
        return ChatOpenAI(verbose=True, model="gpt-4", api_key=apikey, streaming=True)

    @staticmethod
    def gpt4turbo(apikey):
        return ChatOpenAI(verbose=True, model="gpt-4-1106-preview", api_key=apikey, streaming=True)

    @staticmethod
    def gpt35turbo(apikey):
        return ChatOpenAI(verbose=True, model="gpt-3.5", api_key=apikey, streaming=True)

    @staticmethod
    def azure_gpt(azure_apikey, azure_endpoint, deployment_name):
        return AzureChatOpenAI(
            deployment_name=deployment_name,
            azure_endpoint=azure_endpoint,
            api_key=azure_apikey,
            api_version="2023-05-15",
        )
