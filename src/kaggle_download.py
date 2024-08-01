import os
import kaggle

def download_dataset(owner_slug, dataset_slug, path='src/data'):
    api = kaggle.KaggleApi()
    api.authenticate()
    api.dataset_download_files(f'{owner_slug}/{dataset_slug}', path=path, unzip=True)

if __name__ == "__main__":
    owner_slug = 'andrewmvd'
    dataset_slug = 'sp-500-stocks'
    download_dataset(owner_slug, dataset_slug)
