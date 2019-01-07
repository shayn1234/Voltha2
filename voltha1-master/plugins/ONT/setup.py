from setuptools import setup

# Replace the place holders with values for your project

setup(

    # Do not use underscores in the plugin name.
    name='ONT',

    version='0.1',
    author='ENTER-AUTHOR-HERE',
    author_email='ENTER-AUTHOR-EMAIL-HERE',
    description='ENTER-DESCRIPTION-HERE',

    # This must correspond to the actual packages in the plugin.
    packages=['ONT'],
    zip_safe=False,
    install_requires=[
        # Necessary dependency for developing plugins, do not remove!
        "cloudify-plugins-common>=4.2"
    ]
)

