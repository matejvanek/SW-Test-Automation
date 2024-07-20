from setuptools import setup, find_packages

setup(
    name="EXAM_ReportCompareApp",
    version="0.1",
    packages=find_packages(include=['source']), # Search root directory for all packages; or specify by include=['source']
    entry_points={
        'console_scripts': [
            'EXAM_ReportCompareApp = main:hello_world',
        ],
    },
)

'''
$ pip install -e .

Now, install in editable mode (with the -e flag, note the . at the end), so that Python will direct any import operation to the package folder under development (instead of copying the codes to another disk location, e.g., site-packages) and any updates to the codes will be reflected the next time the Python interpreter is run.
'''