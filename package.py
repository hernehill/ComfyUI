name = 'comfyui'

version = '0.45.5.hh.1.0.0'

authors = [
    'ComfyUI',
]

description = '''ComfyUI'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['HH_REZ_REPO_RELEASE_EXT']
    c.plugins.release_hook.hh_emailer.recipients = []

requires = [
    "numpy",
    "pillow",
]

private_build_requires = [
]

variants = [
    ["python-3.12"],
    ["python-3.13"]
]

def commands():
    env.REZ_COMFYUI_ROOT = '{root}'
    # env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/comfy')
    env.PYTHONPATH.append('{root}/comfy_api')
    env.PYTHONPATH.append('{root}/comfy_config')
    env.PYTHONPATH.append('{root}/comfy_api_nodes')
    env.PYTHONPATH.append('{root}/comfy_execution')
    env.PYTHONPATH.append('{root}/comfy_extras')


build_command = 'rez python {root}/rez_build.py'
uuid = 'repository.ComfyUI'
