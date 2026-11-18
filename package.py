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
    "PyYAML",
    "scipy",
    "tqdm",
    "psutil",
    "alembic",
    "filelock",
    "requests",
    "PyOpenGL",
    "einops",
    "transformers",
    "tokenizers",
    "sentencepiece",
    "safetensors",
    "aiohttp",
    "yarl",
    "simpleeval",
    "blake3",
    "spandrel",
    "pydantic",
    "pydantic_settings",
    "av",  # Python binding for FFMpeg
    "kornia",
    "torch",
    "torchvision",
    "torchaudio",
    "torchsde",
    "comfyui_frontend_package-1.58.5",
    "comfyui_workflow_templates-0.11.110",
    "comfyui_embedded_docs-0.5.16",
    "comfy_aimdo-0.6.0",
    "comfy_kitchen-0.2.41",  # not available for Python 3.9
    "comfy_angle",
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
    env.PYTHONPATH.append('{root}')


build_command = 'rez python {root}/rez_build.py'
uuid = 'repository.ComfyUI'
