import requests
import numpy as np
import PIL.Image

import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Load the image
image_url = 'https://www.google.co.uk/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
image = PIL.Image.open(requests.get(image_url, stream=True).raw)

# Resize the image to the desired dimensions
image = image.resize((224, 224))

# Convert the image to a NumPy array
image_array = np.array(image)

# Normalize the pixel values to be between 0 and 1
image_array = image_array / 255.0

# Encode the image using OpenAI's CLIP model
image_encoding = openai.Completion.create(engine="davinci", prompt=image_array.tolist(), max_tokens=200)

# Get the manipulation prompt from the user
manipulation_prompt = input("Enter a prompt for image manipulation: ")

# Combine the image encoding and manipulation prompt
combined_prompt = f"{image_encoding.choices[0].text}{manipulation_prompt}"

# Generate text completion based on the combined prompt
completion_result = openai.Completion.create(engine="davinci", prompt=combined_prompt, max_tokens=200)

# Extract the manipulated image text from the completion result
manipulated_image_text = completion_result.choices[0].text

# Decode the manipulated image text into a NumPy array
manipulated_image_array = np.array(eval(manipulated_image_text))

# Rescale the pixel values to the 0-255 range
manipulated_image_array = manipulated_image_array * 255.0
manipulated_image_array = manipulated_image_array.astype(np.uint8)

# Create a PIL image from the manipulated array
manipulated_image = PIL.Image.fromarray(manipulated_image_array)

# Display the manipulated image
manipulated_image.show()
