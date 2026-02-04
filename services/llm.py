from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"]
)


def generate_answer(context, question):
    completion = client.chat.completions.create(
        model="Qwen/Qwen3-1.7B:featherless-ai",
        messages=[
            {
                "role": "user",
                "content": f"Context: {context}\nQuestion: {question}\nAnswer the question based on the context above."
            }
        ],
    )
    return completion.choices[0].message.content
