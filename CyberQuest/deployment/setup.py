```python
from setuptools import setup, find_packages

setup(
    name='CyberQuest',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Add your project dependencies here
        # For example:
        # 'numpy==1.15.4',
        # 'pandas==0.23.4',
    ],
    entry_points='''
        [console_scripts]
        cyberQuest=cyberQuest:cli
    ''',
)
```