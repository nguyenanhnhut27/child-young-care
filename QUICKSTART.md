# 🚀 Quick Start Guide

## Welcome, Que Anh Huynh!

This guide will help you get started with your Child & Adolescent Mental Health AI Agent in just 5 minutes.

---

## Step 1: Installation (2 minutes)

### Install Python Dependencies
Open your terminal/command prompt and run:

```bash
cd mental_health_agent
pip install -r requirements.txt
```

**What's being installed?**
- Streamlit: Web app framework
- OpenAI: For GPT models
- Anthropic: For Claude
- PyPDF2: PDF processing
- python-docx: Word document processing

---

## Step 2: Get Your API Keys (5-10 minutes)

You need at least ONE API key to use the app.

### Option A: OpenAI (Recommended for beginners)
1. Go to https://platform.openai.com/signup
2. Create an account or sign in
3. Navigate to "API Keys" in your dashboard
4. Click "Create new secret key"
5. Copy the key (starts with `sk-`)
6. **Important**: Add $5-10 credit to your account

### Option B: Anthropic (Claude)
1. Go to https://console.anthropic.com/
2. Sign up for an account
3. Go to "API Keys"
4. Generate a new key
5. Copy and save it

### Option C: xAI (Grok) - Optional
1. Visit https://x.ai/
2. Request API access
3. Generate API key

---

## Step 3: Configure API Keys (1 minute)

### Method 1: Using .env file (Recommended)
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your keys:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   ANTHROPIC_API_KEY=sk-ant-your-key-here
   XAI_API_KEY=your-key-here
   ```

### Method 2: Enter directly in the app
- You can also paste API keys directly in the sidebar when you run the app

---

## Step 4: Launch the App (30 seconds)

Run this command:

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

If it doesn't open automatically, just copy that URL into your browser.

---

## Step 5: First Use (2 minutes)

### Initialize the Agent
1. Look at the left sidebar
2. Enter your API key(s) if you didn't use the .env file
3. Check the boxes for which AI models to use
4. Click **"Initialize AI Agent"** button
5. Wait for the success message ✅

### Try Your First Query
1. Go to the "Chat & Case Analysis" tab
2. Click **"Load Sample Case"** button
3. Click **"🔍 Analyze with AI"**
4. Watch the AI analyze the case!

---

## 🎯 What to Try Next

### 1. Analyze Different Cases
Try asking:
- "What are the DSM-5 criteria for ADHD in children?"
- "Recommend assessment tools for a 10-year-old with anxiety"
- "Explain the difference between ODD and Conduct Disorder"

### 2. Upload Your Study Materials
1. Go to "Document Upload" tab
2. Upload your PDFs, Word docs, or text files
3. Click "Process Documents"
4. Now the AI will reference YOUR materials in responses!

### 3. Generate Study Notes
1. Go to "Study Notes" tab
2. Enter a topic: "Autism Spectrum Disorder in adolescents"
3. Select note type: "Summary"
4. Click "Generate Study Notes"
5. Download for offline studying

### 4. Compare Multiple AI Models
1. In the case analysis tab
2. Check the box "Compare Multiple Models"
3. Get perspectives from different AI systems!

---

## 💡 Pro Tips

### For Better Responses
- Be specific with your questions
- Include patient age when relevant
- Mention what aspect you want to focus on (diagnosis, treatment, assessment)
- Use the "Additional Context" section for complex cases

### For Studying
- Upload your lecture notes and textbooks
- Generate study notes on different topics
- Practice with the sample cases provided
- Use the Knowledge Base tab for quick reference

### Save Your Work
- The chat history saves during your session
- Download important responses
- Export study notes for later review

---

## 🔧 Troubleshooting

### "Error initializing agent"
- Check your API key is correct
- Make sure you have credits in your OpenAI account
- Try copying the key again (no extra spaces)

### "Module not found" errors
- Run `pip install -r requirements.txt` again
- Make sure you're in the correct directory

### App won't open
- Check if port 8501 is already in use
- Try: `streamlit run app.py --server.port 8502`

### Slow responses
- This is normal! AI models take 10-30 seconds
- Reduce "Max Response Length" in settings
- Use only one model instead of comparing multiple

---

## 📚 Sample Questions to Ask

Copy and paste these into the chat to practice:

```
What are the key differences between normal childhood worry and Generalized Anxiety Disorder?
```

```
A 13-year-old shows declining grades, social withdrawal, and irritability for 2 months. What should be considered in the differential diagnosis?
```

```
What are evidence-based treatments for ADHD in a 7-year-old?
```

```
Explain the CBCL (Child Behavior Checklist) and when it's most useful.
```

---

## 🎓 Learning Path Suggestion

### Week 1: Basics
- [ ] Get comfortable with the interface
- [ ] Try all the sample cases
- [ ] Practice asking diagnostic questions
- [ ] Upload one study document

### Week 2: Deep Dive
- [ ] Upload all your course materials
- [ ] Generate study notes for each topic
- [ ] Practice differential diagnosis
- [ ] Try multi-model comparison

### Week 3: Integration
- [ ] Create your own case studies
- [ ] Test yourself with questions
- [ ] Review assessment tools
- [ ] Explore treatment planning

---

## ⚠️ Remember

**This is for EDUCATION only:**
- Don't enter real patient information
- Always verify information with official sources
- Use for study and learning, not clinical decision-making
- Consult with supervisors for real cases

---

## 🆘 Need Help?

1. Check the main README.md file
2. Review the error message carefully
3. Make sure all dependencies are installed
4. Verify your API keys are active

---

## 🎉 You're Ready!

You now have a powerful AI assistant for your mental health studies. 

**Next steps:**
1. Run `streamlit run app.py`
2. Initialize the agent
3. Start learning!

Good luck with your studies! 🧠📚

---

*Created for Que Anh Huynh's Child & Adolescent Mental Health Studies*