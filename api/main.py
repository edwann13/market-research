from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai
# from langchain.prompts import PromptTemplate
# from langchain.llms import OpenAI
# from langchain.chat_models import ChatOpenAI
# from langchain.prompts.chat import ChatPromptTemplate
from mangum import Mangum


# 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
openai.api_key = "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"

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    # print(openai)
    # print(FastAPI)
    # print(prompts)
    # print(generateMarketingPrompt('test comapny'))
    return {"message": "Code was updated"}

@app.get('/test')
def test():
    system_template = generateMarketingSystemTemplate()
    human_template = generateMarketingPrompt('el aviso')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=1000,
        messages=[
            {"role": "system", "content": system_template},
            {"role": "user", "content": human_template}
        ]
    )
    print(response)
    return response
# @app.get("/lang")
# def langChain():
#     system_template = generateMarketingSystemTemplate()
#     human_template = generateMarketingPrompt("involve.ai")
#     chat_prompt = ChatPromptTemplate.from_messages([
#         ('system', system_template),
#         ('human', human_template)
#     ])
#     chain = chat_prompt | ChatOpenAI(openai_api_key="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", max_tokens=1000)
#     response = chain.invoke({})
#     return response

def generateMarketingPrompt(company_name):
    # text = "Conduct competitive marketing research on {company_name}. I want to know what is their competitive advantage, what customers dislike and like about the product and who are their biggest competitors.\nWhat is {company_name} competitive advantage?\nWhat are customers dislikes and likes about {company_name} products?\nWho are {company_name} biggest competitors?\nWhat are the opportunities and threats within a given market or industry?"
    # prompt = PromptTemplate.from_template(text)
    # return prompt.format(company_name=company_name)
    template = """Conduct competitive marketing research on {company_name}. I want to know what is their competitive advantage, what customers dislike and like about the product and who are their biggest competitors.\nWhat is {company_name} competitive advantage?\nWhat are customers dislikes and likes about {company_name} products?\nWho are {company_name} 
        biggest competitors?\nWhat are the opportunities and threats within a given market or industry?"""
    return template.format(company_name=company_name)

def generateMarketingSystemTemplate():
    return "You are an intelligent marketing expert, task with conducting competitive market research."

handler = Mangum(app)