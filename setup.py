import setuptools

setuptools.setup(
    name="jupyter-openrefine-proxy",
    version='1.0dev',
    url="https://github.com/evanlinde/jupyter-openrefine-proxy",
    author="Evan Linde",
    description="Jupyter extension to proxy OpenRefine",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'openrefine = jupyter_openrefine_proxy:setup_openrefine',
        ]
    },
    package_data={
        'jupyter_openrefine_proxy': ['icons/openrefine.svg'],
    },
)
