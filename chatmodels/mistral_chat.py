from mistralai import Mistral

client = Mistral(api_key="MISTRAL_API_KEY")

# Models: mistral-large-latest, mistral-small-latest, open-mixtral-8x7b


def chat_large(prompt: str) -> str:
    response = client.chat.complete(
        model="mistral-large-latest",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def chat_small(prompt: str) -> str:
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def chat_mixtral(prompt: str) -> str:
    response = client.chat.complete(
        model="open-mixtral-8x7b",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
