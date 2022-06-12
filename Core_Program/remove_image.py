import os

def remove_mode(current_IP):
    target_directory = './Main-Image-Captured/'
    image_list_directory = os.listdir(target_directory)
    for images in image_list_directory:
        if images.startswith(current_IP) and images.endswith(".png"):
            target_image = target_directory + images
            os.remove(target_image)

if __name__ == '__main__':
    remove_mode()
