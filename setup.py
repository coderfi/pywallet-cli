from setuptools import setup

setup(name='pywallet-cli',
      version='0.1',
      description='Basic pywallet CLI',
      url='http://github.com/coderfi/pywallet_cli',
      author='Fairiz Azizi',
      author_email='coderfi@gmail.com',
      license='Apache License 2.0',
      packages=['pywallet_cli'],
      entry_points = {
          'console_scripts': [
              'pywallet-cli=pywallet_cli.cli:main'
          ]
      },
      zip_safe=True)
