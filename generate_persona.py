import requests
import json
import logging
import re

def generate_persona(data, groq_api_key, username):
    endpoint = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    sample_data = data[:30]

    prompt = (
        "You are a professional UX researcher. Based on the Reddit user data below, "
        "generate EXACTLY ONE structured user persona using the strict format provided.\n\n"

        "RULES:\n"
        f"- The Reddit username of this user is: '{username}'. Use this as NAME unless an actual name is explicitly stated.\n"
        "- Do NOT fabricate or randomly guess demographic details.\n"
        "- If Name, Age, Location, Occupation, or Status are unclear, output 'Unknown' or 'Not explicitly mentioned'.\n"
        "- If there are behavioral patterns that suggest likely occupation, activity tier, or archetype, explain them using careful, cautious language like 'Likely', 'Appears to', or 'Probably'.\n"
        "- Avoid stating anything with certainty unless directly evident in the posts/comments.\n"
        "- Cite specific Reddit post/comment URLs as evidence wherever possible.\n"
        "- STOP after completing exactly ONE persona.\n\n"

        "PERSONALITY RULES:\n"
        "- EXTROVERSION / INTROVERSION: Briefly explain whether the user's interaction style, tone, or content suggests a more extroverted or introverted personality. If no clear evidence exists, provide a neutral observation about their engagement style (without saying 'unclear').\n"
        "- INTUITION / SENSING: Briefly explain whether the user tends to focus on big-picture thinking, possibilities, and ideas (intuition), or concrete details, facts, and practical matters (sensing), based on their Reddit activity. If no strong pattern is observed, state that their communication balances both abstract and practical focus.\n"
        "- THINKING / FEELING: Comment on whether the user tends to prioritize logic, analysis, and structured responses (thinking), or personal values, empathy, and subjective considerations (feeling), based on their writing style or content choices. If not obvious, describe their communication as neutral or pragmatic.\n"
        "- PERCEIVING / JUDGING: Assess whether the user appears flexible, exploratory, and open-ended in their discussions (perceiving), or structured, opinionated, and goal-driven (judging). If inconclusive, describe their interaction style as balanced or situational.\n"
        "- After each personality trait, cite specific Reddit activity where possible.\n"
        "- (Note: Do not mention 'unclear' anywhere. Always provide a neutral descriptive sentence when unsure.)\n\n"


        "CITATION REQUIREMENT:\n"
        "- In BEHAVIOUR & HABITS, FRUSTRATIONS, and GOALS & NEEDS sections, every point MUST include a real Reddit post/comment URL from the provided data, even if the evidence is partial or speculative.\n"
        "- Use URLs in every point, without exception. If no URLs are usable for a given section, omit the entire section.\n"
        "- Do NOT omit individual points to avoid citation; ensure all included insights are backed by Reddit URLs.\n"
        "- If no supporting URL exists for a point, omit that point.\n\n"

        "FORMAT:\n\n"

        f"NAME: {username}\n"
        "AGE: (Exact, estimated with justification, or 'Unknown')\n"
        "OCCUPATION: (Clearly stated, reasonably inferred, or 'Unknown')\n"
        "STATUS: (If relationship status is mentioned, else 'Unknown')\n"
        "LOCATION: (If mentioned, else 'Unknown' or 'Not explicitly mentioned')\n"
        "TIER: (Summarize based on Reddit activity level: Casual / Regular / Heavy Contributor)\n"
        "ARCHETYPE: (Describe behavioral archetype based on Reddit participation)\n\n"

        "----------------------------------------\n\n"

        "MOTIVATIONS:\n"
        "- \n"
        "- \n"
        "- \n\n"

        "PERSONALITY:\n"
        "- (Reason: Explain with evidence, or state 'Unclear')\n"
        "- (Reason: Explain with evidence, or state 'Unclear')\n"
        "- (Reason: Explain with evidence, or state 'Unclear')\n"
        "- (Reason: Explain with evidence, or state 'Unclear')\n\n"

        "----------------------------------------\n\n"

        "BEHAVIOUR & HABITS:\n"
        "- (Cite specific Reddit posts/comments as evidence)\n"
        "- \n"
        "- \n\n"

        "FRUSTRATIONS:\n"
        "- (Cite specific Reddit posts/comments as evidence)\n"
        "- \n"
        "- \n\n"

        "GOALS & NEEDS:\n"
        "- (Cite specific Reddit posts/comments as evidence)\n"
        "- \n"
        "- \n\n"

        f"Here is the Reddit user data:\n{json.dumps(sample_data)}"
    )

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a professional UX researcher creating clear personas."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 3000
    }

    logging.info("Sending request to Groq API...")

    response = requests.post(endpoint, headers=headers, json=payload)
    
    if response.status_code != 200:
        logging.error(f"Groq API Error: {response.status_code} {response.text}")
        response.raise_for_status()

    persona_text = response.json()['choices'][0]['message']['content'].strip()
    return persona_text

def sanitize_persona_output(persona_text):
    fields = ['NAME', 'AGE', 'OCCUPATION', 'STATUS', 'LOCATION']

    for field in fields:
        pattern = rf"{field}:\s*(.*)"
        match = re.search(pattern, persona_text, re.IGNORECASE)
        
        if match:
            value = match.group(1).strip()
            if value.lower() in ['unknown', 'not specified', 'n/a', 'na']:
                continue
            if field == 'NAME' and ('user' not in value.lower() and len(value.split()) <= 2):
                continue
            if value == '' or len(value.split()) > 3 or any(char.isdigit() for char in value):
                persona_text = re.sub(pattern, f"{field}: Unknown", persona_text)
    
    return persona_text

def save_persona(persona_text, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(persona_text)

    logging.info(f"Persona saved to {output_path}")
