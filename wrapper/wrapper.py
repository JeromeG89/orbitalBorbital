from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


class OpenAIWrapper:
    def __init__(self, api_key=None):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))

    def ask(self, prompt, model="gpt-3.5-turbo", system_prompt='''You are a nutrition expert specializing in Singaporean food. 
                                                               When given the name or description of a food item or dish 
                                                               (like 'chicken rice', 'char kway teow', or 'nasi lemak with extra sambal'),
                                                               estimate the total calories and give a breakdown of macronutrients 
                                                               (carbohydrates, protein, and fat) in grams. If the input is unclear 
                                                               or not a food item, say so politely. Output the result as JSON with keys:
                                                                'calories', 'carbohydrates', 'protein', 'fat'."):'''
            ):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        response = self.client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    wrapper = OpenAIWrapper()
    print(wrapper.ask("1 plate of laksa"))