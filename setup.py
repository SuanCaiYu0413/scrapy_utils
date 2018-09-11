# @Time    : 2018/9/11 下午5:08
# @Author  : SuanCaiYu
# @File    : setup
# @Software: PyCharm
from pkgutil import walk_packages
from setuptools import setup


def find_packages(path):
    # This method returns packages and subpackages as well.
    return [name for _, name, is_pkg in walk_packages([path]) if is_pkg]


setup(name='scrapy-utils',
      version='0.0.1',
      description='a scrapy public utils project',
      author='SuanCaiYu0413',
      author_email='suancaiyu0413@gmail.com',
      url='https://github.com/SuanCaiYu0413/scrapy_utils',
      package_dir={'': 'src'},
      packages=list(find_packages('src')),
      license='MIT',
      keywords='scrapy-utils')
