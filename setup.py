from distutils.core import setup
setup(
  name = 'OneLiner', 
  packages = ['OneLiner'],
  version = '0.1',
  license='MIT',          
  description = 'Create Beautiful Java OneLiners here!',
  author = 'Derek Li',                   
  author_email = 'derekli2@illinois.edu',      
  url = 'https://github.com/derekli-NJ/OneLiner',   
  download_url = 'https://github.com/derekli-NJ/OneLiner/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Java', 'OneLiner', 'Python'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
