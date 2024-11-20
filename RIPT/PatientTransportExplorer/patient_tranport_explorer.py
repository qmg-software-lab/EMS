import os
import sys
import logging
import sqlite3
import pathlib
import pyfiglet
from colorama import Fore
import pandas as pd
from datetime import datetime, timedelta
import logging
from datetime import datetime
from datetime import time
import pandas as pd
import warnings
from fileinput import filename
from tabnanny import filename_only
# import boto3
# import watson

line_1 = pyfiglet.figlet_format(' WELCOME to Patient Transport Explorer!')
line_2 = 'A Routine Interfacility Patient Transport (RIPT) module'
print(Fore.CYAN + line_1)
print(Fore.CYAN + line_2)



# configure logging
log_file_name = __file__.split('/')[-1].split('.')[0]
project_root = os.path.dirname(os.path.abspath(__file__))
log_file_path = project_root + '/RIPT/PatientTransportExplorer/logs/' + log_file_name + '.log'
file_handler = logging.FileHandler(filename=log_file_path)
stdout_handler = logging.StreamHandler(stream=sys.stdout)
handlers = [file_handler, stdout_handler]
logging.basicConfig(handlers=handlers, level=logging.INFO)
logger = logging.getLogger(log_file_name + '-logger')
time_mtn = datetime.now()
warnings.simplefilter(action='ignore', category=FutureWarning)
print('\n-------------------------------------------------------------------------------------------------------------')
logging.info('\n\n ( WELCOME to the RIPT Patient Transport Explorer (PeTE)')
print('---------------------------------------------------------------------------------------------------------------')
logger.info(' \n\n Module start time: {}'.format(time_mtn))
file_path = os.path.dirname(os.path.abspath(__file__))
print('---------------------------------------------------------------------------------------------------------------')
logger.info(' logger file path =\n{}'.format(file_path))


# ToDo Step Zero: Setup dataflow pathway
def dataflow_pathway():
    dataflow_dict = {}
    return dataflow_dict


#  ToDo: Step 1: Hospital EMR has patient information in the system
def emr_get_record():

    pat_record_id = pd'run "qry_get_patient_details"'

    return pat_record_id


# ToDo 2. Physician Clears Patient for discharge
def hospital_ddx_and_dispo_cleared():

    """
    pat_emergency_ddx = my_scrapingFunction(scrape_epic(
    pat_inpatient_ddx = hospital_svc.ddx
    pat_acutecare_ddx)
    """

    return pat_emergency_ddx, pat_inpatient_ddx, pat_acutecare_ddx


# ToDo 3. Transport provider is contacted and minimum required patient data is shared with the transport provider
    #         (name, gender, date of birth, MRN)
    def transporting_agency contacted_initiated()




# ToDo 4. transport provider (name, gender, date of birth, MRN)


    # ToDo 5. The pickup time is arranged
    def patient_pickup_time_affirmation():

        pat_pickup_request_status = 'tst'

        patient_pickup_status_codes = {}

        if pat_pickup_request_status == 'patient_pickup_available':

        return pat_pickup_request_status


# ToDo 6. Transport patient care record is ready to retrieve information and both the EMR and
patient care record have an established XD* infrastructure.

    return



