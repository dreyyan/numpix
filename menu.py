# [IMPORT] Utilities
from modules.character_delay_animation import character_delay_animation
from modules.clear_screen import clear_screen
from modules.display_format import display_format
from modules.delay import delay
from modules.display_function import display_function
from modules.display_header import display_header
from modules.display_line import display_line
from modules.success_message import success_message
from modules.error_message import error_message
from modules.insert_spaces import insert_spaces
from modules.line_delay_animation import line_delay_animation
from modules.press_enter_to_continue import press_enter_to_continue

# [IMPORT] Libraries
from PIL import Image # for loading/saving images
import numpy as np

""" CLASS """
class User:
    # Constructor
    def __init__(self, img_URL=""):
        self.img_URL = img_URL
        self.img = None

    """ Getters & Setters """
    def get_img_URL(self):
        return self.img_URL
        
    def set_img_URL(self, img_URL):
        self.img_URL = img_URL

    def get_img(self):
        return self.img
        
    def set_img(self, img, img_URL):
        self.img = img
        self.img_URL = img_URL

    """ Image Transformation """
    def flip_image(self):
        pass

    def crop_image(self):
        pass
    def normalize_image(self):
        pass

    def threshold_binarize(self):
        pass

    def invert_colors(self):
        pass

    def blur_image(self):
        pass

    def sharpen_image(self):
        pass

    def edge_detect(self):
        pass

    def flatten_image(self):
        pass

    """ Load & Save Image """
    def load_image(self):
        while True:
            img_URL = input("Enter image path or URL: ").strip()
            try:
                img = Image.open(img_URL)
                self.set_img(img, img_URL)
                success_message(f"Image {self.get_img_URL()} loaded!", 3)
                break
            except Exception as e:
                error_message(f"Failed to load message, please try again", 3)

    def save_image(self):
        img = self.get_img()
        if img is None:
            error_message("No image loaded to save", 2)
            return

        save_path = input("Enter filename to save image (e.g., output.png): ").strip()
        try:
            img.save(save_path)
            self.set_img_URL(save_path)
            success_message(f"Image saved as {save_path}", 1)
        except Exception as e:
            error_message(f"Failed to save image: {e}", 2)


    def exit_program(self):
        exit(0)

class Menu:
    def __init__(self):
        self.user = user
        # Mapping menu numbers to method names and descriptions
        self.function_list = {
            1: ('flip_image', 'Flip Image'),
            2: ('crop_image', 'Crop Image'),
            3: ('normalize_image', 'Normalize Image'),
            4: ('threshold_binarize', 'Threshold / Binarize'),
            5: ('invert_colors', 'Invert Colors'),
            6: ('blur_image', 'Blur Image'),
            7: ('sharpen_image', 'Sharpen Image'),
            8: ('edge_detect', 'Edge Detection'),
            9: ('flatten_image', 'Flatten Image'),
            10: ('load_image', 'Load Image'),
            11: ('save_image', 'Save Image'),
            0: ('exit_program', 'Exit')
        }

    # [FUNCTION] Display main menu
    def display_main_menu(self):
        while True:
            clear_screen()

            index: int = 1 # to keep track of the current function index

            # Display UI
            line_delay_animation("`~`~`~ [ NumPix ] ~`~`~`", 0.1)
            display_format('#', 28)

            # Dynamically display list of operations
            for index, (function_name, description) in self.function_list.items():
                line_delay_animation(f"{' ' if index < 10 else ''}[{index}] | {description}", 0.1)
            display_format('#', 28)

            try:
                user_choice = int(input(">> ").strip())
                if user_choice not in self.function_list:
                    print("Invalid input, please enter a valid choice")
                    continue

                # Call the method dynamically
                method_name = self.function_list[user_choice][0]
                if hasattr(self.user, method_name):
                    getattr(self.user, method_name)()
                else:
                    print(f"Function {method_name} not implemented yet.")

            except ValueError as e:
                print(f"Invalid input: {e}")

# [MAIN] Main method
if __name__ == '__main__':
    user = User()
    init = Menu()
    init.display_main_menu()