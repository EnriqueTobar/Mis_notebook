from setuptools import setup

setup(
	name = "paquete",
	version = "0.1",
	description = "Este es un paquete de ejemplo",
	author = "Enrique Tobar",
	author_email = "yo@dale.info",
	url = "http://hcosta.info",
	scripts=[],
	packages=["paquete", "paquete.adios", "paquete.hola"]
)