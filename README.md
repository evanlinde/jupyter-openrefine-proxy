# jupyter-openrefine-proxy

**jupyter-openrefine-proxy** provides Jupyter server and notebook extensions to proxy [OpenRefine](https://openrefine.org/).

If you have a JupyterHub deployment, jupyter-openrefine-proxy can take advantage of JupyterHub's existing authenticator and spawner to launch OpenRefine in users' Jupyter environments. You can also run this from within Jupyter.

This is a convenience package built from the template in [jupyter-server-proxy](https://github.com/jupyterhub/jupyter-server-proxy) with some additional features and readme text copied/modeled after [jupyter-rsession-proxy](https://github.com/jupyterhub/jupyter-rsession-proxy).


## Installation

### Pre-reqs

#### Install OpenRefine

Download the package appropriate for your system from the OpenRefine project's [download page](https://openrefine.org/download.html) and follow the corresponding [installation instructions](https://github.com/OpenRefine/OpenRefine/wiki/Installation-Instructions).

Add the OpenRefine install location to the PATH variable or one of the additional paths (explained below)

OR

Create a symbolic link to the OpenRefine executable somewhere in your existing PATH:
```bash
ln -s /path/to/refine /usr/bin/refine
```

jupyter-openrefine-proxy will search for the OpenRefine executable `refine` using the PATH environment variable. It will also check in `/opt/openrefine` and `~/openrefine` if it does not find anything in PATH.


### Install jupyter-openrefine-proxy

Install the library:
```
pip install git+https://github.com/evanlinde/jupyter-openrefine-proxy
```


### Multiuser Considerations

This extension launches an OpenRefine process from the jupyter notebook server. This is fine in JupyterHub deployments where user servers are containerized since other users cannot connect to the OpenRefine port. In non-containerized JupyterHub deployments, for example on multiuser systems running LocalSpawner or BatchSpawner, this not secure. Any user may connect to OpenRefine and run arbitrary code.

