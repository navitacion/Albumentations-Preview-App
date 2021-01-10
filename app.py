import os
import cv2
import glob
import yaml
from PIL import Image
import streamlit as st
import albumentations as A
import torch
from torchvision.utils import make_grid

from src.utils import load_image, get_transform, display_images


def app():
    st.title('Albumantations Demo App')
    st.markdown(f'Albumentations Version: {A.__version__}')

    # Select Image
    st.subheader('Image')
    image_files = glob.glob('./image/*')
    image_files = ['Upload'] + [os.path.basename(path) for path in image_files]
    image_name =  st.selectbox('Select Pic', image_files)

    # Load Image
    img = load_image(image_name)

    if img is not None:
        st.subheader('Image Info')
        st.markdown(f'(Height, Width) : ({img.shape[0]}, {img.shape[1]})')

        # Setting Sidebar
        with open('config.yml') as file:
            cfg = yaml.safe_load(file)
        transforms = get_transform(cfg)

        # Display Image  -----------------------------------------------------
        display_images(img, transforms)


if __name__ == '__main__':
    app()


