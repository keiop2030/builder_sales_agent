"""
Demo mode for Builder Sales Agent
Simulates conversations without requiring OpenAI API
"""
import sys
from colorama import init, Fore, Style
import config

# Initialize colorama
init(autoreset=True)


class DemoSalesAgent:
    """Demo version of the sales agent with pre-programmed responses"""
    
    def __init__(self):
        self.conversation_stage = "greeting"
        self.builder_type = None
        self.turn_count = 0
        
    def get_response(self, user_input: str) -> str:
        """Get a simulated response based on user input"""
        user_lower = user_input.lower()
        self.turn_count += 1
        
        # Exit handling
        if any(word in user_lower for word in ['exit', 'quit', 'bye', 'goodbye']):
            return f"Thank you so much for your time today! It was great learning about your business. Feel free to reach out anytime at {config.DEMO_BOOKING_URL} if you'd like to see a demo. Have a great day!"
        
        # Greeting stage
        if self.conversation_stage == "greeting":
            self.conversation_stage = "identify_type"
            return f"Hello! I'm {config.AGENT_NAME} from {config.COMPANY_NAME}. We help builders like you streamline their operations with our complete construction management platform. Are you working on commercial or residential projects, and what brought you here today?"
        
        # Identify builder type
        if self.conversation_stage == "identify_type":
            if "residential" in user_lower or "homes" in user_lower or "house" in user_lower:
                self.builder_type = "residential"
                self.conversation_stage = "discovery"
                return "That's wonderful! Residential building is such a rewarding business. What are some of the biggest challenges you're facing right now in managing your projects? Is it coordinating with trades, keeping clients updated, tracking selections, or something else?"
            elif "commercial" in user_lower or "office" in user_lower or "retail" in user_lower:
                self.builder_type = "commercial"
                self.conversation_stage = "discovery"
                return "Great! Commercial construction requires juggling so many moving parts. I'd love to understand what's driving your interest today. Are you looking to solve specific pain points with your current setup, or are you growing and need more robust tools?"
            else:
                return "I'd love to learn more about your business! Are you primarily focused on residential home building or commercial construction projects?"
        
        # Discovery stage - identify pain points
        if self.conversation_stage == "discovery":
            self.conversation_stage = "solution"
            
            # Detect pain points
            if any(word in user_lower for word in ['client', 'customer', 'selection', 'upgrade', 'choice']):
                if self.builder_type == "residential":
                    return f"I completely understand - client selections can get overwhelming fast! Our {config.PRODUCT_NAME} has a dedicated client selection and upgrade tracking system that keeps everything organized. Clients can make selections through a portal, you get instant notifications, and everything is documented with pricing automatically updated. We also have photo documentation features so clients can see progress. Would you like to hear more about how this works?"
            
            if any(word in user_lower for word in ['schedule', 'delay', 'coordination', 'timeline']):
                return "Scheduling challenges are one of the top issues we help with! Our system has automated notifications, schedule management, and coordination tools that keep everyone on the same page. You can see at a glance where every project stands and get alerts before small delays become big problems. What's your current process for managing schedules?"
            
            if any(word in user_lower for word in ['budget', 'cost', 'money', 'profit']):
                return "Budget control is critical! Our platform gives you real-time visibility into project costs, tracks change orders automatically, and helps you catch overruns early. You can see exactly where money is going across all your projects. Many of our clients tell us this alone pays for the software. Are you currently using any tools for budget tracking?"
            
            if any(word in user_lower for word in ['multiple', 'several', 'many', 'sites']):
                return "Managing multiple sites is exactly what our platform excels at! You get a dashboard view of all projects, can allocate resources across sites, and track everything in real-time. Your site supervisors can update status from their mobile devices, so you always know what's happening. How many projects are you typically managing at once?"
            
            # Generic discovery response
            return "Those are definitely common challenges in the construction business. Our platform is designed to address exactly these kinds of issues. What would you say is the #1 thing that, if you could fix it, would make the biggest impact on your business?"
        
        # Solution stage - present features and move to pricing
        if self.conversation_stage == "solution":
            self.conversation_stage = "pricing"
            
            if any(word in user_lower for word in ['price', 'cost', 'how much', 'pricing', 'expensive']):
                if self.builder_type == "residential":
                    return f"Great question! For most residential builders, our Professional plan at ${config.PRICING['professional']['price_monthly']}/month is the perfect fit. It includes up to {config.PRICING['professional']['projects']} with {config.PRICING['professional']['users']}. We also have a Starter plan at ${config.PRICING['starter']['price_monthly']}/month if you're running a smaller operation. Most builders tell us they save more than that in the first month from reduced errors and time savings. Would you like to see how it would work for your specific situation?"
                else:  # commercial
                    return f"For commercial operations, we typically recommend our Enterprise plan with custom pricing based on your needs. This gives you unlimited projects and users, plus dedicated support. We'd want to understand your specific requirements in a demo to give you accurate pricing. Would you be open to a 20-minute demo where we can see exactly what you need and provide a custom quote?"
            
            # Ask about demo
            return "I think this could really help solve the challenges you mentioned! Would you be interested in seeing a quick 15-20 minute demo where we can show you exactly how it would work for your business? We can customize it to focus on the features that matter most to you."
        
        # Pricing/Demo stage
        if self.conversation_stage == "pricing":
            if any(word in user_lower for word in ['yes', 'sure', 'okay', 'sounds good', 'interested', 'demo']):
                return f"Perfect! You can book a time that works for you at {config.DEMO_BOOKING_URL}. During the demo, we'll walk through the specific features you need and answer any questions. We can also discuss any integration requirements you might have. Is there anything else you'd like to know before we wrap up?"
            elif any(word in user_lower for word in ['no', 'not now', 'not ready', 'thinking']):
                return "No problem at all! This is a big decision and I completely understand wanting to think it over. I can send you some information to review, and you can reach out whenever you're ready. What's the best email to send that to?"
            elif "think" in user_lower or "consider" in user_lower:
                return "Absolutely, take your time! These decisions are important. Is there anything specific you need to know to help with your evaluation? I'm happy to answer any questions you have."
            else:
                return "I appreciate your interest! To move forward, the best next step would be a quick demo where we can show you exactly how this fits your business. Does that sound good?"
        
        # Default response
        return "That's a great point! Let me make sure I understand your needs correctly. Could you tell me a bit more about what's most important to you in a construction management system?"
    
    def run_demo(self):
        """Run the demo conversation"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{config.COMPANY_NAME} - {config.PRODUCT_NAME}")
        print(f"DEMO MODE (No API Key Required)")
        print(f"{'='*70}{Style.RESET_ALL}\n")
        
        print(f"{Fore.YELLOW}Note: This is demo mode with simulated responses.")
        print(f"For full AI capabilities, configure your OpenAI API key and use sales_agent.py{Style.RESET_ALL}\n")
        
        # Get first response
        response = self.get_response("")
        print(f"{Fore.GREEN}{config.AGENT_NAME}: {Style.RESET_ALL}{response}\n")
        
        # Main loop
        while self.turn_count < 50:
            try:
                user_input = input(f"{Fore.YELLOW}You: {Style.RESET_ALL}").strip()
                
                if not user_input:
                    continue
                
                response = self.get_response(user_input)
                print(f"\n{Fore.GREEN}{config.AGENT_NAME}: {Style.RESET_ALL}{response}\n")
                
                # Exit on goodbye
                if any(word in user_input.lower() for word in ['exit', 'quit', 'bye', 'goodbye']):
                    break
                    
            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}Demo ended.{Style.RESET_ALL}")
                break
            except Exception as e:
                print(f"\n{Fore.RED}Error: {str(e)}{Style.RESET_ALL}\n")
                continue
        
        print(f"\n{Fore.CYAN}Thank you for trying the {config.COMPANY_NAME} Sales Agent Demo!{Style.RESET_ALL}\n")


def main():
    """Main entry point"""
    print(f"{Fore.CYAN}Initializing Builder Sales Agent Demo...{Style.RESET_ALL}")
    agent = DemoSalesAgent()
    agent.run_demo()


if __name__ == "__main__":
    main()
