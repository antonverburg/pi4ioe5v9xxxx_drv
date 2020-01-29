import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pi4ioe5v9xxxx-antonverburg", # Replace with your own username
    version="0.0.2",
    author="Anton Verburg",
    author_email="info@tec-V.nl",
    description="Driver for pi4ioe5v0xxxx I2C IO expander chips",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antonverburg/pi4ioe5v9xxxx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3+",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
