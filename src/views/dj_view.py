import sys
import tkinter as tk
from tkinter import ttk

from src.observers.beat_observer import BeatObserver
from src.observers.bpm_observer import BPMObserver
from src.controllers.controller_interface import ControllerInterface
from src.model.beat_model_interface import BeatModelInterface
from src.log import logger


class DJView(BeatObserver, BPMObserver):
    def __init__(self, controller: ControllerInterface, model: BeatModelInterface):
        self.controller: ControllerInterface = controller
        self.model: BeatModelInterface = model
        self.model.register_beat_observer(self)
        self.model.register_bpm_observer(self)
        self.view_frame = tk.Tk()
        self.progress = tk.IntVar()
        self.beat_bar = ttk.Progressbar(
            self.view_frame,
            orient=tk.HORIZONTAL,
            length=200,
            mode="determinate",
            variable=self.progress,
        )
        self.bpm_output_label = tk.Label(self.view_frame, text="Current BPM: 120")

        self.control_frame = tk.Tk()
        self.bpm_label = tk.Label(self.control_frame, text="Enter BPM:")
        self.bpm_text_field = tk.Entry(self.control_frame, width=9)
        self.set_bpm_button = tk.Button(
            self.control_frame, text="Set BPM", command=self._set_bpm
        )
        self.increase_bpm_button = tk.Button(
            self.control_frame, text=">>", command=self._increase_bpm
        )
        self.decrease_bpm_button = tk.Button(
            self.control_frame, text="<<", command=self._decrease_bpm
        )

        self.menu_frame = tk.Menu(self.control_frame)
        self.dj_control = tk.Menu(self.menu_frame, tearoff=0)

    def start_views(self):
        self.view_frame.mainloop()
        self.control_frame.mainloop()

    def create_controls(self):
        self.view_frame.title("View")
        self.view_frame.geometry("200x35+0+0")
        self.control_frame.title("Control")
        self.control_frame.geometry("200x110+300+0")
        self.beat_bar.config(maximum=200)
        self.control_frame.grid_columnconfigure(0, weight=1)
        self.control_frame.grid_columnconfigure(1, weight=1)
        self.bpm_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.bpm_text_field.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.set_bpm_button.grid(
            row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew"
        )
        self.decrease_bpm_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        self.increase_bpm_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self._create_menu_items()
        self._pack_controls()

    def _create_menu_items(self):
        self.menu_frame.add_cascade(label="DJ Control", menu=self.dj_control)
        self.dj_control.add_command(label="Start", command=self._command_start)
        self.dj_control.add_command(label="Stop", command=self._command_stop)
        self.dj_control.add_separator()
        self.dj_control.add_command(label="Quit", command=self._command_quit)
        self.control_frame.config(menu=self.menu_frame)

    def _pack_controls(self):
        self.beat_bar.pack()
        self.bpm_output_label.pack()

    def update_beat(self):
        bpm: int = self.model.get_bpm()
        self.progress.set(bpm)

    def update_bpm(self):
        bpm: int = self.model.get_bpm()
        if bpm == 0:
            self.bpm_output_label.config(text="Offine")
        else:
            self.bpm_output_label.config(text=f"Current BPM: {bpm}")
            self.progress.set(bpm)

    def enable_start_menu_item(self):
        self.dj_control.entryconfig("Start", state="normal")

    def disable_start_menu_item(self):
        self.dj_control.entryconfig("Start", state="disabled")

    def enable_stop_menu_item(self):
        self.dj_control.entryconfig("Stop", state="normal")

    def disable_stop_menu_item(self):
        self.dj_control.entryconfig("Stop", state="disabled")

    def _set_bpm(self):
        bpm = 90
        try:
            bpm = int(self.bpm_text_field.get())
        except ValueError:
            logger.error("Invalid BPM value")
        self.controller.set_bpm(bpm)
        logger.debug("Setting BPM to %d", bpm)

    def _increase_bpm(self):
        self.controller.increase_bpm()
        logger.debug("Increasing BPM")

    def _decrease_bpm(self):
        self.controller.decrease_bpm()
        logger.debug("Decreasing BPM")

    def _command_start(self):
        self.controller.start()

    def _command_stop(self):
        self.controller.stop()

    def _command_quit(self):
        logger.debug("Quitting DJ View. Bye!")
        sys.exit(0)
