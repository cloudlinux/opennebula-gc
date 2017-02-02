from setuptools import setup

with open('./requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='opennebula-gc',
    version='0.1',
    description='OpenNebula Garbage Collector',
    license='MIT',
    packages=['opennebula_gc'],
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'console_scripts': [
            'opennebula-gc = opennebula_gc.cli:main',
        ],
    }
)
