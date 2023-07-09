import zipfile
import os
from .conftest import tmp_path, resources_path


def test_create_zip_file():
    file_dir = os.listdir(resources_path)

    with zipfile.ZipFile(os.path.join(tmp_path, 'resources.zip'), mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(resources_path, file)
            zf.write(add_file)


def test_zip_file():
    with zipfile.ZipFile(os.path.join(tmp_path, 'resources.zip'), mode='a') as zf:
        files = [os.path.basename(file.filename) for file in zf.infolist()]
        # files = []
        # for file in zf.infolist():
        #     name = os.path.basename(file.filename)
        #     files.append(name)
        print(files)

        assert 'docs-pytest-org-en-latest.pdf' in files
        assert 'file_example_XLSX_50.xlsx' in files

    os.remove(os.path.join(tmp_path, 'resources.zip'))
