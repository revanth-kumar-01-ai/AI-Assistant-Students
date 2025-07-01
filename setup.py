import setuptools

__version__ = "0.0.0"


REPO_NAME = "AI-Assistant-Students"
AUTHOR_USER_NAME = "revanth-kumar-01-ai"
SRC_REPO = "ai_student_assistant"
AUTHOR_EMAIL = "revanthk486@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= """
       AI assistant helps students study smarter with notes, doubts, solutions
    """,
    long_description="""
           AI Student Assistant is a smart helper 🤖 designed for school students to solve doubts, explain concepts, scan homework, generate notes, and give study support in a fun and easy way! ✨📘 It helps students learn faster, better, and smarter using the power of AI.
    """,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)