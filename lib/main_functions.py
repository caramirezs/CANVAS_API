import os
import sys
import csv
import pandas as pd
import glob
import requests
from colorama import Fore, Back, Style, init

init(autoreset=True)  # reset the previous color and style after each line


def get_function(url='', payload={}, token='', verbose=True):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, json=payload)
    if verbose:
        if response.status_code == 200:
            color = Fore.GREEN
        else:
            color = Fore.RED
        print(color + f'{response.status_code} >> {response.reason}')
    if response.status_code == 200:
       return response
    else:
        return None