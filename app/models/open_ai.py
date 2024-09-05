from openai import OpenAI
import json


class OpenAiService:

    def __init__(self):
        self.client = OpenAI()

    def classify_products(self, data):
        foods = ['Vegetables', 'Fruits', 'Nuts', 'Animal', 'Dairy', 'Beverages', 'Pastries']
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user",
                     "content": f"Please provide a JSON list containing the information inside this {data} and classify them with one of the following types{foods}, just the JSON list."}
                ]
            )
            result = response.choices[0].message.content
            cleaned = result.strip('```json\n').strip('\n```')
            parsed_data = json.loads(cleaned)
            print(parsed_data)
            return parsed_data


        except Exception as e:
            print(f"An error occurred: {e}")
            return None
