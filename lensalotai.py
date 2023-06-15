import requests
import numpy as np
import PIL.Image

import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Function to process image manipulation prompts
def manipulate_image(image_array, manipulation_prompt):
    # Normalize the pixel values to be between 0 and 1
    image_array = image_array / 255.0

    # Encode the image using OpenAI's Clip model
    image_encoding = openai.Image(image_array)

    # Perform image manipulation using OpenAI's DALL·E model
    response = openai.DALL_E.edit(image_encoding, manipulation_prompt)

    # Decode the manipulated image
    manipulated_image_array = response['output']

    # Rescale the pixel values to the 0-255 range
    manipulated_image_array = manipulated_image_array * 255.0
    manipulated_image_array = manipulated_image_array.astype(np.uint8)

    # Create a PIL image from the manipulated array
    manipulated_image = PIL.Image.fromarray(manipulated_image_array)

    # Display the manipulated image
    manipulated_image.show()

# Get user input for the desired option
print("Choose an option:")
print("1. Create image from prompts only")
print("2. Manipulate an uploaded file")
option = int(input("Enter your option (1 or 2): "))

if option == 1:
    # Get the manipulation prompt from the user
    manipulation_prompt = input("Enter a prompt for image creation: ")

    # Generate the image using prompts
    response = openai.DALL_E.create(prompt=manipulation_prompt)

    # Get the image URL from the response
    image_url = response['image']

    # Load the image
    image = PIL.Image.open(requests.get(image_url, stream=True).raw)

    # Display the generated image
    image.show()

elif option == 2:
    # Get the file path from the user
    file_path = input("Enter the path of the file to be uploaded: ")

    try:
        # Load the image from the file
        image = PIL.Image.open(file_path)

        # Manipulation prompt for the user to provide
        manipulation_prompt = input("Enter a prompt for image manipulation: ")

        # Perform image manipulation
        manipulate_image(np.array(image), manipulation_prompt)

    except FileNotFoundError:
        print("File not found. Please make sure the file path is correct.")

else:
    print("Invalid option. Please choose 1 or 2.")
