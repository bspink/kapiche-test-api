import os
from setuptools import setup, find_packages


base_dir = os.path.dirname(__file__)

with open(os.path.join(base_dir, 'VERSION')) as f:
    version = f.read().strip()

with open(os.path.join(base_dir, 'requirements.txt')) as f:
    requires = f.read().splitlines()


setup(
    name='kapiche_api',
    version=version,
    description='NPS test app for Kapiche',
    long_description='NPS test app for Kapiche',
    license='Proprietary',
    url='https://github.com/bspink/kapiche-test-api',
    author='bspink',
    author_email='bradley.spink@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Programming Language :: Python',
    ],
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,  # Requires a MANIFEST.in
    install_requires=requires,
    extras_require={
        "test": ['pytest'],
    },
    python_requires='>=3.7',
)
