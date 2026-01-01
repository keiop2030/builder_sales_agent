# Quick Start Guide

Get started with the Builder Sales Agent in under 5 minutes!

## For Quick Testing (No Setup Required)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the demo:**
   ```bash
   python demo_agent.py
   ```

3. **Try a conversation:**
   - Say you're a residential or commercial builder
   - Mention pain points like "client selections" or "budget tracking"
   - Ask about pricing
   - Request a demo

That's it! The demo mode works without any API keys.

## For Full AI Capabilities

1. **Get an OpenAI API key:**
   - Go to https://platform.openai.com/api-keys
   - Create a new API key
   - Copy the key (starts with "sk-")

2. **Configure the environment:**
   ```bash
   cp .env.example .env
   ```

3. **Edit `.env` and add your key:**
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   COMPANY_NAME=Your Company Name
   AGENT_NAME=Sarah
   DEMO_BOOKING_URL=https://calendly.com/your-company/demo
   ```

4. **Run the full AI agent:**
   ```bash
   python sales_agent.py
   ```

## What to Customize

### 1. Product Information (config.py)

Update these to match your actual software:
- `PRODUCT_NAME` - Your product name
- `COMPANY_NAME` - Your company name
- `COMMERCIAL_FEATURES` - Features for commercial builders
- `RESIDENTIAL_FEATURES` - Features for residential builders
- `PRICING` - Your actual pricing tiers

### 2. Agent Personality (sales_agent.py)

Modify the system prompt in the `get_system_prompt()` method to adjust:
- Agent tone and style
- Sales approach
- Qualification questions
- Feature presentation strategy

### 3. Demo Booking URL (.env)

Update `DEMO_BOOKING_URL` with your actual calendar link:
- Calendly
- HubSpot Meetings
- Microsoft Bookings
- Or any other scheduling tool

## Testing Your Changes

After customizing, run the tests:
```bash
python test_agent.py
```

All tests should pass. If not, check your configuration.

## Usage Examples

### View Example Conversations
```bash
python examples.py          # Show menu
python examples.py 1        # Residential builder scenario
python examples.py 2        # Commercial builder scenario
python examples.py 3        # Price-sensitive prospect
python examples.py 4        # Early stage prospect
```

### Test the Demo Agent
```bash
python demo_agent.py
```

Example conversation:
```
Sarah: Hello! I'm Sarah from BuilderPro Software...
You: I'm a residential builder doing 10 homes a year
Sarah: That's wonderful! What are your biggest challenges?
You: Client selections are overwhelming
Sarah: I completely understand! Our client selection tracking...
```

## Common Issues

### "ModuleNotFoundError: No module named 'openai'"
Run: `pip install -r requirements.txt`

### "Error: OPENAI_API_KEY not found"
- Either use `demo_agent.py` (no key needed)
- Or configure your API key in `.env`

### Agent responses seem generic
- The demo mode uses pre-programmed responses
- For adaptive AI conversations, use `sales_agent.py` with OpenAI API

## Next Steps

1. **Test with real prospects:** Observe which questions work best
2. **Refine the system prompt:** Adjust based on feedback
3. **Track conversations:** Monitor what leads to demos
4. **Iterate on features:** Update product info as you add features
5. **Integrate with CRM:** Consider adding lead capture functionality

## Getting Help

- Read the full [README.md](README.md) for detailed documentation
- Review [examples.py](examples.py) for conversation patterns
- Check [config.py](config.py) for all configuration options

## Quick Checklist

- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Demo mode tested (`python demo_agent.py`)
- [ ] Product information updated in `config.py`
- [ ] OpenAI API key configured in `.env` (for full AI mode)
- [ ] Tests passing (`python test_agent.py`)
- [ ] Demo booking URL configured
- [ ] Agent personality customized (optional)

Ready to sell! 🚀
