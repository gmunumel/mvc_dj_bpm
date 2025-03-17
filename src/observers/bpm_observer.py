import abc


class BPMObserver(abc.ABC):
    @abc.abstractmethod
    def update_bpm(self):
        pass
