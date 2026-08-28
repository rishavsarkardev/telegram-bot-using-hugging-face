# <a href="https://t.me">
  <img src="https://githubusercontent.com" width="32" height="32" alt="Telegram logo"/>
</a> Telegram AI Bot

## ✅ Purpose
This repository demonstrates a Telegram bot creation setup. It serves as an AI assistant that can maintain a conversation and generate images on demand, all powered by open-source Hugging Face models running locally.

## ❓ How It Works
The bot asynchronously listens for user inputs and commands via the `aiogram` framework. Regular text messages are passed to a local text-generation model that retains recent chat history for context. When the `/image` command is called, it triggers a diffusion pipeline to generate an image based on the prompt. The image is saved locally, sent to the user in the Telegram chat, and then immediately deleted from the server.

## 🤗 Hugging Face Models Used
* **Text Generation:** `Qwen/Qwen2.5-0.5B-Instruct`
* **Image Generation:** `stabilityai/sd-turbo`

## 🤔 Key Modules & Libraries
* `aiogram`
* `diffusers`
* `transformers`
* `torch`
* `asyncio`
