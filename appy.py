import streamlit as st
import requests

def get_quote():
    headers = {
        "Authorization": "Bearer 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",  # Ensure this is valid
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are a motivational coach."},
            {"role": "user", "content": "Give me a short motivational quote."}
        ]
    }

    r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

    try:
        data = r.json()

        # Check if "choices" exists in response
        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        else:
            return f"❌ API Error: {data.get('error', {}).get('message', 'Unknown error')}\n\nFull response:\n{data}"

    except Exception as e:
        return f"❌ Exception occurred: {e}"

# Streamlit UI
st.title("🔥 Daily Motivation")

if st.button("Get Quote"):
    quote = get_quote()
    st.write(quote)
