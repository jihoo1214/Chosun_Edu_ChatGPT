from langchain.chat_models import ChatOpenAI
import os # 모델의 키를 연동하기위함
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.prompts import load_prompt


_ = load_dotenv(find_dotenv())

prompt = load_prompt("./lecture/data.json")
# prompt = load_prompt("./data.yaml")

chat = ChatOpenAI(
    openai_api_key =os.getenv("OPENAI_API_KEY"),
    # temperature: 0.1~1.0 : 0에 가까울수록 사실기반, 1에 가까울수록 창의력
    temperature=0.1,
    streaming=True,  # 그전 질문과의 연결? 어떤 답변을 원하는지 확률적으로 계산하여 보여주는데, streaming은 답변을 생성하는 과정을 시각화 가능하게 하는 설정
    callbacks=[StreamingStdOutCallbackHandler()]
)


print(prompt.format(country="Japan"))

