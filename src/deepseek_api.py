from openai import OpenAI

class DeepSeekAPI:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    def generate_response(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an assistant specialized in answering game-related questions."},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content