import os
import hashlib
import json
import openai
import ollama


CACHE_FILE = "gpt_cache.json"
MODEL_NAME = "codellama"  # or llama3, mistral, etc.
CACHE = {}

def load_cache():
    global CACHE
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            CACHE = json.load(f)
    else:
        CACHE = {}

def save_cache():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(CACHE, f, indent=2)

def get_code_hash(code: str) -> str:
    return hashlib.sha256(code.encode()).hexdigest()

def summarize_code(code: str, type_: str, name: str) -> str:
    code_hash = get_code_hash(code)
    if code_hash in CACHE:
        return CACHE[code_hash]
   
    prompt = f"Summarize the following {type_} called '{name}' in a clear, concise way for documentation:\n\n```python\n{code}\n```"

    # === Try OpenAI First
    try:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a senior developer writing helpful technical documentation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        summary = response.choices[0].message.content.strip()
        CACHE[code_hash] = summary
        save_cache()
        return summary

    except openai.OpenAIError as e:
        print(f"⚠️ OpenAI failed, falling back to Ollama: {e}")

    # === Fallback to Ollama
    try:
        response = ollama.chat(
            model=MODEL_NAME,  # e.g., "codellama" or "llama3"
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        summary = response['message']['content'].strip()
        CACHE[code_hash] = summary
        save_cache()
        return summary

    except Exception as e:
        return f"Error generating summary via OpenAI or Ollama: {e}"

