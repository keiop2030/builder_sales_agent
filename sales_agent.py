"""
Builder Sales Agent - AI-powered sales assistant for builder software
"""
import os
import sys
from typing import List, Dict, Optional
from openai import OpenAI
from colorama import init, Fore, Style
import config

# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)


class BuilderSalesAgent:
    """AI Sales Agent for commercial and residential builder software"""
    
    def __init__(self):
        """Initialize the sales agent"""
        if not config.OPENAI_API_KEY:
            print(f"{Fore.RED}Error: OPENAI_API_KEY not found. Please set it in your .env file.{Style.RESET_ALL}")
            print(f"Copy .env.example to .env and add your OpenAI API key.")
            print(f"\n{Fore.YELLOW}Tip: To test without an API key, use demo_agent.py instead!{Style.RESET_ALL}")
            sys.exit(1)
            
        self.client = OpenAI(api_key=config.OPENAI_API_KEY)
        self.conversation_history: List[Dict[str, str]] = []
        self.lead_info: Dict[str, str] = {}
        self.builder_type: Optional[str] = None  # 'commercial' or 'residential'
        
    def get_system_prompt(self) -> str:
        """Generate the system prompt for the AI agent"""
        return f"""You are {config.AGENT_NAME}, an expert sales representative for {config.COMPANY_NAME}. 
You are helping commercial and residential builders discover how {config.PRODUCT_NAME} - {config.PRODUCT_TAGLINE} can transform their business.

Your personality:
- Professional yet friendly and approachable
- Consultative - you ask questions to understand their needs
- Knowledgeable about the construction industry
- Focused on solving their problems, not just selling features
- Enthusiastic but never pushy

Your goals:
1. Understand if they are a commercial or residential builder
2. Identify their biggest pain points and challenges
3. Show how {config.PRODUCT_NAME} specifically addresses their needs
4. Qualify the lead (company size, current tools, timeline)
5. Schedule a demo if they're interested

Product Information:

COMMERCIAL BUILDER FEATURES:
{chr(10).join('- ' + feature for feature in config.COMMERCIAL_FEATURES)}

RESIDENTIAL BUILDER FEATURES:
{chr(10).join('- ' + feature for feature in config.RESIDENTIAL_FEATURES)}

PRICING:
- Starter: ${config.PRICING['starter']['price_monthly']}/month - {config.PRICING['starter']['description']}
- Professional: ${config.PRICING['professional']['price_monthly']}/month - {config.PRICING['professional']['description']}
- Enterprise: Custom pricing - {config.PRICING['enterprise']['description']}

Demo booking: {config.DEMO_BOOKING_URL}

Common pain points to listen for:
COMMERCIAL: {', '.join(config.PAIN_POINTS['commercial'])}
RESIDENTIAL: {', '.join(config.PAIN_POINTS['residential'])}

Guidelines:
- Start with a warm greeting and ask what type of building projects they do
- Ask open-ended questions to understand their current workflow
- Listen for pain points and connect them to specific features
- Don't overwhelm them with all features - focus on what matters to them
- When they show interest, suggest a personalized demo
- Be concise - keep responses to 2-3 paragraphs unless they ask for details
- Use their name if they provide it
- If they seem hesitant, ask what concerns they have
"""

    def start_conversation(self):
        """Begin the sales conversation"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{config.COMPANY_NAME} - {config.PRODUCT_NAME}")
        print(f"{'='*70}{Style.RESET_ALL}\n")
        
        # Initial greeting from the agent
        initial_message = self._get_ai_response(
            "Greet the prospect warmly and introduce yourself. Ask what type of builder they are (commercial/residential) and what brought them here today."
        )
        
        print(f"{Fore.GREEN}{config.AGENT_NAME}: {Style.RESET_ALL}{initial_message}\n")
        
        # Main conversation loop
        self.run_conversation_loop()
    
    def run_conversation_loop(self):
        """Run the main conversation loop"""
        turn_count = 0
        
        while turn_count < config.MAX_CONVERSATION_TURNS:
            try:
                # Get user input
                user_input = input(f"{Fore.YELLOW}You: {Style.RESET_ALL}").strip()
                
                if not user_input:
                    continue
                
                # Check for exit commands
                if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                    farewell = self._get_ai_response(
                        f"The prospect said: '{user_input}'. Give a professional, warm farewell. Thank them for their time and let them know they can reach out anytime."
                    )
                    print(f"\n{Fore.GREEN}{config.AGENT_NAME}: {Style.RESET_ALL}{farewell}\n")
                    break
                
                # Add user message to history
                self.conversation_history.append({
                    "role": "user",
                    "content": user_input
                })
                
                # Get AI response
                response = self._get_ai_response(user_input)
                
                # Display response
                print(f"\n{Fore.GREEN}{config.AGENT_NAME}: {Style.RESET_ALL}{response}\n")
                
                turn_count += 1
                
            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}Conversation ended.{Style.RESET_ALL}")
                break
            except Exception as e:
                print(f"\n{Fore.RED}Error: {str(e)}{Style.RESET_ALL}\n")
                continue
    
    def _get_ai_response(self, user_message: str) -> str:
        """Get response from OpenAI API"""
        try:
            # Prepare messages for API call
            messages = [
                {"role": "system", "content": self.get_system_prompt()}
            ]
            
            # Add conversation history
            messages.extend(self.conversation_history)
            
            # Add current user message if not already in history
            if not self.conversation_history or self.conversation_history[-1]["content"] != user_message:
                messages.append({"role": "user", "content": user_message})
            
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=config.OPENAI_MODEL,
                messages=messages,
                temperature=config.CONVERSATION_TEMPERATURE,
                max_tokens=500
            )
            
            assistant_message = response.choices[0].message.content
            
            # Add to conversation history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            return f"I apologize, but I encountered an error. Could you please rephrase that? (Error: {str(e)})"
    
    def extract_lead_info(self) -> Dict[str, str]:
        """Extract lead information from the conversation"""
        # This could be enhanced with more sophisticated NLP
        # For now, returns the conversation history
        return {
            "conversation_length": str(len(self.conversation_history)),
            "builder_type": self.builder_type or "unknown"
        }


def main():
    """Main entry point for the sales agent"""
    print(f"{Fore.CYAN}Initializing Builder Sales Agent...{Style.RESET_ALL}")
    
    agent = BuilderSalesAgent()
    agent.start_conversation()
    
    print(f"\n{Fore.CYAN}Thank you for using {config.COMPANY_NAME}'s Sales Agent!{Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()
