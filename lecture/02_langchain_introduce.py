from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

import os # 모델의 키를 연동하기위함
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

chat = ChatOpenAI(
    openai_api_key =os.getenv("OPENAI_API_KEY"), # api key 오류 -> 키값 넣기
    # temperature: 0.1~1.0 : 0에 가까울수록 사실기반, 1에 가까울수록 창의력
    temperature=0.1
)

template = PromptTemplate.from_template(
    "{country_a}과 {country_b}의 거리는 얼마인가요?"
)

prompt = template.format(country_a="한국", country_b="일본")

print(chat.predict(prompt))