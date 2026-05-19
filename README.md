# Reddit User Persona Generator

AI-powered behavioral persona generation from Reddit activity using Reddit APIs, prompt engineering, and LLM-based inference.

This project collects a Reddit user's public posts/comments, analyzes behavioral patterns, and generates a structured UX-style persona backed by real Reddit citations.

Unlike basic sentiment scripts or keyword summaries, this system attempts to synthesize:

- behavioral tendencies
- motivations
- frustrations
- interaction patterns
- likely archetypes
- communication style

while explicitly separating **observed evidence** from **inferred traits**.

---

## ✨ Why This Project Is Interesting

Most Reddit analysis tools stop at:

- sentiment analysis
- keyword frequency
- subreddit statistics

This project goes further by combining:

- large-scale Reddit activity collection
- structured prompt engineering
- behavioral inference
- evidence-backed persona generation
- hallucination constraints
- post-processing sanitization

to simulate a lightweight AI-powered UX research workflow.

The result feels closer to a **digital ethnography tool** than a simple scraper.

---

## 🧠 What the System Does

Given a Reddit username, the pipeline:

1. Fetches the user's public Reddit activity
2. Extracts comments and submissions
3. Structures the data into JSON
4. Sends behavioral context to an LLM
5. Generates a structured persona
6. Attaches supporting Reddit citations
7. Sanitizes potentially fabricated demographic claims
8. Saves outputs locally

---

## 🏗️ System Architecture

```
Reddit API (PRAW)
        ↓
User Posts + Comments
        ↓
JSON Structuring
        ↓
Prompt Engineering Layer
        ↓
Groq LLaMA 3.1 Inference
        ↓
Persona Post-Processing
        ↓
Structured Persona Output
```

---

## ⚙️ Features

### 🔍 Reddit Behavioral Analysis

- Fetches Reddit posts and comments
- Supports large activity histories
- Handles inactive/suspended/deleted accounts gracefully

### 🧠 AI Persona Generation

Generates structured personas including:

- motivations
- frustrations
- personality traits
- engagement patterns
- behavioral archetypes
- inferred interaction style

### 🔗 Evidence-Based Inference

The model is instructed to:

- cite real Reddit URLs
- avoid unsupported demographic claims
- distinguish inference from certainty
- avoid fabricating identity information

### 🛡️ Hallucination Mitigation

The pipeline includes:

- constrained prompt formatting
- explicit inference rules
- demographic sanitization
- citation requirements
- uncertainty handling

### ⏱️ Rate Limiting Protection

Basic request throttling is included to reduce Reddit API abuse risk.

---

## 📦 Tech Stack

| Component              | Technology           |
| ---------------------- | -------------------- |
| Reddit API Wrapper     | PRAW                 |
| LLM Inference          | Groq API             |
| Model                  | LLaMA 3.1 8B Instant |
| Environment Management | python-dotenv        |
| Language               | Python 3.10+         |

---

## 📁 Project Structure

```
reddit-user-persona-generator/
│
├── fetch_data.py
├── generate_persona.py
├── main.py
├── requirements.txt
├── .env.sample
├── .gitignore
├── README.md
│
├── user_data_<username>.json
└── persona_output_<username>.txt
```

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/reddit-user-persona-generator.git
cd reddit-user-persona-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy the sample environment file:

```bash
cp .env.sample .env
```

Add your credentials:

```env
CLIENT_ID=your_reddit_client_id
CLIENT_SECRET=your_reddit_client_secret
USER_AGENT=your_custom_user_agent
GROQ_API_KEY=your_groq_api_key
```

---

## 🔑 API Requirements

### Reddit API Credentials

Create an app at: [Reddit Apps Dashboard](https://www.reddit.com/prefs/apps)

Required:

- client ID
- client secret
- user agent

### Groq API Key

Generate a key from: [Groq Console](https://console.groq.com)

---

## ▶️ Usage

Run the generator:

```bash
python main.py --username <reddit_username>
```

Example:

```bash
python main.py --username kojied
```

Optional arguments:

```bash
python main.py --username kojied --max_items 500
```

---

## 📤 Output Files

### 1. Raw Reddit Activity

**File:** `user_data_<username>.json`

Contains:

- comments
- submissions
- permalinks
- extracted Reddit activity

### 2. Generated Persona

**File:** `persona_output_<username>.txt`

Contains:

- inferred archetype
- motivations
- frustrations
- personality analysis
- behavioral habits
- supporting Reddit citations

---

## 🧪 Example Persona Snippet

```
ARCHETYPE: Strategic Thinker / Problem Solver

PERSONALITY:
- Appears highly analytical and detail-oriented based on repeated
  long-form strategic discussions in gaming communities.

FRUSTRATIONS:
- Expresses dissatisfaction with shallow game progression systems.
  Evidence:
  https://reddit.com/example-link

GOALS & NEEDS:
- Seeks deeper strategic engagement and meaningful discussion.
```

---

## 🧠 Prompt Engineering Design

The project intentionally uses strict prompting rules to improve reliability.

The model is instructed to:

- avoid guessing demographics
- use uncertainty language
- cite supporting evidence
- avoid unsupported conclusions
- generate exactly one persona
- separate observation from inference

This significantly improves output consistency compared to naive prompting.

---

## 🛡️ Limitations & Ethical Considerations

This project performs behavioral inference from public online activity.

**Important limitations:**

- Personas are probabilistic, not factual identities
- Reddit activity may not represent a user's real-life behavior
- LLM outputs may still contain inaccuracies
- Personality inference is inherently subjective
- Sparse user histories reduce reliability

**This tool should NOT be used for:**

- hiring decisions
- surveillance
- profiling individuals without consent
- high-stakes evaluation

**This project is intended for:**

- educational purposes
- UX research experimentation
- behavioral analysis exploration
- AI prompt-engineering research

---

## 📈 Future Improvements

Planned enhancements:

- subreddit clustering
- sentiment trend analysis
- embedding-based behavioral grouping
- personality trait scoring
- temporal behavior analysis
- Streamlit web interface
- vector memory for long histories
- multi-persona generation modes
- export to PDF/dashboard format

---

## 🔬 Example Research/UX Use Cases

Potential applications include:

- UX audience research
- community behavior analysis
- online identity studies
- AI-assisted ethnography
- social interaction analysis
- digital sociology experiments

---

## 🛠️ Error Handling

The system currently handles:

- deleted Reddit users
- suspended accounts
- inaccessible profiles
- empty activity histories
- missing environment variables
- API request failures

---

## 🔒 Security Notes

- API keys remain local via `.env`
- `.env` is excluded using `.gitignore`
- No user authentication data is stored
- Only publicly available Reddit activity is analyzed

**Never commit secrets to GitHub.**

---

## 📚 Dependencies

Main libraries:

- praw
- requests
- python-dotenv

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Pull requests and improvements are welcome.

**Potential contribution areas:**

- better inference validation
- prompt optimization
- UI/dashboard layer
- analytics visualizations
- model benchmarking
- ethical safeguard improvements

---

## 📄 License

MIT License

---

## ⭐ Final Note

This project is fundamentally an experiment in combining:

- behavioral data collection
- structured prompting
- inference control
- evidence-backed AI generation

into a lightweight automated UX research pipeline.

The interesting part is not simply "using an LLM," but designing a system that attempts to balance:

- insight
- uncertainty
- transparency
- evidence
- structure

within AI-generated human profiling.
