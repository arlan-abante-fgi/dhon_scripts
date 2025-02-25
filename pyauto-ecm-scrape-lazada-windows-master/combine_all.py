from utils.combine_ext import combine_ext
from utils.combine_npl import combine_npl
from utils.combine_sa import combine_sa
from utils.combine_sm import combine_sm
from utils.combine_ss import combine_ss

import os


def combine_all():

    if not os.path.exists(f'./data/to_upload/'):
        os.makedirs(f'./data/to_upload/')

    combine_ext()
    combine_npl()
    combine_sa()
    combine_sm()
    combine_ss()
    
# combine_sa()

# combine_all()

