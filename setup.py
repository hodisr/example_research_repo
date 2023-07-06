from __future__ import unicode_literals
from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='iguazio_example',
      author="Pagaya ml engineering team",
      description="An example repository",
      packages=find_packages(),
      install_requires=[
            'joblib==0.13.2',
            'numpy==1.17.0',
            'pandas==0.25.0',
            'pyarrow==0.14.1',
            'python-dateutil==2.8.0',
            'pytz==2019.2',
            'scikit-learn==0.21.3',
            'scipy==1.10.0',
            'six==1.12.0',
            'xgboost==0.90',
      ],)

