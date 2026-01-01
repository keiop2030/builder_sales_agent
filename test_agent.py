"""
Basic tests for the Builder Sales Agent
"""
import sys
import config
from demo_agent import DemoSalesAgent


def test_config_loaded():
    """Test that configuration is properly loaded"""
    print("Testing configuration...")
    assert config.COMPANY_NAME, "Company name should be set"
    assert config.PRODUCT_NAME, "Product name should be set"
    assert len(config.COMMERCIAL_FEATURES) > 0, "Should have commercial features"
    assert len(config.RESIDENTIAL_FEATURES) > 0, "Should have residential features"
    assert "starter" in config.PRICING, "Should have starter pricing"
    assert "professional" in config.PRICING, "Should have professional pricing"
    assert "enterprise" in config.PRICING, "Should have enterprise pricing"
    print("✓ Configuration loaded correctly")


def test_demo_agent_creation():
    """Test that demo agent can be created"""
    print("\nTesting demo agent creation...")
    agent = DemoSalesAgent()
    assert agent is not None, "Agent should be created"
    assert agent.conversation_stage == "greeting", "Should start at greeting stage"
    assert agent.builder_type is None, "Builder type should be None initially"
    print("✓ Demo agent created successfully")


def test_demo_agent_greeting():
    """Test that demo agent provides greeting"""
    print("\nTesting demo agent greeting...")
    agent = DemoSalesAgent()
    response = agent.get_response("")
    assert len(response) > 0, "Should get a response"
    assert config.AGENT_NAME in response, "Response should include agent name"
    assert config.COMPANY_NAME in response, "Response should include company name"
    print("✓ Demo agent greeting works")


def test_demo_agent_residential_flow():
    """Test residential builder conversation flow"""
    print("\nTesting residential builder flow...")
    agent = DemoSalesAgent()
    
    # Greeting
    response1 = agent.get_response("")
    assert len(response1) > 0, "Should get greeting"
    
    # Identify as residential
    response2 = agent.get_response("I'm a residential builder doing about 10 homes per year")
    assert "residential" in response2.lower() or "challenge" in response2.lower(), "Should acknowledge residential builder"
    
    # Mention pain point
    response3 = agent.get_response("Client selections are a nightmare")
    assert "selection" in response3.lower() or "tracking" in response3.lower(), "Should address selection pain point"
    
    print("✓ Residential builder flow works")


def test_demo_agent_commercial_flow():
    """Test commercial builder conversation flow"""
    print("\nTesting commercial builder flow...")
    agent = DemoSalesAgent()
    
    # Greeting
    response1 = agent.get_response("")
    assert len(response1) > 0, "Should get greeting"
    
    # Identify as commercial
    response2 = agent.get_response("We're a commercial contractor with multiple job sites")
    assert "commercial" in response2.lower() or "project" in response2.lower(), "Should acknowledge commercial builder"
    
    print("✓ Commercial builder flow works")


def test_demo_agent_exit():
    """Test that agent handles exit gracefully"""
    print("\nTesting exit handling...")
    agent = DemoSalesAgent()
    response = agent.get_response("bye")
    assert len(response) > 0, "Should get farewell message"
    assert "thank" in response.lower(), "Should thank the prospect"
    print("✓ Exit handling works")


def test_features_are_comprehensive():
    """Test that we have comprehensive features"""
    print("\nTesting feature comprehensiveness...")
    
    # Commercial features should cover key areas
    commercial_features_text = " ".join(config.COMMERCIAL_FEATURES).lower()
    assert "project" in commercial_features_text, "Should mention project management"
    assert "budget" in commercial_features_text or "cost" in commercial_features_text, "Should mention budget/cost"
    
    # Residential features should cover key areas
    residential_features_text = " ".join(config.RESIDENTIAL_FEATURES).lower()
    assert "client" in residential_features_text or "customer" in residential_features_text, "Should mention client management"
    assert "schedule" in residential_features_text, "Should mention scheduling"
    
    print("✓ Features are comprehensive")


def test_pricing_tiers():
    """Test that pricing tiers are properly configured"""
    print("\nTesting pricing tiers...")
    
    starter = config.PRICING["starter"]
    assert starter["price_monthly"] > 0, "Starter should have monthly price"
    assert "projects" in starter["projects"].lower(), "Should mention project limit"
    
    professional = config.PRICING["professional"]
    assert professional["price_monthly"] > starter["price_monthly"], "Professional should cost more than starter"
    
    enterprise = config.PRICING["enterprise"]
    assert enterprise["projects"].lower() == "unlimited projects", "Enterprise should have unlimited projects"
    
    print("✓ Pricing tiers configured correctly")


def run_all_tests():
    """Run all tests"""
    print("="*70)
    print("Running Builder Sales Agent Tests")
    print("="*70)
    
    try:
        test_config_loaded()
        test_demo_agent_creation()
        test_demo_agent_greeting()
        test_demo_agent_residential_flow()
        test_demo_agent_commercial_flow()
        test_demo_agent_exit()
        test_features_are_comprehensive()
        test_pricing_tiers()
        
        print("\n" + "="*70)
        print("✓ All tests passed!")
        print("="*70 + "\n")
        return True
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {str(e)}\n")
        return False
    except Exception as e:
        print(f"\n✗ Error running tests: {str(e)}\n")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
