import os
from setuptools import setup

requires = []
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    requires = f.read().splitlines()

setup(name='xview',
      version='1.0.0',
      packages=['xview'],
      install_requires=requires,
      include_package_data=True,
      package_data={'xview': ['xview_class_labels.txt']}
      )
