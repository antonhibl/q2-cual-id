# ----------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed w/ this software.
# ----------------------------------------------------------------------

# Import Dependencies
import os

import qiime2.plugin.model as model
from qiime2.plugin import SemanticType

# Define Cual IDs as a new semantic type to hopefully store
# the ID data in the file format I established
CualIDs = SemanticType('CualIDs')

# already defines as a format in plugin_setup.py
# not sure if this class is necessary but it should
# set up a self-validating text file format
class CualIDFile(model.TextFileFormat):
    def _validate_(self, level='min'):
        # TO DO: if needed
        pass

# defining a folder format to hold the cual file and log/metadata
# also already defined a CualFolder in plugin_setup.py so unsure
# if this is necessary
class CualFolder(model.SingleFileDirectoryFormat):
    cual_ids = model.TextFileFormat('ids.txt', format=CualIDFile)
    modified_ids = model.TextFileFormat(
            'modified_ids.txt', format=CualIDFile)

