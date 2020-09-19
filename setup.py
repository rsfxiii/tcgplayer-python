from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(
        name='tcgplayer-python',
        description='Python 3 library for accessing TCGPlayer APIs',
        version='0.8',
        author='rsfxiii',
        author_email='ryan@raijinn.xyz',
        url='https://github.com/rsfxiii/tcgplayer-python',
        license='GNU General Public License v3',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',

            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Games/Entertainment',
        ],
        namespace_packages=['tcgplayer'],
        packages=find_packages(include=['tcgplayer', 'tcgplayer.*']),
        install_requires=[
            'requests',
            'python-dotenv',
            'coverage'
        ],
        python_requires='>=3.7',
    )
