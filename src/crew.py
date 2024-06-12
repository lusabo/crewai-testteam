
from crewai import Crew, Process
from agents.tester import TesterAgents
from tasks.tester_task import TesterTasks

class DeveloperTeamCrew:

    def __init__(self, num_agents):
        self.num_agents = num_agents
        self.agents = []
        self.tasks = []
        
    def run(self):

        for i in range(self.num_agents):
            self.agents.append(TesterAgents().tester_agent())
            self.tasks.append(TesterTasks().enhance_test_coverage(self.agents[i]))
        
        crew = Crew(
            agents = self.agents,
            tasks = self.tasks,
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        return result