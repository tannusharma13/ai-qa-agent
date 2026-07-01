import os
import random
import time

from dotenv import load_dotenv
from google import genai

from config.logger import logger

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-2.5-flash"


def ask_ai(prompt: str, retries: int = 5) -> str:
    """
    Sends a prompt to Gemini with automatic retry
    using exponential backoff.
    """

    for attempt in range(retries):

        try:

            logger.info(
                f"Sending request to Gemini "
                f"(Attempt {attempt + 1}/{retries})"
            )

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            if attempt > 0:
                logger.info(
                    f"Gemini request succeeded on retry {attempt + 1}"
                )

            logger.info("Gemini response received successfully.")

            return response.text

        except Exception as e:

            logger.warning(
                f"Gemini Error ({attempt + 1}/{retries})"
            )

            logger.warning(str(e))

            if attempt == retries - 1:

                logger.error(
                    "Maximum retries reached. Gemini request failed."
                )

                raise

            wait = (5 * (2 ** attempt)) + random.uniform(0, 2)

            logger.info(
                f"Retrying in {wait:.1f} seconds..."
            )

            time.sleep(wait)