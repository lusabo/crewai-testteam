from crewai import Task

class TesterTasks():

    def enhance_test_coverage(self, agent):
        return Task(
            description="Evaluate project code and identify gaps in unit tests and "
                        "create new tests to improve project robustness.",
            expected_output="A list of missing test cases and their referenced unit "
                            "tests written in Go.",
            agent=agent
        )