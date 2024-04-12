from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate # chatprompttemplate 추가되었음

# 1. PromptTemplate: 질문:답변 끝 (1회성)
# 2. ChatPromptTemplate: Chat(채팅처럼)

import os # 모델의 키를 연동하기위함
from dotenv import load_dotenv, find_dotenv

from langchain.schema import HumanMessage, AIMessage, SystemMessage

_ = load_dotenv(find_dotenv())

chat = ChatOpenAI(
    openai_api_key =os.getenv("OPENAI_API_KEY"),
    # temperature: 0.1~1.0 : 0에 가까울수록 사실기반, 1에 가까울수록 창의력
    temperature=0.1
)

template = ChatPromptTemplate.from_messages([
    ("system","너는 탐험가야, 너는 모든 모든 답변을 {language}로 해야해!"),
    ("ai", "Hello I'm {name}"),
    ("human","{country_a}과 {country_b}의 거리는 얼마인가요? 너의 이름은 무엇이니?"),
])


prompt = template.format_messages(
    language="Greek",
    name="Socrates",
    country_a="Mexico",
    country_b="Tailand"
)


print(chat.predict_messages(prompt))