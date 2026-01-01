# Builder Sales Agent

An AI-powered sales agent designed to sell software for commercial and residential builders. The agent conducts intelligent, consultative sales conversations to understand customer needs, qualify leads, and schedule demos.

## Features

- **Conversational AI**: Natural language interactions powered by OpenAI (GPT-3.5-turbo or GPT-4)
- **Builder-Specific**: Tailored for both commercial and residential construction businesses
- **Consultative Approach**: Asks questions to understand pain points before presenting solutions
- **Lead Qualification**: Identifies prospect needs, company size, and buying timeline
- **Product Knowledge**: Deep understanding of construction management software features
- **Demo Scheduling**: Guides interested prospects to book a demonstration

## Product Features Highlighted

### For Commercial Builders
- Multi-project management dashboard
- Advanced resource allocation across sites
- Bid management and proposal generation
- Subcontractor coordination tools
- Real-time project tracking and analytics
- Budget forecasting and cost control
- Compliance and permit tracking
- Client portal with custom branding
- Mobile app for field teams
- Integration with accounting systems

### For Residential Builders
- Home design and floor plan library
- Client selection and upgrade tracking
- Schedule management with automated notifications
- Supplier and vendor management
- Purchase order system
- Warranty management
- Customer communication portal
- Photo documentation and progress sharing
- Budget tracking and change orders
- Integration with design software

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/keiop2030/builder_sales_agent.git
   cd builder_sales_agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-api-key-here
   COMPANY_NAME=Your Company Name
   AGENT_NAME=Your Agent Name
   DEMO_BOOKING_URL=https://calendly.com/your-company/demo
   ```

## Usage

### Option 1: Demo Mode (No API Key Required)

Try the agent with simulated responses:
```bash
python demo_agent.py
```

This demo mode provides a fully functional conversation experience without requiring an OpenAI API key. Perfect for testing and evaluation!

### Option 2: Full AI Mode (Requires OpenAI API Key)

Run the full AI-powered sales agent:
```bash
python sales_agent.py
```

The agent will greet you and begin a conversation. Simply respond naturally to the agent's questions. The agent will:
1. Identify if you're a commercial or residential builder
2. Understand your current challenges and pain points
3. Recommend relevant features from the software
4. Answer questions about pricing and capabilities
5. Offer to schedule a personalized demo

Type `exit`, `quit`, or `goodbye` to end the conversation.

### View Example Conversations

See example sales scenarios:
```bash
python examples.py        # Show menu
python examples.py 1      # Show specific example
```

### Run Tests

Validate the agent is working correctly:
```bash
python test_agent.py
```

## Example Conversation

```
======================================================================
BuilderPro Software - BuilderPro Suite
======================================================================

Sarah: Hello! I'm Sarah from BuilderPro Software. We help builders like you 
streamline their operations with our complete construction management platform. 
Are you working on commercial or residential projects, and what brought you 
here today?

You: We're a residential builder doing about 15 homes per year.

Sarah: That's wonderful! Building 15 homes a year means you're juggling quite 
a bit. What are some of the biggest challenges you're facing right now in 
managing those projects? Is it coordinating with trades, keeping clients updated, 
or something else?

You: Honestly, tracking all the client selections and upgrades is a nightmare.

Sarah: I completely understand - client selections can get overwhelming fast! 
Our BuilderPro Suite has a dedicated client selection and upgrade tracking 
system that keeps everything organized. Clients can make selections through 
a portal, you get instant notifications, and everything is documented with 
pricing automatically updated. Would you like to see how this works in a 
quick demo?
```

## Configuration

You can customize the agent behavior by editing `config.py`:

- **Product features**: Add or modify features for commercial/residential builders
- **Pricing tiers**: Update pricing information
- **Pain points**: Add common customer challenges the agent should address
- **Conversation settings**: Adjust AI temperature and response length

## Requirements

- Python 3.8+
- OpenAI API key (only required for full AI mode with `sales_agent.py`)
- Internet connection

## Dependencies

- `openai>=1.0.0` - OpenAI API client
- `python-dotenv>=1.0.0` - Environment variable management
- `colorama>=0.4.6` - Cross-platform colored terminal output

## Project Structure

```
builder_sales_agent/
├── sales_agent.py       # Main AI agent (requires OpenAI API)
├── demo_agent.py        # Demo mode with simulated responses (no API needed)
├── config.py            # Configuration and product information
├── examples.py          # Example conversation scenarios
├── test_agent.py        # Test suite
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Customization

To customize for your specific software product:

1. **Update product information** in `config.py`:
   - Product name and tagline
   - Features lists for commercial and residential
   - Pricing tiers
   - Common pain points

2. **Adjust agent personality** by modifying the system prompt in `sales_agent.py`

3. **Change conversation style** by adjusting the `CONVERSATION_TEMPERATURE` in `config.py`

## How It Works

1. **Initialization**: Loads configuration and OpenAI API credentials
2. **Greeting**: Agent introduces itself and asks qualifying questions
3. **Discovery**: Through conversation, identifies builder type and pain points
4. **Consultation**: Recommends relevant features based on stated needs
5. **Qualification**: Determines fit and buying timeline
6. **Call-to-Action**: Offers demo scheduling for interested prospects

## Best Practices

- Keep your OpenAI API key secure and never commit it to version control
- Test conversations to ensure the agent maintains your brand voice
- Update product features regularly to keep information current
- Monitor conversations to refine the agent's approach
- Adjust the system prompt based on feedback

## Security Notes

- API keys are loaded from environment variables
- `.env` file is gitignored to prevent accidental commits
- No sensitive customer data is stored by default

## Future Enhancements

Potential improvements:
- Lead information extraction and CRM integration
- Multi-language support
- Voice interface option
- Conversation analytics and reporting
- Email follow-up automation
- Integration with scheduling systems
- Sentiment analysis to gauge interest level

## License

This project is provided as-is for use in selling builder software.

## Support

For questions or issues, please open an issue in the GitHub repository.

---

**Note**: This agent requires an OpenAI API key. Usage will incur costs based on OpenAI's pricing. Monitor your API usage to manage costs effectively.
