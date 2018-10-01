from setuptools import setup, find_packages


setup(
    name='sa-mobile-phone-number-validator',
    version='1.0.0',
    packages=find_packages(),
    license="MIT",
    install_requires=['nose2==0.8.0',
                      'pycodestyle==2.4.0'],
    test_suite='nose2.collector.collector',
    include_package_data=True,
    description='South African Cell Phone Number Validation',
    long_description="\n" + open('README.md').read()
)
