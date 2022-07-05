import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scrapegoat", 
    version="1.0.0.3",
    author="Navaneeth",
    author_email="scrapegoat.python@gmail.com",
    description="Scrape data with ease",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Scrape-Goat/scrapegoat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
   install_requires=[
      "GoogleNews>=1.5.9",
      "googletrans>=3.1.0a0",
      "scipy>=1.7.1",
      "beautifulsoup4>=4.9.3",
      "numpy>=1.21.1",
      "pandas>=1.1.5",
      "Wikipedia-API>=0.5.4",
      "sentence_transformers",
      "googlesearch-python"
   ],
)
