from setuptools import setup, find_packages

setup(name="django-db-locale",
    version="0.1",
    description="Django application to translate strings in database.",
    author="Vladyslav Frolov",
    packages=find_packages(),
    include_package_data=True,
)
