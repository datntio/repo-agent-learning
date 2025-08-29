from openai import OpenAI
client = OpenAI()

prompt = "Viết một hàm Python tính giai thừa"
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)
print(resp.choices[0].message.content)
