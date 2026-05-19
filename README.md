# Reddit User Persona Generator

**A behavioral analysis pipeline combining Reddit data extraction, structured prompt engineering, and LLM-based inference with hallucination mitigation and evidence-backed persona generation.**

This project demonstrates core ML/data engineering patterns: data pipeline design, inference control, output validation, and behavioral analytics—applied to Reddit activity. Rather than a simple "LLM wrapper," this system focuses on the engineering challenges of **reliable behavioral inference at scale**: data normalization, constraint-based prompt design, citation binding, and post-processing validation.

---

## ✨ Key Features

- **Data Pipeline Architecture**: Normalized extraction from unstructured Reddit activity with temporal and community-aware context bucketing
- **Inference Control**: Constraint-based prompting and multi-layer post-processing validation to prevent hallucination
- **Evidence Binding**: Every persona claim includes traceable Reddit sources for auditability
- **Behavioral Pattern Recognition**: Community-specific interaction analysis with temporal consistency scoring
- **Output Reliability**: Citation validation, demographic claim filtering, and reproducibility across inference runs

---

## 🧠 System Architecture

```
Reddit API (PRAW)
        ↓
User Posts + Comments
        ↓
JSON Structuring & Normalization
        ↓
Context Vectorization
        ↓
Constrained Prompt Engineering
        ↓
Groq LLaMA 3.1 Inference
        ↓
Post-Processing & Validation
        ↓
Evidence-Backed Persona Output
```

---

## 🏛️ Core Engineering Patterns

### Hallucination Mitigation (Multi-Layer Approach)

**Problem:** LLMs fabricate demographics, make unsupported claims, and overfit to limited evidence.

**Solution Architecture:**

1. **Prompt-Level Constraints**
   - Explicit role definitions and behavioral analyst guidelines
   - Evidence-first formatting (observations precede inferences)
   - Uncertainty quantification rules ("likely," "probably," "unclear from data")
   - Citation requirements for every claim

2. **Structured Output Validation**
   - Post-processing regex patterns filter fabricated demographics
   - Age/gender/income removal if unsupported by evidence
   - Persona field schema enforcement
   - Citation URL validation against source data

3. **Behavioral Data Normalization**
   - Subreddit community classification
   - Temporal activity pattern detection
   - Sentiment consistency scoring
   - Engagement frequency bucketing

### Data Pipeline Design

**Challenge:** Reddit API returns unstructured activity; naive concatenation loses behavioral signal.

**Key Design Decisions:**
- Comments grouped by subreddit + temporal window (reveals community-specific behavior)
- Submissions weighted higher than comments (signal strength differentiation)
- Deleted/removed posts excluded (avoid spurious inference)
- Timestamp metadata preserved (enables temporal analysis)
- URL formatting standardized for citation validation

### Evidence Binding

Every persona claim includes Reddit source mapping:

```
CLAIM: User frustrated with game progression mechanics
EVIDENCE: https://reddit.com/r/gaming/comments/xyz
CONFIDENCE: observed (direct quote)
```

This separation enables validation and reduces confidence in inference-only claims.

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/your-username/reddit-user-persona-generator.git
cd reddit-user-persona-generator

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.sample .env
# Edit .env with your API credentials
```

### Configuration

**Reddit API Credentials** - Create an app at [Reddit Apps Dashboard](https://www.reddit.com/prefs/apps)

```env
CLIENT_ID=your_reddit_client_id
CLIENT_SECRET=your_reddit_client_secret
USER_AGENT=your_custom_user_agent
```

**Groq API Key** - Generate from [Groq Console](https://console.groq.com)

```env
GROQ_API_KEY=your_groq_api_key
```

### Usage

```bash
# Generate persona for a Reddit user
python main.py --username <reddit_username>

# Example
python main.py --username kojied

# Optional: specify max activity items
python main.py --username kojied --max_items 500
```

---

## 📤 Output Files

### Raw Data: `user_data_<username>.json`
Contains extracted Reddit activity:
- Comments with metadata
- Submissions with timestamps
- Permalinks for evidence binding
- Structured behavioral signals

### Generated Persona: `persona_output_<username>.txt`
Structured analysis including:
- Inferred archetype classification
- Behavioral motivations and frustrations
- Personality trait analysis
- Engagement patterns
- Supporting Reddit citations

### Example Output
```
ARCHETYPE: Strategic Thinker / Problem Solver

PERSONALITY:
- Appears highly analytical and detail-oriented based on repeated
  long-form strategic discussions in gaming communities.

FRUSTRATIONS:
- Expresses dissatisfaction with shallow game progression systems.
  Evidence: https://reddit.com/r/gaming/comments/example

