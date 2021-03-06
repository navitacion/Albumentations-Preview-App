# Albumentations-Preview-App

## What's is this?

This app is Demo of Image Augmentation Library "Albumentations"

![Streamlit](https://user-images.githubusercontent.com/42016148/104123128-9d07e800-538c-11eb-8bad-a64ba278fef2.gif)

## Library

- Albumentations 0.5.2

- Streamlit 0.74.1


## Get Started

This app is already deployed by Streamlit Shareing.

Click [Here](https://share.streamlit.io/navitacion/albumentations-preview-app/app.py) and try it!

### Work by Local

Execute the following command

```
docker build -t albu-preview-app .
docker run -it --rm -p 8501:8501 -v $(pwd):/workspace albu-preview-app bash
streamlit run app.py 
```

Then, Access the following URL

```
http://localhost:8501/
```

### Pre-Set Images

- mt-fuji.jpg
    - Citing from [pixabay](https://pixabay.com/images/id-477832/)

    
- mona-lisa.jpg
    - Citing from [pixabay](https://pixabay.com/photos/art-painting-mona-lisa-classic-74050/)
  

- manhattan.jpg
    - Citing from [pixabay](https://pixabay.com/photos/architecture-new-york-city-manhattan-1853552/)
  