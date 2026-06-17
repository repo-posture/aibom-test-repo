const OpenAI = require("openai");

// JavaScript OpenAI usage — gpt-4 + text-embedding-3-small
// Covers: cross-language detection (JS support in AIBOM scanner)

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function chat(userMessage) {
  const response = await client.chat.completions.create({
    model: "gpt-4",
    messages: [{ role: "user", content: userMessage }],
  });
  return response.choices[0].message.content;
}

async function embed(text) {
  const response = await client.embeddings.create({
    model: "text-embedding-3-small",
    input: text,
  });
  return response.data[0].embedding;
}

module.exports = { chat, embed };
