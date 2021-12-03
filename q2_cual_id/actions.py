# ----------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed w/ this software.
# ----------------------------------------------------------------------

from q2_cual_id.plugin_setup import plugin
import cualid
from cualid.label import get_barcodes
from cualid.mint import create_ids
from cualid.fix import fix_ids, format_output,
from cualtypes import CualArtifact

# this actually transformed the ID file which was initially generated
# into the usable CualFolder Artifact
def cual_transform(CualIDFile)->CualFolder:
    # Initialize local variables
    # parse the ID file into shortend "modified" ID file
    # package original length IDs and new modified IDs into a Folder
    # Return the new folder as the CualFolder Artifact
    return CualFolder

# because this returns only a CualIDFile, I will need to handle
# the calling of this function within some cual_transform() which
# then generates a CualFolder that then stores this file alongside
# any other metadata
def generate_ids(
        NumbOfIDs,
        LenOfIDs
        DistBetween,
        Threshold
        )->CualIDFile:
    # utilize create ids command
    new_ids = create_ids(NumbOfIDs, LenOfIDS, DistBetween, Threshold)
    
    # parse output into a qiime artifact
    for identifier in new_ids:
        # do something with the id to put in artifact here
    # return qiime artifact
    return CualIDFile

# This returns a visualizer, my thinking is to use this function
# outside any pipeline, this is because the visualizer will not
# actually be stored in the CualFolder which is our artifact, this
# will store it as a seperate file.
def generate_barcodes(
        input_ids,
        output_fp,
        suppression_flag)->CualVisualizer:
    # initialize local variables 
    # store barcodes output
    barcodes = get_barcodes(input,
                 output_fp,
                 suppress_ids,
                 barcode_type = '128',
                 columns = 4,
                 rows = 9,
                 x_start = 1.9,
                 y_start = 257.2)
    # store the barcodes in a returnable visualizer object
    # Return the visualizer artifact
    return CualVisualizer

# Thinking it is best to pass in a whole CualFolder which can have
# attached, any important data( the data to cross-check ) as metadata.
# It then can return a Folder back and just edit the cualFile inside
# if errors are discovered in its cross-reference.
def check_ids(
        CualFolder
        )->CualFolder:
    # initialize local variables and data, possible flags
    # extract id data from the provided artifact
    # use the fix_ids command to manage the id metadata from an artifact
    fix_ids(correct_input, input_to_check, thresh=0.5)
    # re-parse the fixed ID metadata into the artifact
    # return the re-generated artifact
    return CualIDFile
