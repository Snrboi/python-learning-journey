class Agent: # 1. this is the class

    def __init__(self, name, role, active=True):
        self.name = name
        self.role = role
        self.active = active

# 2. Below are the two instances
agent1 = Agent("Researcher", "research") 
agent2 = Agent("Coder", "programming", False) #3. self refers to the object/instance agent 2 when it is being initialized.

agent1.active = False

# 4. agent1.name = "Researcher"
# agent1.active = False

# agent2.name = "Coder"
# agent2.active = False