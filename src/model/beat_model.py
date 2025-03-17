import time
import posixpath

from typing import List
from threading import Thread

import pygame

from src.model.beat_model_interface import BeatModelInterface
from src.observers.beat_observer import BeatObserver
from src.observers.bpm_observer import BPMObserver
from src.log import logger

AUDIO_FILE = posixpath.join("resources", "audio", "clap.wav")


class BeatModel(BeatModelInterface):
    def __init__(self):
        self.beat_observers: List[BeatObserver] = []
        self.bpm_observers: List[BPMObserver] = []
        self.bpm: int = 90
        self.thread = None
        self.stop: bool = False
        self.audio = None
        self._initialize_mixer()

    def _initialize_mixer(self):
        try:
            pygame.mixer.init()
            logger.debug("Pygame mixer initialized")
        except Exception as e:
            logger.error("Failed to initialize pygame mixer: %s", e)

    def initialize(self):
        try:
            logger.debug("Loading audio file %s", AUDIO_FILE)
            pygame.mixer.music.load(AUDIO_FILE)
        except FileNotFoundError as e:
            logger.error("Error: %s", e)
        except Exception as e:
            logger.error("Unexpected error: %s", e)
            self.audio = None

    def on(self):
        self.bpm = self.get_bpm()
        self._notify_bpm_observers()
        self.thread = Thread(target=self._run, daemon=True)
        self.stop = False
        self.thread.start()

    def _run(self):
        while not self.stop:
            self._play_beat()
            self._notify_beat_observers()
            time.sleep(60 / self.get_bpm())

    def off(self):
        self._stop_beat()
        self.stop = True

    def set_bpm(self, bpm: int):
        self.bpm = bpm
        logger.debug("BPM set to %d, notifying observers", bpm)
        self._notify_bpm_observers()

    def get_bpm(self):
        return self.bpm

    def register_beat_observer(self, beat_observer: BeatObserver):
        self.beat_observers.append(beat_observer)

    def remove_beat_observer(self, beat_observer: BeatObserver):
        self.beat_observers.remove(beat_observer)

    def register_bpm_observer(self, bpm_observer: BPMObserver):
        self.bpm_observers.append(bpm_observer)

    def remove_bpm_observer(self, bpm_observer: BPMObserver):
        self.bpm_observers.remove(bpm_observer)

    def _notify_beat_observers(self):
        for observer in self.beat_observers:
            observer.update_beat()

    def _notify_bpm_observers(self):
        for observer in self.bpm_observers:
            observer.update_bpm()

    def _play_beat(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.music.play()

    def _stop_beat(self):
        pygame.mixer.music.stop()
