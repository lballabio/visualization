from setuptools import setup

setup(
    name="visualization",
    author="Luigi Ballabio",
    license=open("LICENSE.md").read(),
    packages=["visualization"],
    install_requires=["matplotlib", "numpy", "pandas"],
)
