from groq import Groq

from app.core.config import settings


class GroqClient:
    """
    Wrapper around the Groq SDK.
    """

    def __init__(self):

        self.client = Groq(api_key=settings.groq_api_key,)

        self.model = settings.groq_model

    def generate(self,prompt: str,) -> str:

        """
        Generate a response from the LLM.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content