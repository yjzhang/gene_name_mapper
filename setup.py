from setuptools import setup, find_packages
import numpy




install_requires = [
]

setup(
    name='gene_name_mapper',
    version='0.0.1',
    author='Yue Zhang',
    author_email='yjzhang@cs.washington.edu',
    url='https://github.com/yjzhang/gene_name_mapper',
    license='MIT',
    install_requires=install_requires,
    packages=find_packages("."),
    test_suite='nose.collector',
    tests_require=['nose', 'flaky'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],

)
