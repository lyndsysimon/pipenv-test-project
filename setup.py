from setuptools import setup


setup(
    name='Test project for pipenv dependency resolution',
    version='1.0.0',
    install_requires=[
        'git-noop==1.2.3',
    ],
    dependency_links=[
        'git+ssh://git@github.com/lyndsysimon/git-noop.git@v1.2.3#egg=git-noop-1.2.3',
    ],
)
