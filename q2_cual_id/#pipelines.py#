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

def cual_handler( output_path: str, number_of_ids: int, 
        length_of_ids: int, distance_between_ids: int,
        failure_threshold: int, existing_ids: CualArtifact
        metadata: qiime2.Metadata )->CualArtifact:
    if(#no IDs given):
        # generate IDs if none provided
        create_ids(
            n, 
            id_length, 
            min_distance, 
            failure_threshold=0.99,
            existing_ids=None
            )
    elif(#IDs are given):
        # Import the provided IDs
        create_ids(
            n,
            id_length,
            min_distance,
            failure_threshold=0.99,
            existing_ids=input_ids
            )
    else:
        # return error message

    # Check the IDs
      # determine the correct input and input to check var spaces
    fix_ids(correct_input, input_to_check, threshold=0.5)

    # If flag for barcodes is provided
    if(barcode_flag):
        generate_barcodes()

    return CualArtifact
