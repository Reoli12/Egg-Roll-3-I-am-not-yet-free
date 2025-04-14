from model import EggRollModel
from view import EggRollView

class EggRollController:
    def __init__(self, model: EggRollModel, view: EggRollView):
        self.model = model
        self.view = view