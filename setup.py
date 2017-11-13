from setuptools import setup, find_packages

setup(name='wcxf',
      version='0.1',
      author='David M. Straub, Jason Aebischer',
      author_email='david.straub@tum.de, jason.aebischer@tum.de',
      license='MIT',
      packages=['wcxf'],
      package_data={
      'wcxf':['data/*.yml']
      },
      install_requires=['pyyaml'],
      entry_points={
        'console_scripts': [
            'wcxf-convert = wcxf.cli:convert',
            'wcxf-translate = wcxf.cli:translate',
            'wcxf-match = wcxf.cli:match',
            'wcxf-validate = wcxf.cli:validate',
        ]
      },
    )
