import streamlit as st
import os
from datetime import datetime
import json

# Import the AI agent modules
from agent_core import MentalHealthAgent
from document_processor import DocumentProcessor

# Page configuration
st.set_page_config(
    page_title="Child & Adolescent Mental Health AI Agent",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .case-study-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .response-box {
        background-color: #e8f4f8;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'uploaded_docs' not in st.session_state:
    st.session_state.uploaded_docs = []
if 'agent' not in st.session_state:
    st.session_state.agent = None

# Sidebar
with st.sidebar:
    st.image("IMG_9046.jpg", width=100)
    st.title("QUE ANH HUYNH")
    
    st.subheader("👤 User Information")
    user_name = st.text_input("Your Name", value="Que Anh Huynh")
    
    st.subheader("🤖 AI Model Selection")
    use_openai = st.checkbox("OpenAI GPT", value=True)
    use_claude = st.checkbox("Claude (Anthropic)", value=True)
    use_grok = st.checkbox("Grok (xAI)", value=False)
    
    st.subheader("🔑 API Keys")
    openai_key = st.text_input("OpenAI API Key", type="password", 
                                value=os.getenv("OPENAI_API_KEY", ""))
    claude_key = st.text_input("Claude API Key", type="password",
                               value=os.getenv("ANTHROPIC_API_KEY", ""))
    grok_key = st.text_input("Grok API Key", type="password",
                             value=os.getenv("XAI_API_KEY", ""))
    
    st.subheader("⚙️ Agent Settings")
    temperature = st.slider("Response Creativity", 0.0, 1.0, 0.7)
    max_tokens = st.slider("Max Response Length", 500, 4000, 2000)
    
    # Initialize agent button
    if st.button("Initialize AI Agent", type="primary"):
        with st.spinner("Initializing AI Agent..."):
            try:
                st.session_state.agent = MentalHealthAgent(
                    openai_key=openai_key if use_openai else None,
                    claude_key=claude_key if use_claude else None,
                    grok_key=grok_key if use_grok else None,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                st.success("✅ AI Agent initialized successfully!")
            except Exception as e:
                st.error(f"❌ Error initializing agent: {str(e)}")
    
    st.divider()
    
    # Clear chat button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

# Main content area
st.markdown("<h1 class='main-header'>🧠 Child & Adolescent Mental Health AI Agent</h1>", 
            unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "💬 Chat & Case Analysis", 
    "📚 Document Upload", 
    "📊 Knowledge Base",
    "📝 Study Notes"
])

# Tab 1: Chat & Case Analysis
with tab1:
    st.header("Analyze Cases & Ask Questions")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Input Case or Question")
        
        # Query type selection
        query_type = st.selectbox(
            "Select Query Type",
            ["General Question", "Case Study Analysis", "Differential Diagnosis", 
             "Treatment Planning", "Assessment Tools", "DSM-5 Criteria"]
        )
        
        # Text input area
        user_input = st.text_area(
            "Enter your case study or question:",
            height=200,
            placeholder="Example: A 14-year-old presents with persistent sadness, loss of interest in activities, and difficulty sleeping for the past 3 months..."
        )
        
        # Additional context
        with st.expander("Add Additional Context (Optional)"):
            age = st.number_input("Patient Age", min_value=0, max_value=18, value=10)
            gender = st.selectbox("Gender", ["Not specified", "Male", "Female", "Other"])
            context = st.text_area("Additional Context", 
                                   placeholder="Family history, previous diagnoses, medications, etc.")
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            analyze_button = st.button("🔍 Analyze with AI", type="primary", use_container_width=True)
        with col_btn2:
            multi_model = st.checkbox("Compare Multiple Models", value=False)
    
    with col2:
        st.subheader("Quick Actions")
        st.markdown("""
        **Sample Questions:**
        - What are the DSM-5 criteria for ADHD?
        - Differential diagnosis for anxiety in teens
        - Assessment tools for depression in children
        - Treatment options for ODD
        """)
        
        if st.button("Load Sample Case"):
            sample_case = """A 12-year-old boy is brought to the clinic by his parents due to concerns about his behavior at school and home. Over the past 6 months, he has shown:
            
- Difficulty paying attention in class
- Frequently losing homework and school supplies
- Interrupting others during conversations
- Difficulty waiting his turn
- Running around excessively during inappropriate times
- Academic performance decline

The symptoms have been present for at least 6 months and occur in both school and home settings."""
            st.session_state.sample_case = sample_case
            st.rerun()
    
    # Process the query
    if analyze_button and user_input:
        if st.session_state.agent is None:
            st.error("⚠️ Please initialize the AI Agent in the sidebar first!")
        else:
            with st.spinner("🤖 AI is analyzing your case..."):
                try:
                    # Build the full query with context
                    full_query = f"""
Query Type: {query_type}

Case/Question:
{user_input}

Patient Information:
- Age: {age} years
- Gender: {gender}
- Additional Context: {context if context else 'None provided'}

Please provide a comprehensive analysis following evidence-based practices for child and adolescent mental health.
"""
                    
                    # Get response from agent
                    if multi_model:
                        response = st.session_state.agent.query_all_models(full_query)
                    else:
                        response = st.session_state.agent.query(full_query)
                    
                    # Add to chat history
                    st.session_state.chat_history.append({
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "query": user_input,
                        "query_type": query_type,
                        "response": response
                    })
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    # Display chat history
    st.divider()
    st.subheader("💬 Conversation History")
    
    for idx, chat in enumerate(reversed(st.session_state.chat_history)):
        with st.container():
            st.markdown(f"**🕒 {chat['timestamp']}** | Type: `{chat['query_type']}`")
            
            with st.expander(f"Query {len(st.session_state.chat_history) - idx}", expanded=(idx == 0)):
                st.markdown("<div class='case-study-box'>", unsafe_allow_html=True)
                st.markdown(f"**Your Question/Case:**\n\n{chat['query']}")
                st.markdown("</div>", unsafe_allow_html=True)
                
                st.markdown("<div class='response-box'>", unsafe_allow_html=True)
                st.markdown(f"**AI Response:**\n\n{chat['response']}")
                st.markdown("</div>", unsafe_allow_html=True)

# Tab 2: Document Upload
with tab2:
    st.header("📚 Upload Study Materials")
    
    st.markdown("""
    Upload your documents, case studies, lecture notes, and reference materials. 
    The AI agent will use these to provide more accurate and contextual responses.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        uploaded_files = st.file_uploader(
            "Upload Documents (PDF, DOCX, TXT)",
            type=['pdf', 'docx', 'txt', 'md'],
            accept_multiple_files=True
        )
        
        if uploaded_files:
            if st.button("Process Documents", type="primary"):
                with st.spinner("Processing documents..."):
                    try:
                        processor = DocumentProcessor()
                        for file in uploaded_files:
                            result = processor.process_file(file)
                            st.session_state.uploaded_docs.append({
                                "filename": file.name,
                                "processed": True,
                                "chunks": result.get("chunks", 0),
                                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            })
                        st.success(f"✅ Successfully processed {len(uploaded_files)} documents!")
                    except Exception as e:
                        st.error(f"Error processing documents: {str(e)}")
    
    with col2:
        st.subheader("Uploaded Documents")
        if st.session_state.uploaded_docs:
            for doc in st.session_state.uploaded_docs:
                with st.container():
                    st.markdown(f"""
                    📄 **{doc['filename']}**
                    - Processed: {doc['processed']}
                    - Chunks: {doc.get('chunks', 'N/A')}
                    - Uploaded: {doc['timestamp']}
                    """)
        else:
            st.info("No documents uploaded yet")

# Tab 3: Knowledge Base
with tab3:
    st.header("📊 Mental Health Knowledge Base")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Common Disorders")
        disorders = [
            "ADHD (Attention-Deficit/Hyperactivity Disorder)",
            "Autism Spectrum Disorder (ASD)",
            "Major Depressive Disorder",
            "Generalized Anxiety Disorder",
            "Social Anxiety Disorder",
            "Oppositional Defiant Disorder (ODD)",
            "Conduct Disorder",
            "Separation Anxiety Disorder",
            "Obsessive-Compulsive Disorder (OCD)",
            "Post-Traumatic Stress Disorder (PTSD)"
        ]
        
        selected_disorder = st.selectbox("Select a disorder to learn more:", disorders)
        
        if st.button("Get Information"):
            if st.session_state.agent:
                with st.spinner("Retrieving information..."):
                    query = f"Provide comprehensive information about {selected_disorder} in children and adolescents, including DSM-5 criteria, prevalence, assessment tools, and evidence-based treatments."
                    response = st.session_state.agent.query(query)
                    st.markdown(response)
            else:
                st.warning("Please initialize the AI Agent first")
    
    with col2:
        st.subheader("Assessment Tools")
        st.markdown("""
        **Common Assessment Instruments:**
        - CBCL (Child Behavior Checklist)
        - Conners Rating Scales
        - Beck Youth Inventories
        - SCARED (Screen for Child Anxiety Related Disorders)
        - CDI (Children's Depression Inventory)
        - BASC-3 (Behavior Assessment System for Children)
        - Vanderbilt ADHD Rating Scales
        - ADOS-2 (Autism Diagnostic Observation Schedule)
        """)

# Tab 4: Study Notes
with tab4:
    st.header("📝 Study Notes & Summaries")
    
    st.markdown("Generate study notes and summaries from your materials")
    
    note_topic = st.text_input("Topic for study notes:")
    note_type = st.selectbox(
        "Note Type",
        ["Summary", "Key Points", "Case Examples", "Treatment Guidelines", "DSM-5 Criteria"]
    )
    
    if st.button("Generate Study Notes"):
        if st.session_state.agent and note_topic:
            with st.spinner("Generating study notes..."):
                query = f"Create detailed {note_type.lower()} about {note_topic} for child and adolescent mental health, suitable for clinical study."
                response = st.session_state.agent.query(query)
                
                st.markdown("### Generated Notes")
                st.markdown(response)
                
                # Download button
                st.download_button(
                    label="Download Notes",
                    data=response,
                    file_name=f"{note_topic.replace(' ', '_')}_notes.txt",
                    mime="text/plain"
                )
        else:
            st.warning("Please enter a topic and initialize the AI Agent")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>Child & Adolescent Mental Health AI Agent | Created for Que Anh Huynh</p>
    <p style='font-size: 0.8rem;'>⚠️ This tool is for educational purposes only and should not replace professional clinical judgment</p>
</div>
""", unsafe_allow_html=True)