import ollama

client = ollama.Client(host="http://127.0.0.1:11434")

resp = client.chat(
    model="gemma3:1b",
    messages=[{"role": "user", "content": "Halo, siapa penemu mobil?"}]
)

print(resp["message"]["content"])
