import abc


class ControllerInterface(abc.ABC):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def increase_bpm(self):
        pass

    @abc.abstractmethod
    def decrease_bpm(self):
        pass

    @abc.abstractmethod
    def set_bpm(self, bpm: int):
        pass
