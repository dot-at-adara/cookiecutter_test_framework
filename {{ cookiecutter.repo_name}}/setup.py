import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.readlines()

setuptools.setup(
    name='{{cookiecutter.repo_name}}',  # Replace with your own username
    version="0.0.4",
    author="DOT",
    author_email="dot@adara.com",
    description="{{cookiecutter.repo_name}} framework for simplified development",
    long_description="Sample",
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/dot-at-adara/{{cookiecutter.repo_name}}",
    setup_requires=['pytest-runner'],
    test_requires=requirements,
    packages=setuptools.find_namespace_packages(include=['{{cookiecutter.project_dir}}.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[

    ],

)