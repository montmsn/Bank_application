from pathlib import Path
from itertools import cycle
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageSequence
import time
import dashboard


class AnimatedGif(ttk.Frame):
    def __init__(self, master,username):
        super().__init__(master, width=400, height=300)
        self.username = username
        # open the GIF and create a cycle iterator
        file_path = Path(__file__).parent / "assets/spinners.gif"
        with Image.open(file_path) as im:
            # create a sequence
            sequence = ImageSequence.Iterator(im)
            images = [ImageTk.PhotoImage(s) for s in sequence]
            self.image_cycle = cycle(images)

            # length of each frame
            self.framerate = im.info["duration"]

        self.img_container = ttk.Label(self, image=next(self.image_cycle))
        self.img_container.pack(fill="both", expand="yes")
        self.after(self.framerate, self.next_frame)
        self.after(5000, self.close_window)

    def close_window(self):
        """Close the window and call another function"""
        self.destroy()
        dashboard.dashboard(self.username)  # Call another function after closing the window
        

    def next_frame(self):
        """Update the image for each frame"""
        self.img_container.configure(image=next(self.image_cycle))
        self.after(self.framerate, self.next_frame)


def strat_animate(username):

    app = ttk.Window("Animated GIF", themename="superhero")

    gif = AnimatedGif(app,username)
    gif.pack(fill=BOTH, expand=YES)

    app.mainloop(10)
