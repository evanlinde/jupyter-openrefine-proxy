"""
Return config on servers to start for openrefine

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil

def get_executable(prog):
    # Locations to check even if they're not in the PATH
    other_paths = [
        os.path.join('/opt/openrefine', prog),
        os.path.join('~/openrefine', prog),
    ]
    # Use executable from PATH if found
    if shutil.which(prog):
        return prog
    # Otherwise use first result from other_paths
    for op in other_paths:
        if os.path.exists(op):
            return op

    raise FileNotFoundError(f'Could not find {prog} in PATH')

def setup_openrefine():
    def _get_cmd(port):
        return [
            get_executable('refine'),
            '-p', 
            str(port)
        ]

    return {
        'command': _get_cmd,
        'timeout': 15,
        'environment': {},
        'request_headers_override': {
            'Host': '127.0.0.1'
        }
        'launcher_entry': {
            'title': 'OpenRefine',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'openrefine.svg')
        }
    }
