from groq import Groq
import json

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
    
    def _extract_json(self,content: str) -> dict:
        """
        Extract JSON content from an LLM response.
        """

        content = content.strip()

        if content.startswith("```json"):
            content = content.replace("```json", "", 1)

        if content.startswith("```"):
            content = content.replace("```", "", 1)

        if content.endswith("```"):
            content = content[:-3]

        return content.strip()
    
    def generate_json(self,prompt: str) -> str:
        """
        Generate a JSON response from the LLM.
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

        content = response.choices[0].message.content

        content = self._extract_json(content)

        return json.loads(content)