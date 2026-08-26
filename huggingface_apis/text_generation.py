from transformers import pipeline
import torch

class ChatMemory():
    def __init__(self):
        self.messages = [{"role": "user", "content": "Your creator is Rishav Sarkar. Student of IIIT Kalyani."}]

    def add_message(self, role, content):
        self.messages.append({
            "role": role,
            "content": content
        })

    def get_messages(self):
        return self.messages

chat_memory = ChatMemory()


qwen_model_id = "Qwen/Qwen2.5-0.5B-Instruct"

qwen_pipe = pipeline(
    "text-generation",
    model=qwen_model_id,
    dtype=torch.bfloat16,
    device_map="auto",
)

def generate_text_response(message):
    try:
        chat_memory.add_message("user", message)
        text_outputs = qwen_pipe(
            chat_memory.get_messages()[-10:],
            temperature=0.01,
            max_new_tokens=180
        )
        text_response = text_outputs[0]['generated_text'][-1]['content']
        chat_memory.add_message("system", text_response)

        return str(text_response)
    except Exception as e:
        print(e)
        return "An unexpected error occurred"