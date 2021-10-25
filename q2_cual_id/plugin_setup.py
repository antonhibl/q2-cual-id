
# -------------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# -------------------------------------------------------------------------
import importlib

# Import Types
import qiime2.plugin
from q2_types.#TO-DO

from ._visualizer import bar_encoder

import q2_cual_id
from q2_cual_id import #TO-DO

from qiime2.plugin import Metadata

plugin = qiime2.plugin.Plugin(
    name='cual-id',
    version=q2_cual_id.__version__,
    website=#TO-DO,
    package='q2_cual_id',
    description=('This QIIME 2 plugin helps create and manage sample
                  identifiers in comparative -omics studies.'),
    short_description=('Plugin for globally unique sample identifier 
                        generation/management.'),
    citations=qiime2.plugin.Citations.load('citations.bib', 
                                               package='q2_cual_id')
)

# Function Registration

# Visualizer
plugin.visualizers.register_function(
    function=barcodeGenerator,
    inputs={'TO-DO': #TO-DO},
    parameters={'TO-DO' : #TO-DO},
    input_descriptions={'TO-DO': ('TO-DO')},
    parameter_descriptions={'TO-DO': "TO-DO"},
    name='UUID barcode generator',
    description=(
        'Prepares a barcode that represents a UUID which can be used in'
        'field research to label and keep track of sample identifiers.')
)



plugin.register_formats(DADA2StatsFormat, DADA2StatsDirFmt)
plugin.register_semantic_types(DADA2Stats)
plugin.register_semantic_type_to_format(
    SampleData[DADA2Stats], DADA2StatsDirFmt)
importlib.import_module('q2_dada2._transformer')

# Types Registration
plugin.register_formats(#TO-DO)
plugin.register_semantic_types(#TO-DO)
plugin.register_semantic_type_to_format(#TO-DO)
importlib.import_module(#TO-DO)
