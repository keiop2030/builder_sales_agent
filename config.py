"""
Configuration settings for the Builder Sales Agent
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")

# Agent Configuration
COMPANY_NAME = os.getenv("COMPANY_NAME", "BuilderPro Software")
AGENT_NAME = os.getenv("AGENT_NAME", "Sarah")
DEMO_BOOKING_URL = os.getenv("DEMO_BOOKING_URL", "https://calendly.com/your-company/demo")

# Product Information
PRODUCT_NAME = "BuilderPro Suite"
PRODUCT_TAGLINE = "The Complete Construction Management Platform"

# Features for Commercial Builders
COMMERCIAL_FEATURES = [
    "Multi-project management dashboard",
    "Advanced resource allocation across sites",
    "Bid management and proposal generation",
    "Subcontractor coordination tools",
    "Real-time project tracking and analytics",
    "Budget forecasting and cost control",
    "Compliance and permit tracking",
    "Client portal with custom branding",
    "Mobile app for field teams",
    "Integration with accounting systems (QuickBooks, Sage, etc.)"
]

# Features for Residential Builders
RESIDENTIAL_FEATURES = [
    "Home design and floor plan library",
    "Client selection and upgrade tracking",
    "Schedule management with automated notifications",
    "Supplier and vendor management",
    "Purchase order system",
    "Warranty management",
    "Customer communication portal",
    "Photo documentation and progress sharing",
    "Budget tracking and change orders",
    "Integration with design software"
]

# Pricing Tiers
PRICING = {
    "starter": {
        "name": "Starter",
        "price_monthly": 99,
        "price_annual": 990,
        "description": "Perfect for small residential builders",
        "projects": "Up to 5 active projects",
        "users": "2 users included"
    },
    "professional": {
        "name": "Professional",
        "price_monthly": 299,
        "price_annual": 2990,
        "description": "Ideal for growing builder businesses",
        "projects": "Up to 20 active projects",
        "users": "10 users included"
    },
    "enterprise": {
        "name": "Enterprise",
        "price_monthly": "Custom",
        "price_annual": "Custom",
        "description": "For large commercial builders",
        "projects": "Unlimited projects",
        "users": "Unlimited users"
    }
}

# Common pain points the agent should address
PAIN_POINTS = {
    "commercial": [
        "Managing multiple sites simultaneously",
        "Coordinating with numerous subcontractors",
        "Tracking costs across complex projects",
        "Meeting compliance requirements",
        "Communication gaps between office and field"
    ],
    "residential": [
        "Client communication and expectations",
        "Tracking customer selections and upgrades",
        "Managing schedules and delays",
        "Keeping projects profitable",
        "Coordinating trades and vendors"
    ]
}

# Conversation settings
MAX_CONVERSATION_TURNS = 50
CONVERSATION_TEMPERATURE = 0.7
