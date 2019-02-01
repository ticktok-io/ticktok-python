import os

from setuptools import setup, find_packages

requirementsPath = '%s/requirements.txt' % os.path.dirname(os.path.realpath(__file__))
with open(requirementsPath) as f:
    requirements = [line for line in f.read().splitlines() if len(line) > 0],

setup(
    name="ticktok",
    packages=find_packages(),
    install_requires=requirements,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
