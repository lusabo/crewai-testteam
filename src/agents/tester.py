from crewai import Agent
from config import EnvConfig
from tools.tools import Tools

class TesterAgents():

    def __init__(self) -> None:
        self.tools = []
        self.tools.append(Tools().github_tool())

    def tester_agent(self):
        return Agent(
            role="Unit Testing Specialist in Go",
            goal="Create unit tests for Go project.",
            backstory="This agent is an expert in testing with broad "
                      "knowledge in testing applications developed in Go. "
                      "It reviews the code, identifies gaps in"
                      "tests and writes new unit tests to ensure the"
                      "project is robust and reliable.",
            verbose=True,
            allow_delegation=False,
            tools=self.tools,  
            llm=EnvConfig().get_llama3(),
            max_rpm=3
        )