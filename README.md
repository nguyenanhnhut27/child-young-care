# 🧠 Child & Adolescent Mental Health AI Agent

An intelligent web application powered by multiple AI models (OpenAI, Claude, Grok) designed to help students and clinicians study and analyze child and adolescent mental health disorders.

Created for **Que Anh Huynh** - Mental Health Studies

---

## ✨ Features

### 🤖 Multi-Model AI Integration
- **OpenAI GPT-4**: Advanced language understanding and generation
- **Claude (Anthropic)**: Expert reasoning and analysis
- **Grok (xAI)**: Additional perspective and insights
- Compare responses from multiple models simultaneously

### 📚 Core Capabilities
1. **Case Study Analysis**: Submit clinical cases and receive comprehensive analyses
2. **Diagnostic Support**: Get DSM-5 criteria and differential diagnoses
3. **Treatment Planning**: Evidence-based treatment recommendations
4. **Assessment Tools**: Guidance on appropriate evaluation instruments
5. **Document Upload**: Upload your study materials, lecture notes, and references
6. **Knowledge Base**: Quick access to common disorder information
7. **Study Notes**: Generate custom study materials and summaries

### 💡 Key Benefits
- Multiple AI models for diverse perspectives
- Evidence-based responses following DSM-5-TR
- Developmental considerations for children and adolescents
- Document processing for personalized learning
- Interactive chat interface with history
- Export and save responses

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- API keys for at least one of: OpenAI, Anthropic (Claude), or xAI (Grok)

### Installation

1. **Clone or download this repository**
```bash
cd mental_health_agent
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Set up API keys**

Create a `.env` file in the project root (copy from `.env.example`):
```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```
OPENAI_API_KEY=sk-your-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-claude-key-here
XAI_API_KEY=your-grok-key-here
```

4. **Run the application**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📖 How to Use

### 1. Initial Setup
1. Open the sidebar (click the arrow in the top-left)
2. Enter your API keys for the models you want to use
3. Select which AI models to enable
4. Click "Initialize AI Agent"

### 2. Analyzing Cases
1. Go to the "Chat & Case Analysis" tab
2. Select the query type (e.g., "Case Study Analysis")
3. Enter your case details or question
4. Optionally add patient age, gender, and context
5. Click "Analyze with AI"
6. View the comprehensive response

### 3. Uploading Documents
1. Go to the "Document Upload" tab
2. Upload your PDF, DOCX, or TXT files
3. Click "Process Documents"
4. The AI will use these documents to provide contextualized responses

### 4. Knowledge Base
1. Navigate to the "Knowledge Base" tab
2. Select a disorder from the dropdown
3. Get instant information about diagnostic criteria, assessment tools, and treatments

### 5. Generating Study Notes
1. Go to the "Study Notes" tab
2. Enter a topic (e.g., "ADHD in adolescents")
3. Select note type (Summary, Key Points, etc.)
4. Click "Generate Study Notes"
5. Download the notes for offline study

---

## 🔑 Getting API Keys

### OpenAI (GPT)
1. Visit https://platform.openai.com/
2. Sign up or log in
3. Go to API Keys section
4. Create a new API key
5. **Important**: Add credits to your account

### Anthropic (Claude)
1. Visit https://console.anthropic.com/
2. Sign up or log in
3. Navigate to API Keys
4. Generate a new API key
5. Copy and save securely

### xAI (Grok)
1. Visit https://x.ai/
2. Sign up for API access
3. Generate your API key
4. Note: Grok API may have limited availability

---

## 📂 Project Structure

```
mental_health_agent/
├── app.py                    # Main Streamlit application
├── agent_core.py             # AI agent logic and model integration
├── document_processor.py     # Document upload and processing
├── requirements.txt          # Python dependencies
├── .env.example             # Example environment variables
└── README.md                # This file
```

---

## 🎯 Use Cases

### For Students
- **Study Case Examples**: Analyze practice cases and understand diagnostic reasoning
- **Exam Preparation**: Generate study notes and review key concepts
- **DSM-5 Reference**: Quick access to diagnostic criteria
- **Assessment Tools**: Learn about appropriate evaluation instruments

### For Clinicians
- **Case Consultation**: Get second opinions on complex cases
- **Treatment Planning**: Review evidence-based interventions
- **Documentation Support**: Generate comprehensive case formulations
- **Research**: Explore latest evidence and best practices

---

## ⚙️ Advanced Features

### Multi-Model Comparison
Enable "Compare Multiple Models" to see responses from all active AI models side-by-side. This helps you:
- Identify consensus opinions
- Spot different perspectives
- Cross-validate information
- Learn from diverse approaches

### Document-Based RAG (Retrieval-Augmented Generation)
When you upload documents:
- The system chunks your documents intelligently
- Relevant passages are retrieved for each query
- AI responses incorporate your specific materials
- More personalized and context-aware answers

### Customizable Settings
Adjust in the sidebar:
- **Temperature**: Control creativity (0 = focused, 1 = creative)
- **Max Tokens**: Control response length
- **Model Selection**: Choose which AI models to use

---

## 🛡️ Important Disclaimers

**⚠️ Educational Use Only**
- This tool is designed for educational and study purposes
- It should NOT replace professional clinical judgment
- Real patient care requires comprehensive assessment by licensed professionals
- Always consult with supervisors and follow institutional guidelines

**🔒 Privacy & Security**
- Do NOT enter real patient information or PHI (Protected Health Information)
- Use hypothetical cases only
- API keys are stored locally on your machine
- Follow HIPAA and ethical guidelines

**📚 Information Accuracy**
- AI responses are based on training data and may not reflect latest research
- Always verify information with authoritative sources
- DSM-5-TR should be consulted for official diagnostic criteria
- Evidence-based practice guidelines should be reviewed independently

---

## 🐛 Troubleshooting

### Common Issues

**Problem**: "Error initializing agent"
- **Solution**: Check that your API keys are correct and have sufficient credits

**Problem**: No response from AI
- **Solution**: Verify internet connection and API key validity

**Problem**: Documents not uploading
- **Solution**: Ensure files are in supported formats (PDF, DOCX, TXT, MD)

**Problem**: Slow responses
- **Solution**: Reduce max_tokens setting or try a different model

### Error Messages

If you see API errors:
1. Check your API key is correct
2. Verify you have available credits/quota
3. Check the API service status page
4. Try a different AI model

---

## 🔄 Updates and Improvements

Planned features:
- [ ] Vector database integration for better document search
- [ ] Export conversations to PDF
- [ ] Evidence citations and references
- [ ] Case library with examples
- [ ] Collaborative features for study groups
- [ ] Mobile-responsive design enhancements

---

## 📞 Support

For questions or issues:
1. Check the troubleshooting section above
2. Review API provider documentation
3. Ensure all dependencies are installed correctly

---

## 📄 License

This project is created for educational purposes. Please use responsibly and ethically.

---

## 🙏 Acknowledgments

- Built with Streamlit
- Powered by OpenAI, Anthropic, and xAI
- Designed for mental health education
- Created for Que Anh Huynh's studies in child and adolescent mental health

---

## 🚀 Getting Started Checklist

- [ ] Install Python 3.8+
- [ ] Install dependencies (`pip install -r requirements.txt`)
- [ ] Get at least one API key
- [ ] Create `.env` file with API keys
- [ ] Run `streamlit run app.py`
- [ ] Initialize AI agent in sidebar
- [ ] Try analyzing a sample case
- [ ] Upload study documents
- [ ] Generate study notes

**Ready to enhance your mental health studies!** 🎓

---

*Remember: This is a learning tool. Always prioritize ethical practice and professional supervision in clinical work.*