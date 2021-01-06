import os
import pickle

class MLPlay:
    def __init__(self, side) -> None:
        """
        init is not a constructor
        """
        self.ball_served = False
        self.side = side

        with open(os.path.join(os.path.dirname(__file__), 'save', 'model.pickle'),  'rb') as f:
            self.model = pickle.load(f)