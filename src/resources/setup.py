from setuptools import setup, find_packages
import os

script_dir = os.path.dirname(__file__)

rel_path = 'requirements.txt'
abs_file_path = os.path.join(script_dir, rel_path)

requirements = [l.strip() for l in open(abs_file_path).readlines()]

rel_path = 'README.md'

setup(
      name='sa-mobile-phone-number-validator',
      version = '1.0.0',
      packages=find_packages(),
      install_requires=requirements,
      include_package_data=True,
      description='South African Cell Phone Number Validation',
      long_description="\n" + open(rel_path).read(),
)