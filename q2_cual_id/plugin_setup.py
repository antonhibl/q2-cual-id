# ----------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed w/ this software.
# ----------------------------------------------------------------------

from cual_types import CualID, CualArtifact

from qiime2.plugin import Str, Choices, Properties, Metadata

import q2_cual_id
import q2_cual_id.actions
import q2_cual_id.pipelines
import q2_cual_id.plugin_setup

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

plugin.methods.register_function(
        function=q2_cual_id.actions.check_ids,
        inputs={},
        parameters={},
        outputs=[()],
        input_descriptions={},
        parameter_descriptions={},
        output_descriptions={},
        name='Cual ID Cleaner',
        description=("Checks and fixes a given set of Cual IDs,"
                     "then returns this fixed set to the user.")
        )

plugin.methods.register_function(
        function=q2_cual_id.actions.generate_barcodes,
        inputs={},
        parameters={},
        outputs=[()],
        input_descriptions={},
        parameter_descriptions={},
        output_descriptions={},
        name='Cual ID Bar Encoder',
        description=("Creates a set of barcodes given an error-free"
                     "set of Cual IDs, returns this as a visualizer"
                     "to the user.")
        )

plugin.methods.register_function(
        function=q2_cual_id.actions.cual_transform,
        inputs={},
        parameters={},
        outputs=[()],
        input_descriptions={},
        parameter_descriptions={},
        output_descriptions={},
        name='Cual ID Parser',
        description=("Parses longer globally unique IDs into their"
                     "shortened Cual IDs.")
        )
