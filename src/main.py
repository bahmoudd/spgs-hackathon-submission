from dotenv import dotenv_values
from openai import OpenAI

API_KEY = dotenv_values(".env")["API_KEY"]
MODEL = dotenv_values(".env")["MODEL"]

client = OpenAI(
    api_key = API_KEY
)

def question_and_answer(instructions: str):
    response = client.response.create(
        model = MODEL,
        instructions = instructions,
        input = input("Your response: ")
    )
    return response
    

response = client.responses.create(
    model = MODEL,
    instructions = "You are an AI assistant designed to help user conserve household water usage, to save the environment and to cut down on people's water bills. The first question which you must ask the user is 'How many cups of tea do you have in a day?' - rephrase this question to be more friendly and less direct. The user will start with 'Hello, Aqua' - please introduce yourself in depth but not too much in depth - just briefly. Separate the introduction from the question with a newline character. For all questions - remember what the user says in response to you - this will be important for the final calculation of water consumption. Don't be too direct with the questions.",
    input = "Hello, Aqua"
)

question_and_answer("Ask the user how much they spend on their water bill per month in pounds sterling")
question_and_answer("Ask the user if they shower or if they bathe - not too directly.")
question_and_answer("If the user has said shower, ask them how long they shower for on average (as a rough estimate). If the user has said bath, remember that they consumed around 80 litres of water. Ask them how often they bathe instead.")
question_and_answer("Ask the user how often they use the dishwasher")
question_and_answer("Ask how long each dishwasher cycle is")
question_and_answer("Ask if the user's dishwasher has an eco mode and if they use it")
question_and_answer("Ask the user how often they use the washing machine")
question_and_answer("Ask how long each wash cycle is")
question_and_answer("Ask if the user's washing machine has an eco mode and if they use it")
question_and_answer("Ask the user if they have a dual-flush toilet")
question_and_answer("Ask the user if they have a garden or any plants, and if so, ask how much water they use when watering them and how often they water their plants.")

response = client.responses.create(
    model = MODEL,
    instruction = "Okay, given all the answers to the questions that the user has given you, give the user a detailed list of tips on how they can save water. Also, give them the potential amount that they could save from the initial spending amount that they've given you, as a nominal pounds sterling amount."
)
