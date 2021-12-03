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
from cualid.fix import fix_ids, format_output
from cualtypes import CualArtifact

# need to rework some of the code details, this should take in an
# artifact, handle the cleaning & possibly the barcode generation,
# I am not convinced this needs to be a pipeline
def cual_handler( output_path: str,
                  existing_ids: CualFolder,
                  barcode_flag:bool
        )->CualFolder:
    # Check the IDs
      # determine the correct input and input to check var spaces
    fix_ids(correct_input, input_to_check, threshold=0.5)

    # If flag for barcodes is provided
    if(barcode_flag):
        # need to update the params in here
        generate_barcodes()

    return CualFolder

# this can handle quick and easy ID Generator
def cual_gen_pl(
        n,
        IDlength,
        # few more params to add
)->CualFolder:
    # Initialize local variables
    # call to generate_ids()
    # call to cual_transform(),
    # this ensures proper structure & both ID variants being
    # included in the final artifact
    # return the artifact
    return CualFolder
