from crew import DeveloperTeamCrew

if __name__ == "__main__":

    num_agents = 1

    crew = DeveloperTeamCrew(num_agents)
    result = crew.run()
    print(result)