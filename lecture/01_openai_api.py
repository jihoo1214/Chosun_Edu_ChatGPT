# openai api 사용하기
# - platform.openai.com
# 1. API-KET 발급
# 2. 카드 등록(visa, master) + 5.5달러(보유)


# 라이브러리 관리
# 1. VENV 가상환경
# 2. Anaconda 



# 챗봇 만들기
# - ChatGPT : 챗봇 서비스 이름(ex: 카카오톡)
# > 인공지능 모델 : GPT
# > 무료 : 3.5
# > 유료 : 4.0

# OPENai 회사에서 gpt 관련 api 제공
# https://openai.com/blog/openai-api


from openai import OpenAI
client = OpenAI(api_key="")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "클라우드 한국어로 설명해줘"}
  ]
)

print(completion.choices[0].message)

# openai의 api를 사용하는 챗봇 문제점
# 1. 개발의 어려움(난이도 상) -> 쉽게 개발할 수 있는 프레임워크 필요
# 2. 챗봇 개발 완성 -> 모델변경 -> 변경한 모델 api로 처음부터 개발 -> 모델이 바뀔때마다 어려워짐
# 3. --> Langchain 프레임워크 사용