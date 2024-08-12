import os
import kaggle
import zipfile

def download_dataset(owner_slug='andrewmvd', dataset_slug='sp-500-stocks', path='src/data'):
    api = kaggle.KaggleApi()
    api.authenticate()
    api.dataset_download_file(f'{owner_slug}/{dataset_slug}', file_name='sp500_companies.csv', path=path)
    api.dataset_download_file(f'{owner_slug}/{dataset_slug}', file_name='sp500_index.csv', path=path)
    api.dataset_download_file(f'{owner_slug}/{dataset_slug}', file_name='sp500_stocks.csv', path=path)

    zip_path = os.path.join(path, 'sp500_stocks.csv' + '.zip')
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(path)
        os.remove(zip_path)