from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model = 'gemini-pro', google_api_key = GEMINI_API_KEY)


def generate_rasturants_names_and_items(cuisine):

    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template = "I want to open a rasturant for {cuisine} food. Suggest a fency name of my rasturant. Suggest only one name without giving its description."
    )

    name_chain = LLMChain(llm=llm, prompt = prompt_template_name, output_key='rasturant_name')

    prompt_template_items = PromptTemplate(
        input_variables=['rasturant_name'],
        template = "Suggest some menu items for {rasturant_name}. Just return menu items without giving its description. Menu Items must categorized in 'Appetizers', 'MainCourse', 'Sides', 'Desserts'."
    )

    items_chain = LLMChain(llm=llm, prompt = prompt_template_items, output_key='menu_items')

    chain = SequentialChain(
        chains = [name_chain, items_chain],
        input_variables = ['cuisine'],
        output_variables = ['rasturant_name', 'menu_items']
    )

    return chain({'cuisine': cuisine})


if __name__ == '__main__':
    response = generate_rasturants_names_and_items('Indian')
    print(response)
