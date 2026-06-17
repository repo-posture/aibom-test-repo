const Anthropic = require("@anthropic-ai/sdk");

const client = new Anthropic();

// Models: claude-3-5-sonnet-20241022, claude-3-opus-20240229, claude-3-haiku-20240307

async function chatSonnet(prompt) {
  return client.messages.create({
    model: "claude-3-5-sonnet-20241022",
    max_tokens: 1024,
    messages: [{ role: "user", content: prompt }],
  });
}

async function chatOpus(prompt) {
  return client.messages.create({
    model: "claude-3-opus-20240229",
    max_tokens: 1024,
    messages: [{ role: "user", content: prompt }],
  });
}

async function chatHaiku(prompt) {
  return client.messages.create({
    model: "claude-3-haiku-20240307",
    max_tokens: 512,
    messages: [{ role: "user", content: prompt }],
  });
}

module.exports = { chatSonnet, chatOpus, chatHaiku };
