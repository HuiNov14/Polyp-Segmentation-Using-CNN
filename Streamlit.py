import torch
import torch.nn.functional as F
import numpy as np
import os
from PIL import Image
from HarDMSEG import HarDMSEG
import streamlit as st

# Load the pre-trained model
model = HarDMSEG()
model.load_state_dict(torch.load('/content/HarD-MSEG-best.pth'))
model.cuda()
model.eval()

# Function to process the image and generate segmentation result
def process_image(image):
    image = image.convert("RGB")
    image_tensor = torch.unsqueeze(transform_image(image), 0).cuda()
    res = model(image_tensor)
    res = F.interpolate(res, size=image.size, mode='bilinear', align_corners=False)
    res = res.sigmoid().data.cpu().numpy().squeeze()
    res = (res - res.min()) / (res.max() - res.min() + 1e-8)
    return res

# Function to transform the image
def transform_image(image):
    image = image.resize((352, 352))  # Resize the image to the required input size
    image = np.array(image)  # Convert PIL image to numpy array
    image = image.transpose((2, 0, 1))  # Transpose the dimensions to (channels, height, width)
    image = image.astype(np.float32) / 255.0  # Normalize the image
    image = torch.from_numpy(image)  # Convert numpy array to torch tensor
    return image

# Streamlit app
def main():
    # Set the title and sidebar
    st.title("Image Segmentation")
    st.sidebar.title("Settings")

    # Upload the image file
    uploaded_file = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Process the image and generate segmentation result
        result = process_image(image)

        # Display the segmentation result
        st.image(result, caption="Segmentation Result", use_column_width=True)

if __name__ == '__main__':
    main()