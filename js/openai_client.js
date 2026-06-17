const OpenAI = require("openai");

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// Models: gpt-4o, gpt-4, gpt-3.5-turbo, text-embedding-3-small, text-embedding-3-large

async function chatGpt4o(prompt) {
  return client.chat.completions.create({
    model: "gpt-4o",
    messages: [{ role: "user", content: prompt }],
  });
}

async function chatGpt4(prompt) {
  return client.chat.completions.create({
    model: "gpt-4",
    messages: [{ role: "user", content: prompt }],
  });
}

async function chatGpt35(prompt) {
  return client.chat.completions.create({
    model: "gpt-3.5-turbo",
    messages: [{ role: "user", content: prompt }],
  });
}

async function embedSmall(text) {
  return client.embeddings.create({ model: "text-embedding-3-small", input: text });
}

async function embedLarge(text) {
  return client.embeddings.create({ model: "text-embedding-3-large", input: text });
}

module.exports = { chatGpt4o, chatGpt4, chatGpt35, embedSmall, embedLarge };
