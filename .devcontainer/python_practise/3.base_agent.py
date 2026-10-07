from abc import ABC, abstractmethod
from typing import Any

# Create an Abstract BAse Class

class BaseAgent(ABC): # This is abstract class as it is inheriting from ABC Abstract class module
    def __init__(self, name: str, tools: list = None):
        self.name = name
        self.tools = tools or []
        self.memory = []

    @abstractmethod    # Tis is the abstractmethod that we are creating in Abstarct class . which will make sure it runs in every agent
    def run(self, task: str) -> str:
        """ Every Agent must Implement This """
        pass

# Test it by creating instance of the class
# agent = BaseAgent(name="Sandeep")

# It will throw this error - TypeError: Can't instantiate abstract class BaseAgent without an implementation for abstract method 'run'
# So we cannot instantiate a class with unimplemented abstract method

# 2. So now try to create a subclass -> Try writing a MarketResearchAgent that inherits from BAseAgent class and implements run

class MarketResearchAgent(BaseAgent):
    def run(self, task: str) -> str:
        self.memory = task
        return f"{self.name} resreached {task}"
    

# Test it

agent1 = MarketResearchAgent(name="MarketBot", tools = ["stock_api", "news_api"])
result = agent1.run("Analyse Stock")
print(result)
print(agent1.memory)
print(agent1.tools)

# 2c. Add a tools interface. Instead of tools being plain strings make them callable functions and add method to call a tool by name

class BaseAgent1(ABC):
    def __init__(self, name: str, tools: dict = None):
        self.name = name
        self.tools = tools or {}   # dict: {"tool_name": function}
        self.memory = []

    @abstractmethod
    def run(self, task: str) -> str:
        pass

    def call_tools(self, tool_name: str, *args, **kwargs):
        if tool_name not in self.tools:
            raise ValueError(f"Tool {tool_name} not available in {self.name}")
        return self.tools[tool_name](*args, **kwargs)


# For now leave it like this only as it looked a bit confusing. We will do it literally , but got the point





