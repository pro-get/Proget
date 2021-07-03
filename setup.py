from setuptools import setup

with open("README.md", "r") as file:
   long_description = file.read()

setup(
	name='Proget',
	version='1.0b4',    
	description='''A software installation tool''',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/Whirlpool-Programmer/Proget',
	author='Whirlpool-Programmer',
	author_email='whirlpool.programmer@outlook.com',
	license='MIT License',
	packages=['proget'],
	requires=['pyyaml','urllib','requests','platform'],
	classifiers =[
	'Programming Language :: Python :: 3',
	'License :: OSI Approved :: MIT License',
	'Operating System :: OS Independent'
	],
	 entry_points = {
		"console_scripts": [
			"proget = proget:main",
		]
	}
	
)

'''
BUILD COMMANDS
python setup.py sdist
python setup.py bdist_wheel --universal
python -m twine upload dist/*.*
'''