from setuptools import setup


setup(name="toadata",
      version="0.1",
      description="generate markdown from mediainfo, ffmpeg and others",
      url='http://github.com/liuyang1/toadata',
      author='liuyang1',
      license='MIT',
      packages=['toadata'],
      scripts=['scripts/mdtoadata', 'scripts/toadata'],
      zip_safe=False)
