# ----------------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

import versioneer


setup(
    name="q2-cual-id",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url="https://qiime2.org",
    license="BSD-3-Clause",
    packages=find_packages(),
    author="John Chase and Evan Bolyen",
    author_email="ebolyen@gmail.com",
    description="Create and manage sample identifiers in comparative -omics datasets.",
    package_data={
        'q2_cual_id': ['citations.bib'],
    },
    entry_points={
        "qiime2.plugins":
        ["q2-cual-id=q2_cual_id.plugin_setup:plugin"]
    },
    zip_safe=False,
