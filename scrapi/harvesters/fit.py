"""
A harvester for Florida Institute of Technology for the SHARE project

An exaple API call: http://repository.lib.fit.edu/oai/request?verb=ListRecords
"""

from __future__ import unicode_literals

from scrapi.base import OAIHarvester


class FIT_Harvester(OAIHarvester):
    short_name = 'fit'
    long_name = "Florida Institute of Technology"
    url = "http://repository.lib.fit.edu"

    base_url = "http://repository.lib.fit.edu/oai/request"

    approved_sets = [
        u'com_11141_1', 'com_11141_2', 'com_11141_3', 'com_11141_8',
        'com_11141_12', 'com_11141_13', 'com_11141_14', 'com_11141_15', 'com_11141_16',
        'com_11141_17', 'com_11141_18', 'com_11141_19', 'com_11141_20', 'com_11141_21',
        'com_11141_22', 'com_11141_31', 'com_11141_32', 'com_11141_33', 'com_11141_38',
        'com_11141_39', 'com_11141_40', 'com_11141_41', 'com_11141_42', 'com_11141_50',
        'com_11141_245', 'com_11141_248', 'col_11141_4', 'col_11141_11', 'col_11141_23',
        'col_11141_24', 'col_11141_25', 'col_11141_26', 'col_11141_27', 'col_11141_28',
        'col_11141_29', 'col_11141_30', 'col_11141_34', 'col_11141_35', 'col_11141_36',
        'col_11141_43', 'col_11141_44', 'col_11141_45', 'col_11141_46', 'col_11141_47',
        'col_11141_48', 'col_11141_51', 'col_11141_52', 'col_11141_74', 'col_11141_211',
        'col_11141_212', 'col_11141_213', 'col_11141_214', 'col_11141_215', 'col_11141_216',
        'col_11141_217', 'col_11141_218', 'col_11141_219', 'col_11141_220', 'col_11141_221',
        'col_11141_222', 'col_11141_223', 'col_11141_224', 'col_11141_225', 'col_11141_226',
        'col_11141_227', 'col_11141_228', 'col_11141_229', 'col_11141_246', 'col_11141_247',
        'col_11141_249', 'col_11141_257', 'col_11141_561', 'col_11141_572', 'col_11141_573',
        'col_11141_574', 'col_11141_575', 'col_11141_576', 'col_11141_577', 'col_11141_578',
        'col_11141_579', 'col_11141_580', 'col_11141_693', 'col_11141_696', 'col_11141_697',
        'col_11141_698', 'col_11141_699']

    timezone_granularity = True
