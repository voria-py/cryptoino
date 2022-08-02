from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
        # the name must match the folder name 'verysimplemodule'
        name="cryptoino", 
        version='0.5.0',
        author="Amirhossein Khosravi",
        author_email="me@amirkho.ir",
        url="https://github.com/amirkho-py/cryptoino",
        license='MIT',
        description='cryptocurrencies information from coingecko',
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        
        # add any additional packages that 
        # needs to be installed along with your package.
        install_requires=["requests"], 
        
        keywords=['cryptoino', 'coingecko' , 'crypto info' , 'crypto price' , 'cryptocurrencies'],
        classifiers= [
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.10',
        ]
)