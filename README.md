# ColdCraft

An AI-powered cold outreach email generator built with Python and Flask. Enter your context,
select your industry and tone, and get a professional email instantly. All drafts are saved 
automatically.


## Features 

- AI generated emails powered by Groq
- Industry selector - Sales, Freelance, Real Estate, Marketing 
- Tone selector - Professional, Warm, Confident, Persuasive
- Saves all drafts automatically to a local SQLite database
- One click copy button for every email
- Clean dark web interface


## Tech Stack

- Python
- Flask
- Groq AI API (llama-3.3-70b-versatile)
- SQLite
- HTML/CSS


## Setup 

1. Clone the repository 
```
git clone https://github.com/dashya-bit9/coldcraft.git
```

2. Create and activate a virtual environment 
```
python3 -m venv venv
source venv/bin/activate
```

> On Windows use: `venv\Scripts\activate`

3. Install dependencies
```
pip install -r requirements.txt
```

4. Rename `config.example.py` to `config.py` and add your API key

```
GROQ_API_KEY="your_groq_api_key_here"
```

5. Run the app
```
python3 main.py
```

6. Open your browser and go to:
```
http://127.0.0.1:5000
```


## Usage

1. Enter bullet points or context about your outreach in the text box
2. Select your industry and tone
3. Click generate Email
4. Copy the generated email with one click
5. All emails are saved automatically in the Saved Drafts section below 
