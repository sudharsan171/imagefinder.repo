from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
import os


class ImageApp(App):
    def build(self):
        # Root layout
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Input field for file name
        self.input_label = Label(text="Enter the name of the image file (without extension):")
        self.layout.add_widget(self.input_label)

        self.file_input = TextInput(multiline=False, hint_text="File name")
        self.layout.add_widget(self.file_input)

        # Button to load the image
        self.load_button = Button(text="Load Image")
        self.load_button.bind(on_press=self.load_image)
        self.layout.add_widget(self.load_button)

        # Image widget to display the image
        self.image_widget = Image()
        self.layout.add_widget(self.image_widget)

        # Label to display errors or status messages
        self.status_label = Label(text="")
        self.layout.add_widget(self.status_label)

        return self.layout

    def load_image(self, instance):
        file_name = self.file_input.text.strip()

        # Check for .jpg or .jpeg file
        if os.path.exists(f"{file_name}.jpg"):
            file_path = f"{file_name}.jpg"
        elif os.path.exists(f"{file_name}.jpeg"):
            file_path = f"{file_name}.jpeg"
        else:
            self.status_label.text = "File not found. Please check the file name and try again."
            self.image_widget.source = ""  # Clear the image
            return

        # Load the image into the Image widget
        self.image_widget.source = file_path
        self.image_widget.reload()  # Ensure the image updates
        self.status_label.text = f"Successfully loaded: {file_path}"


# Run the app
if __name__ == "__main__":
    ImageApp().run()
