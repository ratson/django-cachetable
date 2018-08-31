import setuptools

setuptools.setup(
    name="django-cachetable",
    version="0.0.2",
    url="https://github.com/ratson/django-cachetable",

    author="Ratson",
    author_email="contact@ratson.name",

    description="Use Django admin to view cachetable",
    long_description=open('README.rst').read(),
    keywords=[],

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
