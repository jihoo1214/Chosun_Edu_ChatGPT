from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

import os # 모델의 키를 연동하기위함
from dotenv import load_dotenv, find_dotenv

from langchain.schema import HumanMessage, AIMessage, SystemMessage

_ = load_dotenv(find_dotenv())

chat = ChatOpenAI(
    openai_api_key =os.getenv("OPENAI_API_KEY"),
    # temperature: 0.1~1.0 : 0에 가까울수록 사실기반, 1에 가까울수록 창의력
    temperature=0.1
)

messages = [
    SystemMessage(content="너는 탐험가야, 너는 모든 모든 답변을 영어로 해야해!"),
    AIMessage(content="Hello I'm sara"),
    HumanMessage(content="한국과 일본의 거리는 얼마인가요? 너의 이름은 무엇이니?"),
]

print(chat.predict_messages(messages))