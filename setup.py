from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "Book-Recommendation-System"
AUTHOR_USER_NAME = "Priyanshu Dey"
SRC_REPO = "Book-Recommendation-System"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/PriyanshuDey23/Book-Recommendation-System",
    author_email="priyanshudey.ds@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS
)