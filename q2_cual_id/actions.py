# ----------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed w/ this software.
# ----------------------------------------------------------------------

import cualid
from cualid.label import get_barcodes
from cualid.mint import create_ids
from cualid.fix import fix_ids, format_output,
from cualtypes import CualArtifact

def cual_transform()->CualFolder:
    # Initialize local variables
    # parse the ID file into shortend "modified" ID file
    # package original length IDs and new modified IDs into a Folder
    # Return the new folder as the CualFolder Artifact
    return CualFolder

def generate_ids(
        
        )->CualIDFile:
    # initialize local variables and data
    # utilize create ids command
    ids = create_ids(n, id_length, min_distance, failure_thres);
    # parse output into a qiime artifact
    # return qiime artifact
    return CualIDFile

def generate_barcodes()->CualVisualizer:
    # initialize local variables
    # utilize get barcodes command
    # create a visualizer that allows for storing & viewing of the barcodes
    # Return the visualizer artifact
    return CualVisualizer

def check_ids(
        CualArtifact
        )->CualIDFile:
    # initialize local variables and data, possible flags
    # extract id data from the provided artifact
    # use the fix_ids command to manage the id metadata from an artifact
    # re-parse the fixed ID metadata into the artifact
    # return the re-generated artifact
    return CualIDFile
