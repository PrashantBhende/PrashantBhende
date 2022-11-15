class QAAgent:
    def __init__(self, role):
        self.role = role
    def process_ticket(self, ticket_id):
        return f"Agent [{self.role}] analyzing ticket {ticket_id} for regressions..."

class MultiAgentCoordinator:
    def __init__(self, agents):
        self.agents = agents
    def run_workflow(self, ticket_id):
        for agent in self.agents:
            print(agent.process_ticket(ticket_id))

if __name__ == "__main__":
    coord = MultiAgentCoordinator([QAAgent("RootCause"), QAAgent("FixVerifier")])
    coord.run_workflow("BUG-4096")