from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate # chatprompttemplate 추가되었음
import os # 모델의 키를 연동하기위함
from dotenv import load_dotenv, find_dotenv
from langchain.schema import HumanMessage, AIMessage, SystemMessage

_ = load_dotenv(find_dotenv())

# 1. chat 모델 생성
chat = ChatOpenAI(
    openai_api_key =os.getenv("OPENAI_API_KEY"),
    # temperature: 0.1~1.0 : 0에 가까울수록 사실기반, 1에 가까울수록 창의력
    temperature=0.1
)

# 2. parser 생성
from langchain.schema import BaseOutputParser
class CommaOutputParser(BaseOutputParser): # 파이썬 상속은 ()
    # def __init__():  생성자
    
    def parse(self, text): # self는 java의 this와 비슷하다
        items = text.strip().split(",") # strip 좌우 여백 지우기 -> split으로 ,기준으로 나누어 list 형태로 만든다.
        return list(map(str.strip, items))
    
p = CommaOutputParser()

# 3. template 생성
template = ChatPromptTemplate.from_messages([
    ("system", "너는 리스트 생성 기계다. 모든 답변을 콤마로 구분해서 대답해라."),
    ("human", "{question}")
])


# 4. chain 생성
# - 모든 요소를 합쳐주는 역할
# - 합쳐진 요소들은 하나의 chain으로 실행(하나하나 순서대로 reuslt를 반환할 때 까지)
# - 2개 이상의 Chain을 연결 가능 

chain = template | chat | CommaOutputParser()


# 5. Chain 실행 (입력 매개변수 : dict type 전달)
result = chain.invoke({
    "max_items" : 5,
    "question" : "포켓몬은 무엇인가?"
})

print(result)