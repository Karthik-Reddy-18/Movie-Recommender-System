from setuptools import setup
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
AUTHOR_NAME='KARTHIK REDDY'
SRC_REPO='src'
LIST_OF_REQUIREMENTS=['streamlit']


setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='karthikreddyboya21@gmail.com',
    description='movie recommender system',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package=[SRC_REPO],
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS
)