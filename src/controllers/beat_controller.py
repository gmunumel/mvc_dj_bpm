from src.controllers.controller_interface import ControllerInterface
from src.model.beat_model_interface import BeatModelInterface
from src.views.dj_view import DJView
from src.log import logger


class BeatController(ControllerInterface):
    def __init__(self, model: BeatModelInterface):
        self.model: BeatModelInterface = model
        self.view: DJView = DJView(self, model)
        self.view.create_controls()
        self.view.disable_stop_menu_item()
        self.view.enable_start_menu_item()
        self.model.initialize()
        self.view.start_views()

    def start(self):
        self.model.on()
        self.view.disable_start_menu_item()
        self.view.enable_stop_menu_item()

    def stop(self):
        self.model.off()
        self.view.disable_stop_menu_item()
        self.view.enable_start_menu_item()

    def increase_bpm(self):
        bpm: int = self.model.get_bpm()
        logger.debug("BPM increased to %d, communicate to model", bpm + 1)
        self.model.set_bpm(bpm + 1)

    def decrease_bpm(self):
        bpm: int = self.model.get_bpm()
        logger.debug("BPM decreased to %d, communicate to model", bpm - 1)
        self.model.set_bpm(bpm - 1)

    def set_bpm(self, bpm: int):
        logger.debug("BPM set to %d, communicate to model", bpm)
        self.model.set_bpm(bpm)
