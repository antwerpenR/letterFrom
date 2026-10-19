import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
key = os.environ["NANOGPT_API_KEY"]
for base in ["https://api.nano-gpt.com/api/v1", "https://nano-gpt.com/api/v1"]:
    try:
        c = OpenAI(api_key=key, base_url=base)
        n = len(c.models.list().data)
        print("OK  ", base, "->", n, "models")
        r = c.embeddings.create(model="text-embedding-3-small", input=["test"])
        print("     embeddings OK, dim =", len(r.data[0].embedding))
        break
    except Exception as e:
        print("FAIL", base, type(e).__name__, str(e)[:160])
