from openai import OpenAI

client = OpenAI(api_key="API_KEY")

def summarize(title: str, abstract: str) -> str:
    system_prompt = "Summarize the following research paper abstract concisely."
    user_content = f"Title: {title}\n\nAbstract: {abstract}"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]
    )
    
    return response.choices[0].message.content
