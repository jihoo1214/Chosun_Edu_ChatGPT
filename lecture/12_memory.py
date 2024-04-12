from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv, find_dotenv
import os

#  memory를 사용해야하는 이유?
#  -> 단발설 질문/답변이 아닌 채팅(지속적인 기록)을 하기 위해
#  -> LLM 모데에는 메모리가 없음(대화기록 저장을 할수가 없음)
#  1. 우리가 자체적으로 Memory에 대화기록을 저장
#  2. 대화기록을 질문과 함께 전달
#  * LangChain에서 제공하는 메모리 종류는 4개
#  * 기존 LLM 모델의 API에서는 대부분 메모리기능 지원X
#  * 2023년 11월 OpenAI API에도 메모리 기능 추가! 

_ = load_dotenv(find_dotenv())

llm = ChatOpenAI(
    openai_api_key =os.getenv("OPENAI_API_KEY"),
    temperature=0.1
)


#  대화 내용기록 => 전체 저장(Best) => 메모리 비효율적 낭비
# - ConversationSummaryBufferMemory
# - 설정한 최대 토큰까지는 모든 대화 내용 저장!
#  - 설정한 최대 토큰 넘어가는 경우! 가장 오래된 대화부터 요약

# return_message=True
#  - Memory는 Return 2가지 Type으로 전달
#  - return_message=True 옵션을 주면 Message Class로 받음(채팅으로 활용)
#  - False이면 Text로 출력

memory = ConversationSummaryBufferMemory(
    llm = llm,
    max_token_limit=120,
    memory_key="history",
    return_messages=True,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpfoul AI talking to a human"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ]
)

chain = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)

chain.predict(question="My name is jihoo park")
chain.predict(question="I live in GwangJu")
chain.predict(question="What is my name?")
# Memory에 대화기록을 가져오는데, 마지막 질문에 대한 답변이 나오지않음
chain.predict(question="?")
