# Albumentations-Preview-App

## What's is this?

This app is Demo of Image Augmentation Library "Albumentations"


## Set up (Local)

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

### Citing

```commandline
@Article{info11020125,
    AUTHOR = {Buslaev, Alexander and Iglovikov, Vladimir I. and Khvedchenya, Eugene and Parinov, Alex and Druzhinin, Mikhail and Kalinin, Alexandr A.},
    TITLE = {Albumentations: Fast and Flexible Image Augmentations},
    JOURNAL = {Information},
    VOLUME = {11},
    YEAR = {2020},
    NUMBER = {2},
    ARTICLE-NUMBER = {125},
    URL = {https://www.mdpi.com/2078-2489/11/2/125},
    ISSN = {2078-2489},
    DOI = {10.3390/info11020125}
}
```