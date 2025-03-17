import abc

from src.observers.beat_observer import BeatObserver
from src.observers.bpm_observer import BPMObserver


class BeatModelInterface(abc.ABC):
    @abc.abstractmethod
    def initialize(self):
        pass

    @abc.abstractmethod
    def on(self):
        pass

    @abc.abstractmethod
    def off(self):
        pass

    @abc.abstractmethod
    def set_bpm(self, bpm):
        pass

    @abc.abstractmethod
    def get_bpm(self):
        pass

    @abc.abstractmethod
    def register_beat_observer(self, beat_observer: BeatObserver):
        pass

    @abc.abstractmethod
    def remove_beat_observer(self, beat_observer: BeatObserver):
        pass

    @abc.abstractmethod
    def register_bpm_observer(self, bpm_observer: BPMObserver):
        pass

    @abc.abstractmethod
    def remove_bpm_observer(self, bpm_observer: BPMObserver):
        pass
