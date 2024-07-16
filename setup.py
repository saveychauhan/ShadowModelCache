from setuptools import setup, find_packages

setup(
    name='shadowmodelcache',
    version='0.1.0',
    description='High-performance django model cache library.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/saveychauhan/ShadowModelCache',
    author='Sawan Chauhan',
    author_email='sav.ey@live.co.uk',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Django'
    ],
    packages=find_packages(),
    install_requires=[
        'django>=3.2',
        'django-redis'
    ],
    python_requires='>=3.6',
)
