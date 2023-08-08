```python
# CyberQuest/deployment/config.py

class Config:
    """
    Configuration class for CyberQuest application.
    """
    def __init__(self):
        """
        Initialize configuration parameters.
        """
        self.AI_MODULE_PATH = "../src/ai_module.py"
        self.QUANTUM_MODULE_PATH = "../src/quantum_module.py"
        self.AR_MODULE_PATH = "../src/ar_module.py"
        self.METAPHYSICS_MODULE_PATH = "../src/metaphysics_module.py"
        self.MUSIC_MODULE_PATH = "../src/music_module.py"
        self.CRYPTOGRAPHY_MODULE_PATH = "../src/cryptography_module.py"
        self.ETHICS_MODULE_PATH = "../src/ethics_module.py"

        self.USER_SCHEMA_PATH = "../schemas/user.json"
        self.CHALLENGE_SCHEMA_PATH = "../schemas/challenge.json"
        self.QUANTUM_ALGORITHM_SCHEMA_PATH = "../schemas/quantum_algorithm.json"
        self.METAPHYSICAL_CONNECTION_SCHEMA_PATH = "../schemas/metaphysical_connection.json"
        self.KNOWLEDGE_SCHEMA_PATH = "../schemas/knowledge.json"
        self.GUARDIANSHIP_SCHEMA_PATH = "../schemas/guardianship.json"

        self.DOM_ELEMENT_IDS = {
            "cyberQuestApp": "#cyberQuestApp",
            "quantumAlgorithms": "#quantumAlgorithms",
            "metaphysicalConnections": "#metaphysicalConnections",
            "multidimensionalChallenges": "#multidimensionalChallenges",
            "alchemyOfKnowledge": "#alchemyOfKnowledge",
            "etherealGuardianship": "#etherealGuardianship"
        }

        self.MESSAGE_NAMES = {
            "initCyberQuest": "initCyberQuest",
            "updateQuantumAlgorithms": "updateQuantumAlgorithms",
            "updateMetaphysicalConnections": "updateMetaphysicalConnections",
            "updateMultidimensionalChallenges": "updateMultidimensionalChallenges",
            "updateAlchemyOfKnowledge": "updateAlchemyOfKnowledge",
            "updateEtherealGuardianship": "updateEtherealGuardianship"
        }

        self.FUNCTION_NAMES = {
            "init": "init",
            "updateQuantumAlgorithms": "updateQuantumAlgorithms",
            "updateMetaphysicalConnections": "updateMetaphysicalConnections",
            "updateMultidimensionalChallenges": "updateMultidimensionalChallenges",
            "updateAlchemyOfKnowledge": "updateAlchemyOfKnowledge",
            "updateEtherealGuardianship": "updateEtherealGuardianship"
        }
```