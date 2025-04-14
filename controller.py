from model import EggRollModel
from view import EggRollView

from project_types import RunningStatus, Feedback
# from type_aliases import Grid


class EggRollController:
    def __init__(self, model: EggRollModel, view: EggRollView):
        self.model = model
        self.view = view

    def run(self):
        # new strategy: have a list[DisplayContent] in model, add each increment of movement there
        # then just go through them in controller to print
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

            self.model.reset_movement_frames()
            self.model.roll(user_orders)
            frames_to_display = self.model.movement_frames
            self.model.reset_movement_frames()

            self.view.show_movements_to_user(frames_to_display)

        if self.model.running_status is RunningStatus.DONE:
            self.view.print_game_over_message()





            
            
