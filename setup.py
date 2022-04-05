from setuptools import setup

if __name__ == '__main__':

    # Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
    setup(
        name="Amarela",
        install_requires=[
            "pandas >= 1.3.3",
            "importlib-metadata >= 3.6.0; python_version < '3.10'",
        ],
        extras_require={
            "dotenv": ["python-dotenv"],
        },
    )