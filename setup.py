from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements1=file_obj.readlines()
        requirements1=[req.replace("\n","") for req in requirements1]

        if HYPEN_E_DOT in requirements1:
            requirements1.remove(HYPEN_E_DOT)
    
    return requirements1

setup(
name='mlproject',
version='0.0.1',
author='Suraj',
author_email='surajrahinj.sr@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)