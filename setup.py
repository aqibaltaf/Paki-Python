
import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='yoda',                           # should match the package folder
    packages=['yoda'],                     # should match the package folder
    version='1.0.0',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='A Package full of helpful functions',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='Aqib Altaf',
    author_email='aqibaltaf99@gmail.com',
    url='https://github.com/aqibaltaf/Yoda-Python', 
    project_urls = {                                # Optional
        "Bug Tracker": "https://github.com/aqibaltaf/Yoda-Python/issues"
    },
    install_requires=['requests'],                  # list all packages that your package uses
    keywords=["pypi", "yoda", "tutorial"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/aqibaltaf/Yoda-Python/archive/refs/tags/v1.0.0.tar.gz",
)