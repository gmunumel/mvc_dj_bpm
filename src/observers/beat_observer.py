import abc


class BeatObserver(abc.ABC):
    @abc.abstractmethod
    def update_beat(self):
        pass
