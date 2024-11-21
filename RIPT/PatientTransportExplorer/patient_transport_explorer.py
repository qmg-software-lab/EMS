import os
import sys
import logging
import sqlite3
import pathlib
import logging
import pyfiglet
import pandas as pd
from colorama import Fore
from sqlite3 import connect
from fileinput import filename
from datetime import datetime, timedelta
from tabnanny import filename_only
from datetime import datetime
from datetime import time
import pandas as pd
import warnings
# import lamda
# import watson
# import python-dotenv
# import lymbic




# configure logging
log_file_name = __file__.split('/')[-1].split('.')[0]
project_root = os.path.dirname(os.path.abspath(__file__))
log_file_path = project_root + '/logs/' + log_file_name + '.log'
file_handler = logging.FileHandler(filename=log_file_path)
stdout_handler = logging.StreamHandler(stream=sys.stdout)
handlers = [file_handler, stdout_handler]
logging.basicConfig(handlers=handlers, level=logging.INFO)
logger = logging.getLogger(log_file_name + '-logger')
time_mtn = datetime.now()
warnings.simplefilter(action='ignore', category=FutureWarning)
line_0 = ' '
line_1 = ' WELCOME to the explorer module for '
line_2 = pyfiglet.figlet_format(' Routine Interfacility Patient Transport')
print(Fore.CYAN + line_0); print(); print(line_1); print(Fore.CYAN + line_2)
print('\n-------------------------------------------------------------------------------------------------------------')
logging.info('\n\n ( WELCOME to Routine Interfacility Patient Transport - RIPT Data Explorer')
print('---------------------------------------------------------------------------------------------------------------')
logger.info(' \n\n Module start time: {}'.format(time_mtn))
file_path = os.path.dirname(os.path.abspath(__file__))
print('---------------------------------------------------------------------------------------------------------------')
logger.info(' logger file path =\n{}'.format(file_path))


# ToDo Step 0: # write an app to dynamically gen a dataflow diagram for team collaboration
def dataflow_pathway_output_as_diagram():
    dataflow_dict = {}
    # while True:
    #     if 1=1:
    #         dev_tools == True
    return dataflow_dict


# ToDo Step 1: Hospital EMR has patient information in the system
def emr_get_record():
    pat_record_id_dict = {}
    qry_pat_details = pd.read_sql() 'qry_get_patient_details')

    result = pd.read_sql_query(pat_record_id, pat_record_id_emr_dict)

    conn = connect(':memory:')
    df = pd.DataFrame(data=[[0, '10/ 11/ 12'], [1, '12/ 11/ 10']],
    columns = ['int_column', 'date_column'])
    df.to_sql(name='test_data', con=conn)


    if pat_record_id:
        pass
    else:
        raise Exception as e_pat_record_missing (' No patient record id found')

    return pat_record_id_dict









# #
# # # ToDo Step 2. Physician clears patient for discharge
# # def hospital_ddx_dispo_cleared():
# #     physician_clears_patient_for_discharge_ack = """"
# #
# #     """
# #
# #     qry_get_patient_details
# #     result = pd.to_sql(
# #         """
# #     pat_emergency_ddx = my_scrapingFunction(scrape_epic(
# #     pat_inpatient_ddx = hospital_svc.ddx
# #     pat_acutecare_ddx
# #     """
# #     return pat_emergency_ddx, pat_inpatient_ddx, pat_acutecare_ddx
# #
# #
# # # ToDo Step 3. Transport provider contacted and minimum required patient data is exchanged
# # def transporting_agency_contact_affirmation():
# #
# #     def patient_transport_risk_mitigator():
# #         # pd.api('get' )
# #         risk_score = 532
# #
# #         # where transport_completion_likelihood >= .90
# #         #   and risk_of_tansporting_patient < 100
# #         #   and risk_of_not_tranporting > 100
# #
# #
# #
# #
# #         if risk_score > 500:
# #             patient_transport_risk_assessment_order_level = 5
# #             risk_score = patient_transport_risk_assessment_order_level * ('some numbers here')
# #
# #         return patient_transport_risk_assessment_order
# #
# #
# #     minimum_pat_details = [
# #           'name'
# #         , 'gender'
# #         , 'date of birth'
# #         , 'MRN'
# #     ]
# #     minimum_provider_details = [
# #           'transporting_provider_name'
# #         , 'transporting_provider_dispatch_active_transaction_code'
# #         , 'transporting_provider_request_acknowledgement'
# #     ]
# #
# #
# #
# #     qry_get_patient_details = """
# #         select
# #               d.first_name as patient_first_name
# #             , d.last_name as patient_last_name
# #             , d.gender as patient_gender
# #             , d.date_of_birth as patient_date_of_birth
# #             , d.patient_medical_record_number as patient_mrn
# #         from edw_tst.patient_demographics as d
# #         # where transport_completion_likelihood >= .90
# #         #   and risk_of_tansporting_patient < 100
# #         #   and risk_of_not_tranporting > 100
# #
# #     """
# #
# #
# #
# #     5. Hospital EMR has patient information in the system
# #     Physician Clears Patient for discharge
# #     Transport provider is contacted and minimum required patient data is shared with the
# #     transport provider (name, gender, date of birth, MRN)
# #     The pickup time is arranged
# #     Transport patient care record is ready to retrieve information and both the EMR and
# #     patient care record have an established XD* infrastructure.
# #     Main Flow:
# #     1. Transport teams arrives at the pick-up location and queries the patient information from
# #     the Hospital EMR to populate the patient care record system.
# #     2. 3. Transport team receives nurse report and transfer of care
# #     Patient contact is made and transport is started
# #     Post-conditions:
# #     1. 2. Patient information is updated in the patient care record system during transport.
# #     Patient is transferred to the care of the drop-off facility staff.
# #
# #
# #
# #
# # #
# # #
# # #     # ToDo 5. The pickup time is arranged
# # #     def patient_pickup_time_affirmation():
# # #
# # #         pat_pickup_request_status = 'tst'
# # #
# # #         patient_pickup_status_codes = {}
# # #
# # #         if pat_pickup_request_status == 'patient_pickup_available':
# # #
# # #         return pat_pickup_request_status
# # #
# # #
# # # # ToDo 6. Transport patient care record is ready to retrieve information and both the EMR and
# # # patient care record have an established XD* infrastructure.
# # #
# # #     return
# # #
# # #
# # #
