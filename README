# Reddit User Persona Generator

This project analyzes a Reddit user's activity and generates a structured, source-cited **user persona** using AI models.
It fetches Reddit comments and posts via Reddit API, then uses Groq's LLaMA3 API to generate the persona.

---

## 📦 Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/reddit-persona-generator.git
cd reddit-persona-generator
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Set Up API Keys

* Rename `.env.sample` to `.env`:

```
cp .env.sample .env
```

* Edit `.env` and add your API credentials:

```
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_custom_user_agent
GROQ_API_KEY=your_groq_api_key
```

⚠️ **Note:** Do not share your actual keys publicly. `.env` is included in `.gitignore` for security.

---

## 🚀 Running the Program

```
python main.py --username <reddit_username>
```

Example:

```
python main.py --username kojied
```

Each execution will create separate output files per user.

---

## 📤 Outputs

* `outputs/<username>_user_data.json`: Fetched Reddit posts/comments.
* `outputs/<username>_persona_output.txt`: Generated structured persona, source-cited.

---

## 📁 Repository Structure

```
.env.sample
.gitignore
fetch_data.py
generate_persona.py
main.py
README.md
requirements.txt
outputs/
├── kojied_user_data.json
├── kojied_persona_output.txt
```

---

## ⚙️ Features

* Fetches Reddit user data (posts/comments).
* Persona generated using LLaMA3 model via Groq API.
* Cites real Reddit URLs for transparency.
* Handles:

  * Deleted or suspended accounts.
  * Inactive accounts (no posts/comments).
* Basic rate-limiting protection.

---

## 🛡️ Security Consideration

* Your Reddit API and Groq API keys remain local, secured via `.env`.
* Do not expose `.env` in any public repositories.
* `.env.sample` indicates required environment variables.

---

## 📊 Sample Persona Output Includes:

* **NAME**, **AGE**, **OCCUPATION**, **STATUS**, **LOCATION**
* **TIER**, **ARCHETYPE**
* **MOTIVATIONS**
* **PERSONALITY** (with reasoning)
* **BEHAVIOUR & HABITS** (with Reddit URL citations)
* **FRUSTRATIONS**
* **GOALS & NEEDS**
