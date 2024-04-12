from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate # chatprompttemplate 추가되었음
import os # 모델의 키를 연동하기위함
from dotenv import load_dotenv, find_dotenv
from langchain.schema import HumanMessage, AIMessage, SystemMessage

_ = load_dotenv(find_dotenv())

chat = ChatOpenAI(
    openai_api_key =os.getenv("OPENAI_API_KEY"),
    # temperature: 0.1~1.0 : 0에 가까울수록 사실기반, 1에 가까울수록 창의력
    temperature=0.1
)

# parser: GPT가 생성한 답변을 parser를 통해서 원하는 형태로 parsing
from langchain.schema import BaseOutputParser
class CommaOutputParser(BaseOutputParser): # 파이썬 상속은 ()
    # def __init__():  생성자
    
    def parse(self, text): # self는 java의 this와 비슷하다
        items = text.strip().split(",") # strip 좌우 여백 지우기 -> split으로 ,기준으로 나누어 list 형태로 만든다.
        return list(map(str.strip, items))
    
p = CommaOutputParser()
# result = p.parse("hello, how, are, you")
template = ChatPromptTemplate.from_messages([
    ("system", "너는 리스트 생성 기계다. 모든 답변을 콤마로 구분해서 대답해라."),
    ("human", "{question}")
])

prompt = template.format_messages(
    max_items=10,
    question="색상은 무엇인가?"
)

result = chat.predict_messages(prompt)
print(p.parse(result.content))