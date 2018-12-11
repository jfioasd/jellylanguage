from distutils.core import setup

setup(
	name = 'jellylanguage',
	version = '0.1.29',
	packages = [
		'jelly'
	],
	scripts = [
		'scripts/jelly'
	],
	install_requires = [
		'sympy'
	]
)
