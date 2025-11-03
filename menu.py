# [IMPORT] Utilities
from modules.character_delay_animation import character_delay_animation
from modules.clear_screen import clear_screen
from modules.display_format import display_format
from modules.delay import delay
from modules.display_function import display_function
from modules.display_header import display_header
from modules.display_line import display_line
from modules.error_message import error_message
from modules.insert_spaces import insert_spaces
from modules.line_delay_animation import line_delay_animation
from modules.press_enter_to_continue import press_enter_to_continue

# [IMPORT] Functions (image transformation)
from functions import *

""" CLASS """
class User:
    # Constructor
    def __init__(self, img_URL=""):
        self.img_URL = img_URL

    # Getters & Setters
    def get_img_URL(self):
        return self.img_URL
        
    def set_img_URL(self, img_URL):
        self.img_URL = img_URL

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
                if hasattr(self, method_name):        # class method
                    getattr(self, method_name)()
                elif method_name in globals():         # standalone function
                    globals()[method_name](self.user)
                else:
                    print(f"Function {method_name} not implemented yet.")

            except ValueError as e:
                print(f"Invalid input: {e}")

# [MAIN] Main method
if __name__ == '__main__':
    user = User()
    init = Menu()
    init.display_main_menu()