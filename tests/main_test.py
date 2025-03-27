from src.model.beat_model_interface import BeatModelInterface
from src.model.beat_model import BeatModel
from src.controllers.controller_interface import ControllerInterface
from src.controllers.beat_controller import BeatController


def test_main(caplog):
    pass
    # model: BeatModelInterface = BeatModel()
    # controller: ControllerInterface = BeatController(model)
    # assert "Pygame mixer initialized" in caplog.text
    # assert "Loading audio file resources/audio/clap.wav" in caplog.text
    # controller.increase_bpm()
    # assert "BPM increased to 91, communicate to model" in caplog.text
    # controller.decrease_bpm()
    # assert "BPM decreased to 90, communicate to model" in caplog.text
