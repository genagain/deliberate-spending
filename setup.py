import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="deliberate_spending",
    version="1.0.0",
    url="",
    license="BSD",
    maintainer="Gen Ohta",
    maintainer_email="myself@genohta.com",
    description="Budgeting application",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest", "coverage", "blinker"]},
)
