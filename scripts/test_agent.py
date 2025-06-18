from agent.core import create_agent

def test_basic_prompt():
    agent = create_agent()
    response = agent.run("What is 5 times 7?")
    assert "35" in response