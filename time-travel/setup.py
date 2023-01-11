from setuptools import setup, find_packages

setup(
    name='time-travel',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'time-travel = time_travel.time_travel:main',
        ],
    },
    install_requires=[
        'gitpython',
        'argparse',
    ],
)
