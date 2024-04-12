from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate # chatprompttemplate 추가되었음
import os # 모델의 키를 연동하기위함
from dotenv import load_dotenv, find_dotenv
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.example_selector.base import BaseExampleSelector 

# Fewshot Learning
# - 기존학습이 완료된 모델에 조금 더 학습시키는 것
# - 모델에게 생성하는 대답의 예제를 전달
# - 기본저인 messages(system)을 활용한 엔지니어링보다 훨씬 더 강력한 성능을 보임
# - 즉, prompt 작성보다 예제를 보여주는 fewshot이 훨씬 더 좋음
# - 대화기록 등 DB에서 가져와서 fewshot 사용


_ = load_dotenv(find_dotenv())

chat = ChatOpenAI(
    openai_api_key =os.getenv("OPENAI_API_KEY"),
    # temperature: 0.1~1.0 : 0에 가까울수록 사실기반, 1에 가까울수록 창의력
    temperature=0.1,
    streaming=True,  # 그전 질문과의 연결? 어떤 답변을 원하는지 확률적으로 계산하여 보여주는데, streaming은 답변을 생성하는 과정을 시각화 가능하게 하는 설정
    callbacks=[StreamingStdOutCallbackHandler()]
)


# fewshot 예제
examples = [
    {
        "question": "What do you know about France?",
        "answer": """        Here is what I know:        Capital: Paris        Language: French        Food: Wine and Cheese        Currency: Euro        """,
    },
    {
        "question": "What do you know about Italy?",
        "answer": """        I know this:        Capital: Rome        Language: Italian        Food: Pizza and Pasta        Currency: Euro        """,
    },
    {
        "question": "What do you know about Greece?",
        "answer": """        I know this:        Capital: Athens        Language: Greek        Food: Souvlaki and Feta Cheese        Currency: Euro        """,
    },
]


# RandomSelector 설계
class RandomExampleSelector(BaseExampleSelector):
    def __init__(self, examples):
        self.examples = examples
    
    def add_example(self, example):
        self.examples.append(example)
    
    def select_examples(self, input_variables):
        from random import choice
        return [choice(self.examples)]
    
# RandomSelector 생성
example_selector = RandomExampleSelector(examples=examples)





example_prompt = PromptTemplate.from_template(
    "Human: {question}\nAI:{answer}"
)

prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
#    examples=examples, 전체 예제 모두 활용
    example_selector=example_selector, # 랜덤하게 예제 선택 활용
    suffix="Human: What do you know about {country}?",
    input_variables=["country"],
)

chain = prompt | chat
result = chain.invoke({
    "country" : "Japan"
})

print(result)