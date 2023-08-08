```python
class EtherealGuardianship:
    def __init__(self, user):
        self.user = user
        self.ethics_score = 0

    def responsible_disclosure(self, vulnerability):
        """
        Method to simulate responsible disclosure of a vulnerability.
        Increases the user's ethics score.
        """
        self.ethics_score += 1
        print(f"{self.user} responsibly disclosed a vulnerability!")

    def ethical_practices(self, action):
        """
        Method to simulate ethical practices in hacking.
        Increases the user's ethics score.
        """
        self.ethics_score += 1
        print(f"{self.user} performed an ethical action: {action}")

    def protect_digital_realm(self):
        """
        Method to simulate the protection of the digital realm.
        Increases the user's ethics score.
        """
        self.ethics_score += 1
        print(f"{self.user} protected the digital realm!")

    def get_ethics_score(self):
        """
        Method to get the user's current ethics score.
        """
        return self.ethics_score
```