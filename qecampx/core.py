"""QECampX core."""


class QECampX:
    """Representation of QECampX object."""

    def __init__(self, name, score=1.0):
        """Initialize QECampX object."""
        self.name = name
        self.score = score

    @property
    def score_average(self):
        """Return annual score average."""
        return self.score / 12
