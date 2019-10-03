from setuptools import setup, find_packages
'''
Version numbering will follow major.minor.patch
patch is backward compatible bug fix
minor is backward compatible new feature
major is non backward compatible new feature

Add required packages as needed.
'''


setup(name='proxysource',
      version='0.0.1',
      description='Package to simplify the retrieval of proxies for use in web scraping',
      url='https://github.com/mrcbrown1/proxysource',
      author='Mitchell Brown',
      author_email='mitch.rcb@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
