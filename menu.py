# [IMPORT] Utilities
from modules.clear_screen import clear_screen
from modules.display_format import display_format
from modules.delay import delay
from modules.display_header import display_header
from modules.display_line import display_line
from modules.success_message import success_message
from modules.error_message import error_message
from modules.line_delay_animation import line_delay_animation
from modules.press_enter_to_continue import press_enter_to_continue

# [IMPORT] Libraries
from PIL import Image # for loading/saving images
import numpy as np

""" Classes """
class User:
    # Constructor
    def __init__(self, img_URL=""):
        self.img_URL = img_URL
        img = Image.open(img_URL)
        self.set_img(img, img_URL)

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
    # * [FUNCTION: Transform] Flip image horizontally or vertically
    def flip_image(self):
        img = self.get_img()

        # [ERROR] No image loaded
        if img is None:
            error_message("No image loaded to flip", 2)
            return
        
        # Convert image to matrix
        matrix = np.array(self.get_img())

        # Prompt user to flip image horizontally or vertically
        while True:
            user_input = input("Flip [H]orizontal or [V]ertical?: ").strip()
            if user_input.lower() not in ['h', 'v']:
                error_message("Invalid input, please enter 'H' to flip horizontally or 'V' to flip vertically", 2)
            else: break

        user_input = user_input[0]

        # Flip based on user input
        if user_input[0] == 'h':
            # Flip the matrix horizontally
            flipped_matrix = np.fliplr(matrix)
        elif user_input[0] == 'v':
            # Flip the matrix vertically
            flipped_matrix = np.flipud(matrix)

        # Update current image
        flipped_img = Image.fromarray(flipped_matrix)
        success_message(f"Image '{self.get_img_URL()}' flipped successfully!", 1)

        # Save flipped image
        self.set_img(flipped_img, self.get_img_URL())

        # Output saved image
        self.save_image()
        press_enter_to_continue()

    # * [FUNCTION: Transform] Crop image within a specified dimension
    def crop_image(self):
        img = self.get_img()

        # [ERROR] No image loaded
        if img is None:
            error_message("No image loaded to flip", 2)
            return
        
        # Prompt user to enter dimensions to crop
        while True:
            # Convert image to matrix
            matrix = np.array(self.get_img())
            print(f"Image Dimensions: {matrix.shape[0]} x {matrix.shape[1]}")

            try:
                input_dimensions = input("Enter dimension (e.g. 200 x 200): ").strip()

                width_str, height_str = [s.strip() for s in input_dimensions.lower().split('x')]
                
                width = int(width_str)
                height = int(height_str)

                break

            except Exception as e:
                error_message("Invalid input, please enter a valid dimension (e.g. 200 x 200)", 2)
                return

        # Crop matrix using specified width and height
        cropped_matrix = matrix[0:height, 0:width]

        # Update current image
        cropped_img = Image.fromarray(cropped_matrix)
        success_message(f"Image '{self.get_img_URL()}' cropped successfully!", 1)

        # Save cropped image
        self.set_img(cropped_img, self.get_img_URL())

        # Output saved image
        self.save_image()
        press_enter_to_continue()

    # * [FUNCTION: Transform] Scale vectors' pixel values to [0, 1]
    def normalize_image(self):
        img = self.get_img()

        # [ERROR] No image loaded
        if img is None:
            error_message("No image loaded to flip", 2)
            return

        # Convert image to matrix and normalize it
        matrix = np.array(img).astype(np.float32)
        normalized_matrix = matrix / 255.0

        # Update current image
        normalized_img = Image.fromarray(np.clip(normalized_matrix * 255, 0, 255).astype(np.uint8))

        # Save flipped image
        self.set_img(normalized_img, self.get_img_URL())

        # Save normalized matrix (for machine learning)
        np.save(f"{self.get_img_URL()}_normalized.npy", normalized_matrix)
        success_message(f"Image '{self.get_img_URL()}' normalized successfully!", 1)
        success_message(f"Normalized matrix saved as {self.get_img_URL()}.npy", 1)

        # Output saved image
        self.save_image()
        press_enter_to_continue()

    # * [FUNCTION: Transform] Apply threshold-based binarization (converting color values to either black or white)
    def binarize(self):
        img = self.get_img()

        # [ERROR] No image loaded
        if img is None:
            error_message("No image loaded to flip", 2)
            return

        # convert image to grayscale
        img = Image.open("sample-image.jpg").convert("L")

        # Prompt user to enter threshold
        while True:
            try:
                input_threshold = int(input("Enter threshold for binarization (max.: 255): ").strip())

                # [ERROR] Out-of-range threshold
                if input_threshold < 0 or input_threshold > 255:
                    error_message("Out of range, please enter a valid threshold (0-255)", 2)
                else: break
                
            except Exception as e:
                error_message("Invalid input, please enter a valid threshold (0-255)", 2)
                return
        
        # Convert image to matrix
        matrix = np.array(img)
        binarized_matrix = np.where(matrix > input_threshold, 255, 0)

        # Update current image
        binarized_img = Image.fromarray(binarized_matrix.astype(np.uint8))

        # Save binarized image
        self.set_img(binarized_img, self.get_img_URL())

        # Output saved image
        self.save_image()
        press_enter_to_continue()


    # * [FUNCTION: Transform] Invert color images
    def invert_colors(self):
        img = self.get_img()

        # [ERROR] No image loaded
        if img is None:
            error_message("No image loaded to flip", 2)
            return

        # Convert image to matrix
        matrix = np.array(img)
        inverted_matrix = 255 - matrix

        # Update current image
        inverted_img = Image.fromarray(inverted_matrix)

        # Save color-inverted image
        self.set_img(inverted_img, self.get_img_URL())

        # Output saved image
        self.save_image()
        press_enter_to_continue()

    def blur_image(self):
        pass

    def sharpen_image(self):
        pass

    def edge_detect(self):
        pass

    # * [FUNCTION: Transform] Convert image to 1D vector
    def flatten_image(self):
        img = self.get_img()

        # [ERROR] No image loaded
        if img is None:
            error_message("No image loaded to flip", 2)
            return

        # Convert image to matrix and flatten it
        matrix = np.array(img)
        flattened_matrix = matrix.flatten()
        
        # Update current image
        normalized_img = Image.fromarray(flattened_matrix)

        # Save flattened image
        self.set_img(normalized_img, self.get_img_URL())

        # Save flattened matrix (for machine learning)
        np.save(f"{self.get_img_URL()}_flattened.npy", flattened_matrix)
        success_message(f"Flattened matrix saved as {self.get_img_URL()}.npy", 1)

        reshaped_matrix = flattened_matrix.reshape(matrix.shape)
        display_img = Image.fromarray(reshaped_matrix)

        # Save converted image from flattened 1D vector
        self.set_img(normalized_img, self.get_img_URL())

        # Output saved image
        self.save_image()
        press_enter_to_continue()

    """ Load & Save Image """
    # * [FUNCTION]: Load image via path or URL
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

    # * [FUNCTION]: Save the image output
    def save_image(self):
        img = self.get_img()
        if img is None:
            error_message("No image loaded to save", 2)
            return

        save_path = input("Enter filename to save image (default: output.png): ").strip()
        try:
            if save_path == '':
                save_path = "output.png"
            else:
                self.set_img_URL(save_path)
            img.save(save_path)
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
            4: ('binarize', 'Binarize'),
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
            line_delay_animation("  `~`~`~ [ NumPix ] ~`~`~`", 0.1)
            display_format('#', 27)

            # Dynamically display list of operations
            for index, (function_name, description) in self.function_list.items():
                line_delay_animation(f"{' ' if index < 10 else ''}[{index}] | {description}", 0.05)
            display_format('#', 27)

            try:
                user_choice = int(input(">> ").strip())
                if user_choice not in self.function_list:
                    print("Invalid input, please enter a valid choice")
                    continue

                # Call the method dynamically
                method_name = self.function_list[user_choice][0]
                method_description = self.function_list[user_choice][1]

                if hasattr(self.user, method_name):
                    # Clear screen and display header
                    clear_screen()
                    display_header("NumPix", method_description, '#', 12, False)
                    getattr(self.user, method_name)()
                else:
                    print(f"Function {method_name} unknown.")

            except ValueError as e:
                print(f"Invalid input: {e}")

""" Main Method """
if __name__ == '__main__':
    user = User('sample-image.jpg')
    init = Menu()
    init.display_main_menu()