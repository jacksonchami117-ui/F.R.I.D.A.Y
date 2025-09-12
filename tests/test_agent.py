"""Test for the agent_b_renderer module."""
import sys
import os

# Add the agents directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'agents', 'agent_b_renderer'))

def test_agent_import():
    """Test that we can import the main agent module."""
    try:
        import main
        assert True  # If we get here, import was successful
    except ImportError as e:
        assert False, f"Failed to import agent module: {e}"


def test_agent_module_exists():
    """Test that the agent file exists and is readable."""
    agent_path = os.path.join(os.path.dirname(__file__), '..', 'agents', 'agent_b_renderer', 'main.py')
    assert os.path.exists(agent_path), "Agent main.py file should exist"
    assert os.path.isfile(agent_path), "Agent main.py should be a file"