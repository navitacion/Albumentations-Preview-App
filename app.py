import os
import cv2
import glob
import yaml
import streamlit as st
import albumentations as A


def setting_sidebar(cfg):
    transforms = []

    # Select Albumentations Methods
    albu_methods = [k for k in cfg.keys()]

    st.sidebar.subheader('Albumentation Methods')
    apply_methods = st.sidebar.multiselect('Apply', albu_methods)

    # Settings for a specific method
    for method in albu_methods:
        # Add only Selected Method
        if method in apply_methods:
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
                select_params = {}
                for k in t_cfg['values'].keys():
                    params = t_cfg['values'][k]
                    st_type = params.pop('st_type')

                    v = getattr(st.sidebar, st_type)(f'{method} - {k}', **params)
                    select_params.update({k: v})
                transforms.append(getattr(A, method)(**select_params, p=1.0))

    return cfg, transforms


def app():
    st.title('Albumantation Demo App')

    # Select Image
    st.subheader('Image')
    image_files = glob.glob('./image/*')
    image_files = [os.path.basename(path) for path in image_files]
    image_name =  st.selectbox('Select Original Image', image_files)

    # Load Original Image
    img = cv2.imread(f'./image/{image_name}')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    st.subheader('Image Info')
    st.markdown(f'(Height, Width) : ({img.shape[0]}, {img.shape[1]})')

    # Setting Sidebar
    with open('config.yml') as file:
        cfg = yaml.safe_load(file)
    cfg, transforms = setting_sidebar(cfg)

    # Display Image  -----------------------------------------------------
    # Original Image
    st.subheader('Original Image')
    st.image(img, use_column_width=True)

    # Transformed Image
    if len(transforms) != 0:
        transform = A.Compose(transforms)
        transformed_img = transform(image=img)['image']
        st.subheader('Transformed Image')
        st.image(transformed_img, use_column_width=True)


if __name__ == '__main__':
    app()


