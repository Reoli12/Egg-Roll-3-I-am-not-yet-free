from model import EggRollModel
from view import EggRollView

from project_types import RunningStatus, Feedback

class EggRollController:
    def __init__(self, model: EggRollModel, view: EggRollView):
        self.model = model
        self.view = view

    def run(self):
        while self.model.running_status is RunningStatus.ONGOING:
            while True:
                user_moves = self.view.get_user_moves()
                match self.model.get_feedback(user_moves):
                    case Feedback.VALID:
                        break
                    case Feedback.INVALID:
                        self.view.print_invalid_characters_message()

            assert user_moves
            user_orders = self.model.parse_user_moves(user_moves)

            
            
