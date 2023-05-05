from setuptools import find_packages, setup
from typing import List

requirements = []
hyphen_e_dot = "-e ."
def get_requirements(file_path:str) -> List[str]:

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
    name = 'mlproject',
    author = 'rabi3333',
    author_email = 'ghenirabee@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)