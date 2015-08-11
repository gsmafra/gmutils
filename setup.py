from setuptools import setup, find_packages

setup(
    name='gmutils',
    version='0.1.1',
    author='Gustavo Sena Mafra',
    author_email='gsenamafra@gmail.com',
    description='Utils',
    license='MIT',
    packages=find_packages(),
    url='https://github.com/gsmafra/gmutils',
    install_requires=['numpy'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Machine Learning',
        ]
    )
