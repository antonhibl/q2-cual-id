# ------------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ------------------------------------------------------------------------

from setuptools import setup, find_packages

import versioneer

setup(
    name="q2-cual-id",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    author="Anton Hibl",
    author_email="antonhibl11@gmail.com",
    description="Global 'Cual' ID toolkit plugin for QIIME2.",
    license='BSD-3-Clause',
    url="https://qiime2.org",
    entry_points={
        'qiime2.plugins':
        ['q2-cual-id=q2_cual_id.plugin_setup:plugin']
    },
    package_data={
        'q2_cual_id': [
            'citations.bib',
        ]
    },
    zip_safe=False,
)
