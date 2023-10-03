from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai
from mangum import Mangum
import os

openai.api_key = os.environ['OPEN_AI_KEY']

app = FastAPI()

origins = [
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
    return {"message": "Code was updated"}

# Endpoint to Conduct Market Research In Open AI
@app.get('/market-research/{company_name}')
def market_research(company_name):
    system_template = generateMarketingSystemTemplate()
    human_template = generateMarketingPrompt(company_name)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=1000,
        messages=[
            {"role": "system", "content": system_template},
            {"role": "user", "content": human_template}
        ]
    )
    return response

# Generate Human Prompt based on the company named provided
def generateMarketingPrompt(company_name):
    template = """Conduct competitive marketing research on {company_name}. I want to know what is their competitive advantage, 
    what customers dislike and like about the product and who are their biggest competitors.\nWhat is {company_name} competitive advantage?\n
    What are customers dislikes and likes about {company_name} products?\nWho are {company_name} 
    biggest competitors?\nWhat are the opportunities and threats within a given market or industry?"""
    return template.format(company_name=company_name)

# Generate System Template, help open ai to give a better response
# By giving them a persona of an intelligent market expert
def generateMarketingSystemTemplate():
    return "You are an intelligent marketing expert, task with conducting competitive market research."

handler = Mangum(app)