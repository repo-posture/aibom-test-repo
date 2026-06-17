import cohere

co = cohere.Client()

# Models: command-r-plus, command-r, command


def chat_command_r_plus(prompt: str) -> str:
    response = co.chat(model="command-r-plus", message=prompt)
    return response.text


def chat_command_r(prompt: str) -> str:
    response = co.chat(model="command-r", message=prompt)
    return response.text


def chat_command(prompt: str) -> str:
    response = co.chat(model="command", message=prompt)
    return response.text
