import os
import kaggle

def download_dataset(owner_slug='andrewmvd', dataset_slug='sp-500-stocks', path='src/data'):
    api = kaggle.KaggleApi()
    api.authenticate()
    api.dataset_download_files(f'{owner_slug}/{dataset_slug}', path=path, unzip=True)


