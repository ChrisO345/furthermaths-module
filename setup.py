from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("readme.md") as f:
    readme = f.read()

extras_require = {}

packages = [
    "furthermaths",
    "furthermaths.series",
    "furthermaths.complex",
    "furthermaths.matrices",
    "furthermaths.vectors",
]

setup(
    name='furthermaths',
    url="",
    version="0.1.1",
    packages=packages,
    license='MIT',
    description='An extension to the pre-installed and packaged python default maths library',
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires='>=3.10.0',
    classifiers=[
        'Programming Language :: Python :: 3.10'
    ]
)
