from setuptools import setup, find_packages
from typing import List

HYFEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n", "") for req in requirements]

        if HYFEN_E_DOT in requirements:
            requirements.remove(HYFEN_E_DOT)

    return requirements


setup(
    name="project",
    version="0.01",
    author="Ibrahim Khaleel",
    author_email="ik09012006@gmial.com",
    packages=find_packages(),
    requures=get_requirements("requirements.txt"),
)
