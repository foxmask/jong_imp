from setuptools import setup, find_packages
from jong_imp import __version__ as version

setup(
    name='jong_imp',
    version=version,
    description='JOplin Notes Generator Importer',
    long_description=open('README.md').read(),
    author='FoxMaSk',
    maintainer='FoxMaSk',
    author_email='foxmaskhome@gmail.com',
    maintainer_email='foxmaskhome@gmail.com',
    url='https://github.com/foxmask/jong_imp',
    download_url="https://github.com/foxmask/jong/archive/jong-imp-" + version + ".zip",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True
)
