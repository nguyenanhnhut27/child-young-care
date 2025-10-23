import os
from typing import Optional, Dict, List
import anthropic
from openai import OpenAI
import requests

class MentalHealthAgent:
    """
    Multi-model AI agent for child and adolescent mental health case analysis.
    Integrates OpenAI, Claude (Anthropic), and Grok (xAI) models.
    """
    
    def __init__(
        self,
        openai_key: Optional[str] = None,
        claude_key: Optional[str] = None,
        grok_key: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000
    ):
        self.temperature = temperature
        self.max_tokens = max_tokens
        
        # Initialize available models
        self.available_models = []
        
        # OpenAI
        if openai_key:
            self.openai_client = OpenAI(api_key=openai_key)
            self.available_models.append("openai")
        else:
            self.openai_client = None
        
        # Claude (Anthropic)
        if claude_key:
            self.claude_client = anthropic.Anthropic(api_key=claude_key)
            self.available_models.append("claude")
        else:
            self.claude_client = None
        
        # Grok (xAI)
        if grok_key:
            self.grok_key = grok_key
            self.available_models.append("grok")
        else:
            self.grok_key = None
        
        if not self.available_models:
            raise ValueError("At least one AI model API key must be provided")
        
        # System prompt for mental health context
        self.system_prompt = """You are an expert AI assistant specializing in child and adolescent mental health disorders. Your role is to help students and clinicians analyze cases, understand diagnostic criteria, and explore evidence-based treatment approaches.

Key responsibilities:
1. Provide accurate information based on DSM-5-TR criteria
2. Analyze case studies systematically
3. Suggest differential diagnoses when appropriate
4. Recommend evidence-based assessment tools
5. Outline treatment considerations following best practices
6. Consider developmental factors specific to children and adolescents
7. Emphasize the importance of comprehensive assessment

Important guidelines:
- Always acknowledge the complexity of mental health diagnosis
- Recommend professional clinical judgment for real cases
- Consider cultural and contextual factors
- Emphasize the importance of family involvement
- Note when more information would be needed for proper assessment
- Reference evidence-based practices and research when relevant

Remember: This is for educational purposes. Real clinical decisions require comprehensive assessment by licensed professionals."""
    
    def query(self, user_query: str, model_preference: Optional[str] = None) -> str:
        """
        Query the AI agent with a question or case study.
        
        Args:
            user_query: The question or case to analyze
            model_preference: Preferred model to use (openai, claude, grok)
        
        Returns:
            AI-generated response
        """
        # Determine which model to use
        if model_preference and model_preference in self.available_models:
            model = model_preference
        else:
            model = self.available_models[0]  # Use first available model
        
        # Route to appropriate model
        if model == "openai":
            return self._query_openai(user_query)
        elif model == "claude":
            return self._query_claude(user_query)
        elif model == "grok":
            return self._query_grok(user_query)
        else:
            return "Error: No available models"
    
    def query_all_models(self, user_query: str) -> Dict[str, str]:
        """
        Query all available models and return their responses.
        
        Args:
            user_query: The question or case to analyze
        
        Returns:
            Dictionary with model names as keys and responses as values
        """
        responses = {}
        
        for model in self.available_models:
            try:
                if model == "openai":
                    responses["OpenAI GPT"] = self._query_openai(user_query)
                elif model == "claude":
                    responses["Claude"] = self._query_claude(user_query)
                elif model == "grok":
                    responses["Grok"] = self._query_grok(user_query)
            except Exception as e:
                responses[model] = f"Error: {str(e)}"
        
        # Format combined response
        combined = "## 🤖 Multi-Model Analysis\n\n"
        for model_name, response in responses.items():
            combined += f"### {model_name}\n\n{response}\n\n---\n\n"
        
        return combined
    
    def _query_openai(self, user_query: str) -> str:
        """Query OpenAI GPT model"""
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_query}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"OpenAI Error: {str(e)}"
    
    def _query_claude(self, user_query: str) -> str:
        """Query Claude (Anthropic) model"""
        try:
            message = self.claude_client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=self.system_prompt,
                messages=[
                    {"role": "user", "content": user_query}
                ]
            )
            return message.content[0].text
        except Exception as e:
            return f"Claude Error: {str(e)}"
    
    def _query_grok(self, user_query: str) -> str:
        """Query Grok (xAI) model"""
        try:
            # Grok API endpoint (update if needed)
            url = "https://api.x.ai/v1/chat/completions"
            
            headers = {
                "Authorization": f"Bearer {self.grok_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "grok-beta",
                "messages": [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_query}
                ],
                "temperature": self.temperature,
                "max_tokens": self.max_tokens
            }
            
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            
            result = response.json()
            return result['choices'][0]['message']['content']
        except Exception as e:
            return f"Grok Error: {str(e)}"
    
    def analyze_case_study(self, case_details: Dict) -> str:
        """
        Analyze a structured case study.
        
        Args:
            case_details: Dictionary containing case information
        
        Returns:
            Comprehensive case analysis
        """
        # Build structured prompt from case details
        prompt = "Please analyze the following case study:\n\n"
        
        for key, value in case_details.items():
            prompt += f"{key}: {value}\n"
        
        prompt += "\nProvide a comprehensive analysis including:\n"
        prompt += "1. Presenting symptoms and concerns\n"
        prompt += "2. Possible diagnoses (with DSM-5 criteria consideration)\n"
        prompt += "3. Differential diagnoses\n"
        prompt += "4. Recommended assessment tools\n"
        prompt += "5. Treatment considerations\n"
        prompt += "6. Important factors to consider\n"
        
        return self.query(prompt)
    
    def get_dsm5_criteria(self, disorder: str) -> str:
        """Get DSM-5 criteria for a specific disorder"""
        prompt = f"Provide the DSM-5-TR diagnostic criteria for {disorder} in children and adolescents. Include all required criteria and specifiers."
        return self.query(prompt)
    
    def suggest_assessment_tools(self, concern: str, age: int) -> str:
        """Suggest appropriate assessment tools"""
        prompt = f"What are the most appropriate evidence-based assessment tools for evaluating {concern} in a {age}-year-old? Please include both screening tools and comprehensive assessments."
        return self.query(prompt)
    
    def get_treatment_options(self, disorder: str, age: int) -> str:
        """Get evidence-based treatment options"""
        prompt = f"What are the evidence-based treatment options for {disorder} in a {age}-year-old child/adolescent? Include both psychosocial interventions and medication considerations when appropriate."
        return self.query(prompt)