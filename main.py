from flask import Flask, render_template, request
from groq import Groq
from database import init_db, save_draft, get_drafts
from config import GROQ_API_KEY

app = Flask(__name__)
app.config['JSON_AAS_ASCII'] = False

init_db()

client = Groq(api_key=GROQ_API_KEY)


@app.route("/", methods=["GET", "POST"])
def home():

    generated_email = ""

    if request.method == "POST":

        bullets = request.form.get("bullets")
        industry = request.form.get("industry")
        tone = request.form.get("tone")

        prompt = f"""
        You are an expert cold outreach email writer.

        Generate a {tone} outreach email for the {industry} industry.

        Context:
        {bullets}

        Make the email concise, human, and professional.
        Return only the email itself with no explanation or commentary.
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        generated_email = response.choices[0].message.content
        save_draft(industry, tone, bullets, generated_email)

    return render_template(
        "index.html",
        generated_email=generated_email,
        drafts=get_drafts()
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)