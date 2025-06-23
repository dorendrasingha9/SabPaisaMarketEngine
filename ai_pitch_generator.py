from openai import OpenAI
import os

# Initialize OpenAI client using the new SDK v1+
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_pitch(prospect):
    prompt = f"""
    Create a payment solution pitch for {prospect['Name']}, a {prospect['Type']} in the {prospect['Sector']} sector, based in {prospect['Location']}.
    Highlight why SabPaisa (with government ties and multi-bank channels) is a better option over PayU, Razorpay.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Or "gpt-4" if your API key supports it
        messages=[{"role": "user", "content": prompt}],  # ✅ Corrected syntax
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()
