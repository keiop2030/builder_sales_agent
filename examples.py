"""
Example conversation scenarios for the Builder Sales Agent
"""

# Example 1: Residential Builder - Client Selection Pain Point
EXAMPLE_1 = """
Scenario: A residential builder struggling with tracking client selections

Agent: Hello! I'm Sarah from BuilderPro Software. We help builders like you 
streamline their operations with our complete construction management platform. 
Are you working on commercial or residential projects, and what brought you here today?

Prospect: We're a residential builder doing about 15 homes per year.

Agent: That's wonderful! Building 15 homes a year means you're juggling quite a bit. 
What are some of the biggest challenges you're facing right now in managing those 
projects? Is it coordinating with trades, keeping clients updated, or something else?

Prospect: Honestly, tracking all the client selections and upgrades is a nightmare.

Agent: I completely understand - client selections can get overwhelming fast! Our 
BuilderPro Suite has a dedicated client selection and upgrade tracking system that 
keeps everything organized. Clients can make selections through a portal, you get 
instant notifications, and everything is documented with pricing automatically 
updated. We also have a photo documentation feature so clients can see progress 
on their home. Would you like to see how this works in a quick demo?

Prospect: That sounds interesting. How much does it cost?

Agent: Great question! For a builder of your size, our Professional plan at $299/month 
would be perfect. It supports up to 20 active projects and includes 10 user accounts. 
You'd get all the features we discussed plus our mobile app for your field teams. 
Many builders tell us they save that in labor costs within the first month just from 
reduced phone calls and emails. Would you like me to send you our demo booking link 
so we can show you exactly how it would work for your business?

Expected Outcome: Qualified lead, demo scheduled
"""

# Example 2: Commercial Builder - Multi-Project Management
EXAMPLE_2 = """
Scenario: A commercial builder managing multiple job sites

Agent: Hello! I'm Sarah from BuilderPro Software. We help builders like you 
streamline their operations with our complete construction management platform. 
Are you working on commercial or residential projects, and what brought you here today?

Prospect: We're a commercial contractor. We usually have 3-4 projects running 
simultaneously, and I'm looking for better project management tools.

Agent: Managing multiple commercial sites at once - that's quite an operation! 
I'd love to understand what's driving your search. Are you looking to solve specific 
pain points with your current setup, or are you growing and need more robust tools?

Prospect: Both really. We're growing, but also our current spreadsheet system isn't 
cutting it. We need better visibility across all our sites.

Agent: That makes perfect sense. Spreadsheets can only take you so far! Our multi-project 
management dashboard is built exactly for this. You can see real-time status across all 
your sites, track resource allocation, monitor budgets, and spot potential issues before 
they become problems. We also have mobile apps so your site supervisors can update status 
instantly. What types of commercial work do you focus on - office buildings, retail, 
industrial?

Prospect: Mostly office buildings and retail spaces.

Agent: Perfect! Many of our commercial clients in those sectors use our compliance and 
permit tracking features heavily, along with the client portal for keeping building 
owners updated. Are you currently using any software for estimating or accounting that 
you'd need us to integrate with?

Expected Outcome: Deep qualification, moving toward demo
"""

# Example 3: Price-Sensitive Prospect
EXAMPLE_3 = """
Scenario: A smaller builder concerned about cost

Agent: Hello! I'm Sarah from BuilderPro Software. We help builders like you 
streamline their operations with our complete construction management platform. 
Are you working on commercial or residential projects, and what brought you here today?

Prospect: I'm a small residential builder. I only do 3-4 projects at a time. 
I've been looking at software but everything seems so expensive.

Agent: I hear you - when you're running a lean operation, every dollar matters! The 
good news is we have a Starter plan designed exactly for builders at your stage. It's 
$99/month and handles up to 5 active projects with 2 user accounts. What are you 
currently using to manage your projects?

Prospect: Mostly paper and some Excel spreadsheets.

Agent: Got it. So here's the thing - while $99 might seem like an investment, let me 
ask: how much time do you spend each week on paperwork, making phone calls to follow 
up with subs or clients, or looking for information? Most builders your size tell us 
they spend 10-15 hours a week on this administrative stuff.

Prospect: Yeah, probably at least 10 hours.

Agent: So if our system could save you even half that time - 5 hours a week - that's 
20 hours a month. What's your time worth? Even at $50/hour, that's $1,000 in value 
for a $99 investment. Plus, you'll avoid costly mistakes like missed selections or 
scheduling conflicts. Would it be worth 15 minutes to see exactly how it works for 
a small operation like yours?

Expected Outcome: Overcome price objection, schedule demo
"""

# Example 4: Just Browsing / Early Stage
EXAMPLE_4 = """
Scenario: A prospect in early research phase

Agent: Hello! I'm Sarah from BuilderPro Software. We help builders like you 
streamline their operations with our complete construction management platform. 
Are you working on commercial or residential projects, and what brought you here today?

Prospect: I'm just looking around. Not really ready to buy anything yet.

Agent: No problem at all! I appreciate you being upfront. Sometimes the best 
conversations start with just exploring what's out there. Are you currently using 
any software for managing your projects, or are you in growth mode looking at options 
for the future?

Prospect: We're using something now but it's pretty basic. Just want to see what else 
is available.

Agent: Smart approach - it's always good to know what's out there. Without getting 
into a full pitch, I'm curious: if you could wave a magic wand and fix one thing about 
your current setup, what would it be?

Prospect: I guess better communication with clients. They're always calling asking 
about status.

Agent: That's one of the top pain points we hear! Our client portal with automated 
notifications really helps with that - clients can check progress, see photos, and 
get updates without calling you. But since you're in research mode, would it be 
helpful if I sent you some information you could review on your own time? No pressure, 
just so you have it when you're ready to make a decision.

Expected Outcome: Soft follow-up opportunity, building relationship
"""

def print_example(example_num: int):
    """Print a specific example"""
    examples = {
        1: ("Residential Builder - Client Selection Challenge", EXAMPLE_1),
        2: ("Commercial Builder - Multi-Project Management", EXAMPLE_2),
        3: ("Price-Sensitive Prospect", EXAMPLE_3),
        4: ("Early Stage / Just Browsing", EXAMPLE_4)
    }
    
    if example_num in examples:
        title, content = examples[example_num]
        print(f"\n{'='*70}")
        print(f"EXAMPLE {example_num}: {title}")
        print(f"{'='*70}")
        print(content)
        print(f"{'='*70}\n")
    else:
        print(f"Example {example_num} not found. Choose 1-4.")


def print_all_examples():
    """Print all examples"""
    for i in range(1, 5):
        print_example(i)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        try:
            example_num = int(sys.argv[1])
            print_example(example_num)
        except ValueError:
            print("Please provide a number between 1 and 4")
    else:
        print("\nBuilder Sales Agent - Example Conversations")
        print("=" * 70)
        print("\nAvailable examples:")
        print("  1. Residential Builder - Client Selection Challenge")
        print("  2. Commercial Builder - Multi-Project Management")
        print("  3. Price-Sensitive Prospect")
        print("  4. Early Stage / Just Browsing")
        print("\nUsage: python examples.py [1-4]")
        print("Or run without arguments to see this menu\n")
