```python
import music21

class AlchemyOfKnowledge:
    def __init__(self):
        self.music_theory = music21.theory

    def analyze_harmony(self, music_piece):
        """
        Analyze the harmony of a given music piece using music21 library
        """
        harmony = self.music_theory.analyzer.analyze('harmony', music_piece)
        return harmony

    def analyze_counterpoint(self, music_piece):
        """
        Analyze the counterpoint of a given music piece using music21 library
        """
        counterpoint = self.music_theory.analyzer.analyze('counterpoint', music_piece)
        return counterpoint

    def analyze_form(self, music_piece):
        """
        Analyze the form of a given music piece using music21 library
        """
        form = self.music_theory.analyzer.analyze('form', music_piece)
        return form

    def analyze_pitch(self, music_piece):
        """
        Analyze the pitch of a given music piece using music21 library
        """
        pitch = self.music_theory.analyzer.analyze('pitch', music_piece)
        return pitch

alchemyOfKnowledge = AlchemyOfKnowledge()
```