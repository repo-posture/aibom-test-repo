import anthropic

client = anthropic.Anthropic()

# Models: claude-3-5-sonnet-20241022, claude-3-opus-20240229, claude-3-haiku-20240307


def chat_sonnet(prompt: str) -> str:
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def chat_opus(prompt: str) -> str:
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def chat_haiku(prompt: str) -> str:
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text
