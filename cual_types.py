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

# Define Cual Artifact as a new semantic type
CualIDs = SemanticType('CualIDs')

class CualIDFile(model.TextFileFormat):
    def _validate_(self, level='min'):
        # TO DO: if needed
        pass

class CualFolder(model.SingleFileDirectoryFormat):
    cual_ids = model.TextFileFormat('ids.txt', format=CualIDFile)
    modified_ids = model.TextFileFormat(
            'modified_ids.txt', format=CualIDFile)

