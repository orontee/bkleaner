from distutils.core import setup

setup(name='bkleaner',
      version='0.1',
      description='Cleanup EPUB files',
      author='Matthias Meulien',
      author_email='orontee@gmail.com',
      url='https://gitorious.org/bkleaner',
      packages=['bkleaner'],
      scripts=['scripts/bkleaner'],
      platforms=['linux2'],
      license='GNU General Public License')
