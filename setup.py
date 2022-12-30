from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:list[str]=[]
    
# write a code to read requirement.txt file and append each requirements in requirement list variable
    # opening the file in read mode
    my_file = open("requirements.txt", "r")

# reading the file
    data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
    data_into_list = data.split("\n")
    requirement_list.append(data_into_list)
    my_file.close()

    return requirement_list




setup(   
    name="sensor",
    version="0.0.1",
    author="sachinbhavar", 
    author_email="bhavarsachin@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
 


