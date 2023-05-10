from setuptools import find_packages, setup

setup(
    name='smardwrapper',
    packages=find_packages(include=['smardwrapper']),
    version='0.1.0',
    description='A Wrapper for SMARD API',
    author='Eric Kaufmann',
    license='MIT',
    install_requires=['pandas==2.0.1', 'numpy', 'requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.3.1'],
    test_suite='tests',
)