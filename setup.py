from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
  name = 'Topis-Harshit-102003644',        
  packages = ['Topsis-Harshit-102003644'],  
  version = '1.0',      
  license='MIT',        
  description = 'Library for Multiple Criteria Decision Making using Topsis', 
  long_description=long_description,
  long_description_content_type='text/markdown',  
  author = 'Harshit Gogia',                  
  author_email = 'hgogia_be20@thapar.edu',   
  url = 'https://github.com/hrshtgo/Topsis-102003644-Harshit',   
  download_url = 'https://github.com/hrshtgo/Topsis-Harshit-102003644/archive/refs/tags/1.0.tar.gz',    
  keywords = ['Topsis', 'MCDM'],  
  install_requires=[            
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',    
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',    
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
