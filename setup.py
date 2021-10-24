import pathlib
import setuptools
import pkg_resources
from DisFormers import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setuptools.setup(
    name="disformers",
    version=__version__,
    package_dir={"": "DisFormers"},
    packages=setuptools.find_namespace_packages(where="DisFormers"),
    author="SpaceDEV",
    author_email="support@spacedev.space",
    description="Huggingface transformers for discord.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SpaceDEVofficial/disformers",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License"
    ],
    python_requires='>=3.7',
    install_requires=[
        'certifi==2021.5.30',
        'charset-normalizer==2.0.6',
        'click==8.0.1',
        'filelock==3.1.0',
        'huggingface-hub==0.0.17',
        'idna==3.2',
        'importlib-metadata==4.8.1',
        'joblib==1.0.1',
        'numpy==1.21.2',
        'packaging==21.0',
        'Pillow==8.3.2',
        'pyparsing==2.4.7',
        'PyYAML==5.4.1',
        'regex==2021.9.24',
        'requests==2.26.0',
        'sacremoses==0.0.46',
        'six==1.16.0',
        'tokenizers==0.10.3',
        'torch==1.9.1',
        'torchaudio==0.9.1',
        'torchvision==0.10.1',
        'tqdm==4.62.3',
        'transformers==4.11.0',
        'typing-extensions==3.10.0.2',
        'urllib3==1.26.7',
        'zipp==3.5.0',
        "py-cord==1.7.3",
        "requests==2.26.0"
    ]
)
