import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scrapegoat", 
    version="0.0.1.10",
    author="Navaneeth",
    author_email="scrapegoat.python@gmail.com",
    description="Scrapegoat is a python library that can be used to scrape the websites from internet based on the\
                  relevance of the given topic irrespective of language using Natural Language Processing. It can be mainly\
                  used for non-English language to get accurate and relevant scraped text.",
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
      "GoogleNews==1.5.9",
      "googlesearch-python==1.0.1",        
      "googletrans==3.1.0a0",
      "scipy==1.7.1",
      "sent2vec==0.2.0",
      "beautifulsoup4==4.9.3",
      "numpy==1.21.1",
      "pandas==1.1.5",
   ],
)
