from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

model_path = "/Users/michaelstahle/AI-Models/Llama-3.3-70B-Instruct-4bit"

from mlx_lm import load, generate
Can 
model, tokenizer = load(model_path)

while True:
    user_input = input("Enter prompt (or 'end session' to quit): ")
    if user_input.strip().lower() == "end session":
        break
    
    if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
        messages = [{"role": "user", "content": user_input}]
        prompt = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
    else:
        prompt = user_input

    response = generate(model, tokenizer, prompt=prompt, verbose=True)
    print(response)

print("Session ended.")