from setuptools import setup

setup(
    name='todoist',
    version='0.1.0',
    py_modules=['todoist'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'todoist = app:todoist',
        ],
    },
)
