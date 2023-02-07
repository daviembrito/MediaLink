'''
Video to Audio Converter
Coded by: daviembrito
Version: 0.1
'''

from pytube import YouTube
from pytube.exceptions import RegexMatchError
import customtkinter as ctk

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue")
CORNER_RADIUS = 50

class App(ctk.CTk):

    def __init__(self:ctk.CTk):
        super().__init__()

        self.format = "mp3"
        self.path = None

        self.geometry("400x400")
        self.title("Video to Audio Converter")
        self.resizable(False, False)

        self.buildApp()

    # Download audio from video
    def convert(self):
        try:
            yt = YouTube(self.url_entry.get())
        except RegexMatchError:
            self.print("[WARNING] No URL inserted\n")
            return

        filename = yt.title.replace(' ', '_')
        stream = yt.streams.get_audio_only()
        stream.download(filename=f"{filename}.{self.format}", output_path=self.path)

        self.print(f"[OK] Audio download at: {self.path}/{filename}.{self.format}")

    # Get download folder path
    def getPath(self):
        path = ctk.filedialog.askdirectory()
        if len(path) != 0:
            self.path = path
            self.print(f"[OK] Download folder: {path}\n")

    # Build the GUI
    def buildApp(self):

        # Main frame
        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(pady=15, padx=15, fill="both", expand=True)

        # Program name
        self.program_name = ctk.CTkLabel(
                    master=self.frame, 
                    justify=ctk.LEFT, 
                    text="Video to Audio Converter")
        self.program_name.pack(pady=10, padx=10)

        # URL entry
        self.url_entry = ctk.CTkEntry(
                    master=self.frame, 
                    placeholder_text="Video URL",
                    justify="center",
                    corner_radius=CORNER_RADIUS,
                    width=300)
        self.url_entry.pack(pady=10, padx=10)

        # Choose folder button
        self.path_button = ctk.CTkButton(
                    master=self.frame, 
                    text='Choose folder', 
                    command=self.getPath, 
                    width=220,
                    corner_radius=CORNER_RADIUS,
                    state=ctk.NORMAL)
        self.path_button.pack(pady=10, padx=10)

        # Convert button
        self.convert_button = ctk.CTkButton(
                    master=self.frame, 
                    text='Convert',
                    command=self.convert,
                    width=70,
                    corner_radius=CORNER_RADIUS,
                    state=ctk.NORMAL)
        self.convert_button.pack(pady=10, padx=10)

        # Output textbox
        self.output_textbox = ctk.CTkTextbox(
                    master=self.frame,
                    height=140,
                    width=400,
                    corner_radius=CORNER_RADIUS/2,
                    state="disabled")
        self.output_textbox.pack(pady=10, padx=10)

    # Print logs into the textbox
    def print(self, message):
        self.output_textbox.configure(state="normal")

        self.output_textbox.insert("end", message)
        self.output_textbox.see("end")

        self.output_textbox.configure(state="disabled")

if __name__ == "__main__":
    app = App()
    app.mainloop()