GOALS & NEEDS:
- Seeks deeper strategic engagement and meaningful discussion.
```

---

## 📊 Evaluation Framework

### Current Metrics (Implemented)

- **Citation Coverage**: % of claims with supporting Reddit links (target: >85%)
- **Output Consistency**: Reproducibility across multiple inference runs (variance analysis)
- **Hallucination Rate**: % of demographic claims successfully filtered (target: >95%)
- **API Reliability**: Successful fetch rate for user profiles (target: >98%)

### Proposed Metrics (High Priority)

**1. Evidence Alignment Score**
- Manual annotation of 20-30 test personas
- Cohen's kappa for trait-to-behavior alignment
- Target: κ > 0.65 (substantial agreement)

**2. Archetype Validity**
- Cluster test users by known community (r/programming, r/fitness, etc.)
- Precision/recall on archetype classification
- Target: >80% precision on known communities

**3. Inference Confidence Calibration**
- Separate claims marked "observed" vs. "inferred"
- Calculate calibration curve: confidence vs. actual correctness
- Target: Calibration slope ≈ 1.0

**4. Persona Reproducibility**
- Generate same persona with different prompt framings
- Calculate Jaccard similarity of traits
- Target: >0.75 Jaccard overlap

### Validation Phases

**Phase 1 (Current):** Automatic quality gates
- Citation validation via regex URL matching
- Hallucination filter post-processing
- Schema enforcement

**Phase 2 (Recommended):** Ground truth comparison
- Manually annotate test set with personas
- Measure trait agreement vs. generated output

**Phase 3 (Future):** User studies
- Self-recognition accuracy testing
- User feedback collection

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

## 🔧 Design Decisions

### Why PRAW over Direct Reddit API?
- Built-in rate limiting and request throttling
- OAuth handling abstraction
- Object normalization and error recovery

### Why Groq + LLaMA 3.1 8B?
- Open-source model = transparency and reproducibility
- Smaller model = fewer hallucinations, more deterministic outputs
- Lower latency and cost vs. larger alternatives
- Better constraint adherence for our use case

### Why Multi-Stage Filtering?
- Prompts alone cannot guarantee hallucination prevention
- Layered approach catches different fabrication types
- Post-processing provides a safety net for inference failures

---

## 📁 Project Structure

```
reddit-user-persona-generator/
│
├── fetch_data.py              # Reddit API data extraction
├── generate_persona.py         # LLM inference & prompt orchestration
├── main.py                     # CLI entry point
├── requirements.txt            # Python dependencies
├── .env.sample                 # Environment variable template
├── .gitignore                  # Git ignore patterns
│
└── outputs/
    ├── user_data_<username>.json
    └── persona_output_<username>.txt
```

---

## 🛡️ Limitations & Ethical Considerations

### Known Limitations

- Personas are probabilistic estimates, not factual identities
- Reddit activity may not represent real-life behavior
- LLM outputs may still contain inaccuracies despite mitigation
- Personality inference is inherently subjective
- Sparse user histories reduce reliability

### Intended Use Cases

✅ Educational and research purposes
✅ UX audience analysis and exploration
✅ Behavioral pattern analysis
✅ AI prompt-engineering research
✅ Digital ethnography experiments

### Not Intended For

❌ Hiring decisions
❌ Surveillance or unauthorized profiling
❌ High-stakes individual evaluation
❌ Financial or legal decisions

---

## 🛠️ Error Handling

The system gracefully handles:
- Deleted and suspended Reddit accounts
- Empty or minimal user activity histories
- Rate limiting and API failures
- Missing environment variables
- Malformed response data

---

## 🔒 Security

- API keys stored locally via `.env` (never committed)
- No user authentication data stored
- Only publicly available Reddit activity analyzed
- All Reddit URLs verified against source data

**⚠️ Never commit `.env` to version control**

---

## 📚 Dependencies

Core libraries:
- `praw` - Reddit API wrapper
- `requests` - HTTP client
- `python-dotenv` - Environment variable management

Install with:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Potential areas:

- Evaluation framework improvements (ground truth testing)
- Prompt optimization and constraint refinement
- Analytics dashboard and visualization
- Model benchmarking and comparison
- Ethical safeguard enhancements
- Performance profiling and optimization

---

## 📈 Future Roadmap

### High Priority
- [ ] Ground truth persona validation suite
- [ ] Confidence calibration analysis
- [ ] User study validation framework
- [ ] Metrics dashboard for real-time monitoring

### Medium Priority
- [ ] Subreddit clustering and community classification
- [ ] Sentiment trend analysis and behavior drift detection
- [ ] Embedding-based behavioral grouping
- [ ] Temporal behavior evolution analysis

### Lower Priority
- [ ] Streamlit web interface
- [ ] PDF/HTML dashboard export
- [ ] Vector memory for extended histories
- [ ] Multi-persona generation modes

---

## 📄 License

MIT License - see LICENSE file for details

---

## 🔬 Related Work & References

This project combines concepts from:
- **NLP/ML**: Behavioral inference, prompt engineering, hallucination mitigation
- **UX Research**: Digital ethnography, persona development
- **Data Engineering**: Pipeline design, output validation, evidence binding
- **AI Safety**: Constraint-based inference, uncertainty quantification

---

## ⭐ Acknowledgments

Built as an exploration of:
- Reliable behavioral inference at scale
- Structured prompt engineering patterns
- Evidence-backed AI generation
- Balancing insight with uncertainty

The interesting problem is not "using an LLM," but designing a system that balances insight, uncertainty, transparency, and evidence within AI-generated human profiling.
