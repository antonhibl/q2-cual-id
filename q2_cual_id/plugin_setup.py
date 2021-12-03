# ----------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed w/ this software.
# ----------------------------------------------------------------------

# Imports and Dependencies
import importlib
from cual_types import CualID, CualArtifact
from qiime2.plugin import Plugin, Str, Choices, Properties, Metadata
import q2_cual_id
import q2_cual_id.actions
import q2_cual_id.pipelines
import q2_cual_id.plugin_setup

# Register the plugin
plugin = Plugin("cual-id",
                version="0.0.1.dev",
                website="https://github.com/antonhibl/q2-cual-id")

importlib.import_module("cualid")

# Registering formats for directory structure, and short/long file formats
plugin.register_formats(CualFolder, CualIDFile)

#plugin.register_semantic_types(IDs, WideIDs)

# ID Generation Function
plugin.methods.register_function(
        function=q2_cual_id.actions.generate_id,
        inputs={'existing_ids': CualArtifact},
        parameters={'n': NumberOfIDs,
                    'id_length': IDlength,
                    'min_distance': minimumDistance,
                    'failure_threshold': failureThreshold,
                    },
        outputs=[('cual_ids', CualIDs)],
        input_descriptions={'existing_ids': ''},
        parameter_descriptions={
                'n': '',
                'id_length': '',
                'min_distance': '',
                'failure_threshold': ''
            },
        output_descriptions={'cual_ids': ''},
        name='Cual ID Generator',
        description=("Generates a set of Cual IDs for use in"
                     "bio-informatics and computing research.")
        )

# Cual Cleaning Function
plugin.methods.register_function(
        function=q2_cual_id.actions.check_ids,
        inputs={
            # existing ID artifact
        },
        parameters={
            # The data to check against
              # not sure how this is implemented but I think
              # I can attach metadata that tracks this within the
              # artifact somehow
        },
        outputs=[(
            # Fixed ID Artifact
              # structurally the exact same as the input,
              # just fixed errors
        )],
        input_descriptions={
            # the input artifact with IDs should be described here
              # as well as any details about metadata the user may
              # need to know
        },
        parameter_descriptions={
            # Describe the data being cross-checked and how
            # this transfers into the function from the input
            # if necessary
        },
        output_descriptions={
            # describe the returned fixed IDs, emphasize the
            # way the structure is unchanging only the data is
            # being munged
        },
        name='Cual ID Cleaner',
        description=("Checks and fixes a given set of Cual IDs,"
                     "then returns this fixed set to the user.")
        )

# Barcode Generation Function
plugin.visualizers.register_function(
        function=q2_cual_id.actions.generate_barcodes,
        inputs={
            # existing ID Artifact
        },
        parameters={
            # visual appeal affects like title inclusing and ID sub-headers
        },
        outputs=[(
            # new barcode visualization
        )],
        input_descriptions={
            # description for the input existing IDs, generated seperately
        },
        parameter_descriptions={
            # short description of ways the other parameters can affect the output visual
        },
        name='Cual ID Bar Encoder',
        description=("Creates a set of barcodes given an error-free"
                     "set of Cual IDs, returns this as a visualizer"
                     "to the user.")
        )

# Cual Transformer Function
plugin.methods.register_function(
        function=q2_cual_id.actions.cual_transform,
        inputs={
            #existing IDS here
        },
        parameters={
            #length of transformed IDS
        },
        outputs=[(
            # newly parsed IDs
        )],
        input_descriptions={
            # input shorter IDs
        },
        parameter_descriptions={
            # decribe how length parameter takes action
        },
        output_descriptions={
            # short description describing how transform affects the IDs
        },
        name='Cual ID Parser',
        description=("Parses longer globally unique IDs into their"
                     "shortened Cual IDs.")
        )

