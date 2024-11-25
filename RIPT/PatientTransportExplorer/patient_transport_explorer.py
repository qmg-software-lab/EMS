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
# log_file_name = __file__.split('/')[-1].split('.')[0]
# project_root = os.path.dirname(os.path.abspath(__file__))
# log_file_path = project_root + '/logs/' + log_file_name + '.log'
# file_handler = logging.FileHandler(filename=log_file_path)
# stdout_handler = logging.StreamHandler(stream=sys.stdout)
# handlers = [file_handler, stdout_handler]
# logging.basicConfig(handlers=handlers, level=logging.INFO)
logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(log_file_name + '-logger')
logger = logging.getLogger(__name__)
time_mtn = datetime.now()
warnings.simplefilter(action='ignore', category=FutureWarning)

# figlet
line_0 = ' '
line_1 = ' WELCOME to RIPT: '
line_2 = pyfiglet.figlet_format(' Routine Interfacility Patient Transport ')
line_3 = 'solution extension explorer module'
print(Fore.CYAN + line_0);
print();
print(line_1);
print(Fore.CYAN + line_2);
print(Fore.CYAN + line_3)
print('\n-------------------------------------------------------------------------------------------------------------')
logging.info('\n\n ( WELCOME to Routine Interfacility Patient Transport - RIPT Data Explorer')
print('---------------------------------------------------------------------------------------------------------------')
logger.info(' \n\n Module start time: {}'.format(time_mtn))
file_path = os.path.dirname(os.path.abspath(__file__))
print('---------------------------------------------------------------------------------------------------------------')
logger.info(' logger file path =\n{}'.format(file_path))


# Open Issues and Questions
# 1. How can we reuse transactions and create transactions based on its use in QEDm?
#    Patient Medical History and risk factors map to multiple FHIR resources: Procedures,
# conditions, date of onset.
# Should we subsume the mappings in the ETS and ITS Profiles into this profile and
# deprecate them?
# There is a FHIR resource gap for Transport instructions.
# Should the Transport Data Consumer and Transport Data Responder Actors have a more
# generic name such as Data Consumer and Data Responder?
# 6. There is no LOINC code for Revised Trauma Score.
# 7. Cannot find the NEMSIS copyright statement.


# ToDo Step 0: Ingest sample dataframe
def sendero():
    qry_get_sample_data_frame_without_a_name = """
        SELECT * FROM LATERAL (  ) 



    """

    sample_dataframe_without_a_name_dict = {}
    # function to kickoff dataflow
    gen_a_sample_dataframe_without_a_name_is_the_game = pd.read_sql_query('qry_get_sample_dataframe_without_a_name')

    return sample_dataframe_without_a_name_dict


# ToDo Step 1: Hospital EMR has patient information in the system
def patient_record():
    pat_record_id_dict = {}
    logger.info(' Validating patient record cycle for transfer eligibility...\n...please wait')
    try:
        # Create an in-memory SQLite database
        logger.info(' opening odbc tunnel')
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

        # Create test data
        df = pd.DataFrame(data=[[0, '10/11/12'], [1, '12/11/10']], columns=['int_column', 'date_column'])
        df.to_sql(name='test_data', con=conn, index=False, if_exists='replace')

        # Query the database to simulate fetching patient records
        qry_emr_record_existence_check = """SELECT * FROM test_data"""
        result_df = pd.read_sql_query(qry, conn)
        logger.info(' querying EMR for patient records ')

        # Process query results
        if not result_df.empty:
            pat_record_id_dict = result_df.set_index('int_column').to_dict(orient='index')
        else:
            raise Exception('No patient record ID found')

    except Exception as e:
        logger.error('Error during patient record validation: {}'.format(e))
        raise

    finally:
        conn.close()

    logger.info('Patient record validation completed.')
    return pat_record_id_dict


# Example usage
if __name__ == "__main__":
    try:
        pat_eid_list = patient_record()
        print("Patient Record Data:", pat_eid_list)
    except Exception as e:
        logger.error(f"Failed to retrieve patient records: {e}")


# Step 1: ToDo: Hospital EMR has patient information in the system
def patient_record():
    pat_record_id_dict = {}
    logger.info(' validating patient record for transfer eligibility...\n ...please wait...')
    try:
        conn = connect(':memory:')
        df = pd.DataFrame(data=[[0, '10/ 11/ 12'], [1, '12/ 11/ 10']], columns=['int_column', 'date_column'])
        # qry_pat_details = pd.read_sql() 'qry_get_patient_details')
        df.to_sql(name='test_data', con=conn)
    except Exception as e_pat_record_missing:
        logger.ERROR(' No patient record id found: {}'.format(e_pat_record_missing))
    finally:
        conn.close()
    if pat_record_id:
        pass
    return pat_record_id_dict


