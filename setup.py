from setuptools import setup

setup(
      name = "Arithmetic"
    , version = "0.0.0.1"
    , description = "A collection of modules for performing simple arithmetic computations."
    , author = "Njagi Mwaniki"
    , author_email= "njagi@urbanslug.com"
    , package_dir={"": "arithmetic"}
    , packages=["division", "multiplication"]
    , test_suite="arithmetic.tests"
)
