from setuptools import setup, find_packages

setup(
    name='kaggl_air',
    version='0.1',
    packages=find_packages(),
    description='easy downloader of datasets from kaggle.com',
    author='Your Name',
    author_email='edgarabasov1@gmail.com',
    url='https://github.com/Metaphysicist1/kaggl.air',  # Replace with your URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
            'flake8',
        ],
    },
)