pat_eid_list = patient_record()

#
#
#
#
#
# # Step 2. ToDo: Physician clears patient for discharge
# def discharge_approved():
#     physician_discharge_order_status_dict = {}
#     if physician_discharge_order_status[0] == 'dispositioned':
#         physician_clears_patient_for_discharge_ack = 'ready'
#     else:
#         physician_clears_patient_for_discharge_ack = 'pending'
#
#     while pat_eid < max_pat_eid:
#
#
#     pat_ddx_series = [pat_emergency_care_center_ddx, pat_inpatient_nonacutecare_ddx, pat_inpatient_acutecare_ddx]
#     """
#     qry_get_patient_details
#         result = pd.to_sql(             """
#         pat_emergency_ddx = my_scrapingFunction(scrape_epi
#         pat_inpatient_ddx = hospital_svc.ddx
#         pat_acutecare_ddx
#         """
#     return discharge_order_status_dict
#
#
#
# # # # ToDo Step 3. Transport provider contacted and minimum required patient data is exchanged
# # # def transporting_agency_contact_affirmation():
# # #
# # #     def patient_transport_risk_mitigator():
# # #         # pd.api('get' )
# # #         risk_score = 532
# # #
# # #         # where transport_completion_likelihood >= .90
# # #         #   and risk_of_tansporting_patient < 100
# # #         #   and risk_of_not_tranporting > 100
# # #
# # #
# # #
# # #
# # #         if risk_score > 500:
# # #             patient_transport_risk_assessment_order_level = 5
# # #             risk_score = patient_transport_risk_assessment_order_level * ('some numbers here')
# # #
# # #         return patient_transport_risk_assessment_order
# # #
# # #
# # #     minimum_pat_details = [
# # #           'name'
# # #         , 'gender'
# # #         , 'date of birth'
# # #         , 'MRN'
# # #     ]
# # #     minimum_provider_details = [
# # #           'transporting_provider_name'
# # #         , 'transporting_provider_dispatch_active_transaction_code'
# # #         , 'transporting_provider_request_acknowledgement'
# # #     ]
# # #
# # #
# # #
# # #     qry_get_patient_details = """
# # #         select
# # #               d.first_name as patient_first_name
# # #             , d.last_name as patient_last_name
# # #             , d.gender as patient_gender
# # #             , d.date_of_birth as patient_date_of_birth
# # #             , d.patient_medical_record_number as patient_mrn
# # #         from edw_tst.patient_demographics as d
# # #         # where transport_completion_likelihood >= .90
# # #         #   and risk_of_tansporting_patient < 100
# # #         #   and risk_of_not_tranporting > 100
# # #
# # #     """
# # #
# # #
# # #
# # #     5. Hospital EMR has patient information in the system
# # #     Physician Clears Patient for discharge
# # #     Transport provider is contacted and minimum required patient data is shared with the
# # #     transport provider (name, gender, date of birth, MRN)
# # #     The pickup time is arranged
# # #     Transport patient care record is ready to retrieve information and both the EMR and
# # #     patient care record have an established XD* infrastructure.
# # #     Main Flow:
# # #     1. Transport teams arrives at the pick-up location and queries the patient information from
# # #     the Hospital EMR to populate the patient care record system.
# # #     2. 3. Transport team receives nurse report and transfer of care
# # #     Patient contact is made and transport is started
# # #     Post-conditions:
# # #     1. 2. Patient information is updated in the patient care record system during transport.
# # #     Patient is transferred to the care of the drop-off facility staff.
# # #
# # #
# # #
# # #
# # # #
# # # #
# # # #     # ToDo 5. The pickup time is arranged
# # # #     def patient_pickup_time_affirmation():
# # # #
# # # #         pat_pickup_request_status = 'tst'
# # # #
# # # #         patient_pickup_status_codes = {}
# # # #
# # # #         if pat_pickup_request_status == 'patient_pickup_available':
# # # #
# # # #         return pat_pickup_request_status
# # # #
# # # #
# # # # # ToDo 6. Transport patient care record is ready to retrieve information and both the EMR and
# # # # patient care record have an established XD* infrastructure.
# # # #
# # # #     return
# # # #
# # # #
# # # #
# # # ToDo Step 0: Write an app to dynamically gen a dataflow diagram for team collaboration
# # def dataflow_diagram():
# #     dataflow_dict = {}
# #     return dataflow_dict
# #
