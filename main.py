from src.model.beat_model_interface import BeatModelInterface
from src.model.beat_model import BeatModel
from src.controllers.controller_interface import ControllerInterface
from src.controllers.beat_controller import BeatController

if __name__ == "__main__":
    model: BeatModelInterface = BeatModel()
    controller: ControllerInterface = BeatController(model)
