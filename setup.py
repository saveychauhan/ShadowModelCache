
from setuptools import setup, find_packages

setup(
    name='shadowmodelcache',
    version='0.1.0',
    description='ShadowModelCache is a high-performance library designed to create and manage cached copies of models, ensuring fast data retrieval and reduced load on primary data sources. It features automatic cache invalidation, various eviction policies, and supports distributed caching for scalable solutions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your_project',
    author='Your Name',
    author_email='your.email@example.com',
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
    ],
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    python_requires='>=3.6',
)