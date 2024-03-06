from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """This function returns a list of requirements

    Args:
        file_path (str): file path

    Returns:
        List[str]: List of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements


setup(
    name='Student_Performance_Indicator',
    version='1.0.0',
    author='Ashwani-Chaurasiya',
    author_email='ashwanic661@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    url='https://github.com/Ashwani-Chaurasiya/ETE-ML-Project-Student-Performance-Indicator/',
    description='This is a Python package for the student performance indicator.',
)
