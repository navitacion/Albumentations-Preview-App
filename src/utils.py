import os
import gc
import cv2
import glob
import numpy as np
from PIL import Image
import streamlit as st
import albumentations as A
import torch
from torchvision.utils import make_grid


def load_image(image_name):
    # User Selected Image
    if image_name == 'Upload':
        img = st.file_uploader('Choose Your Pic')
        if img is not None:
            img = Image.open(img)
            img = np.array(img)

    # Pre-Set Image
    else:
        img = cv2.imread(f'./image/{image_name}')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img


def get_transform(cfg):
    transforms = []

    # Select Albumentations Methods
    albu_methods = [k for k in cfg.keys()]

    st.sidebar.subheader('Albumentation Methods')
    apply_methods = st.sidebar.multiselect('Apply', albu_methods)

    # Settings for a specific method
    for method in apply_methods:
        t_cfg = cfg[method]

        # Sub Header
        if t_cfg['url'] is None:
            st.sidebar.subheader(method)
        else:
            # Add Hyperlink to Official Documents
            st.sidebar.subheader(f"[{method}]({t_cfg['url']})")

        # No Argument Method (ex. HorizontalFlip)
        if t_cfg['values'] is None:
            transforms.append(getattr(A, method)(p=1.0))

        else:
            albu_params = {}
            for k in t_cfg['values'].keys():
                st_params = t_cfg['values'][k]
                st_type = st_params.pop('st_type')
                # Streamlit Sidebar
                v = getattr(st.sidebar, st_type)(f'{method} - {k}', **st_params)
                albu_params.update({k: v})
            transforms.append(getattr(A, method)(**albu_params, p=1.0))

    return transforms


def display_images(img, transforms):
    # Original Image
    st.subheader('Original Image')
    st.image(img, use_column_width=True)

    # Transformed Image
    if len(transforms) != 0:
        transform = A.Compose(transforms)
        st.subheader('Transformed Image')
        img_num = st.selectbox('Output Image Num', ['[1x1]', '[2x2]', '[3x3]'])

        # Joint Image
        res = []
        img_num = int(img_num.split('x')[0][-1]) * int(img_num.split('x')[1][0])
        for _ in range(img_num):
            res.append(transform(image=img)['image'])
        # ToTensor
        res = [torch.as_tensor(np.transpose(img, [2,0,1])) for img in res]
        # Joint
        res = make_grid(res, nrow=int(np.sqrt(img_num)), padding=5)
        # ToNumpy
        transformed_img = np.transpose(res.numpy(), [1,2,0])
        # Display
        st.image(transformed_img, use_column_width=True)

        del transformed_img, img, res
        gc.collect()