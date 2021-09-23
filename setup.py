from setuptools import find_packages, setup
# running the egg https://stackoverflow.com/a/37800297
setup(
    name="default",
    version="1.0",
    packages=find_packages(),
    entry_points={"scrapy": ["settings = default.settings"]},
)
