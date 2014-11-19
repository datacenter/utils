from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "vmController",
    version = "0.1.0",
    scripts = ['README.md'
               ],

    # The project's main homepage
    # url='https://github.com/datacenter/ACI/tree/master/configuration-python',

    packages = ["vmController"],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['paramiko>=1.15.1', 'vmfusion>=0.2.0', 'argparse>=1.1', 'scp>=0.8.0'],

    # metadata for upload to PyPI
    author = "Bon Huang",
    author_email = "bonhuan@cisco.com",
    description = "Control VMware Fusion",
    long_description = read('README.md'),
    license = "Cisco",
    # keywords = "Create MO in Cisco APIC",

    # could also include long_description, download_url, classifiers, etc.
)