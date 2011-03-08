from setuptools import setup, find_packages

setup(name="django-db-locale",
    version="0.1",
    description="Django application to translate strings in database.",
    author="Vladyslav Frolov",
    packages=find_packages(),
    package_data={'db_locale': ['templates/db_locale/*.html']}
    include_package_data=True,
)
