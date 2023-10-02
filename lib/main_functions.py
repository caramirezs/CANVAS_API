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

def enroll_user(user_id=0, course_id=0, role_id=0, token='xxxx', action=1, verbose=True):
    """
    Enroll or delete a user from a course.

    :param verbose:
    :param user_id: Id of the user to enroll
    :param course_id: Id of the course to enroll the user
    :param api_key_canvas: API key for the canvas API

    :param action: operation to be performed. `1` to enroll the user, `0` to delete the enrollment

    :return: None
    """
    api_url = f"https://poli.instructure.com/api/v1"
    payload = {
        'include': 'sections'
    }
    info_course = get_function(url=f"{api_url}/courses/{course_id}",
                              payload=payload,
                              token=token,
                              verbose=False)
    if len(info_course['sections']) != 0:
        section_id = info_course['sections'][0]['id']
    else:
        return 'FAIL'

    url = f"{api_url}/courses/{course_id}/enrollments"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        'enrollment[user_id]': str(user_id),
        'enrollment[role_id]': role_id,
        'enrollment[course_section_id]': section_id,
        'enrollment[enrollment_state]': 'active'
    }

    if action == 1:  # Enroll the user
        response = requests.post(url, headers=headers, params=payload)
        if response.status_code == 200:
            if verbose:
                print(f'>> Usuario {user_id} ha sido matriculado del curso ID: {course_id}')
            return 'SUCCESS'
        else:
            payload = {
                'course_id': course_id,
                'enrollment[user_id]': str(user_id),
                'enrollment[role_id]': role_id,
                'enrollment[enrollment_state]': 'active'
            }
            response = requests.post(url, headers=headers, params=payload)
            if response.status_code == 200:
                if verbose:
                    print(f'>> Usuario {user_id} ha sido matriculado del curso ID: {course_id}')
                return 'SUCCESS'
            else:
                print(f">> ERRMAT: No se pudo matricular el usuario {user_id}")
                return 'FAIL'

    elif action == 0:  # Delete Enrollment
        # Get enrollment ID from Canvas API
        r = requests.get(f"{url}?user_id={user_id}", headers=headers)
        if r.status_code == 200:
            enrollments = r.json()
            enroll_id = None

            for enrollment in enrollments:
                if enrollment['course_id'] == int(course_id):
                    enroll_id = enrollment['id']
                    break

            # Delete the enrollment from the course
            if enroll_id:
                r = requests.delete(f"{url}/{enroll_id}?task=delete", headers=headers)
                if r.status_code == 200:
                    if verbose:
                        print(f'>> Usuario {user_id} ha sido desmatriculado del curso ID: {course_id}')
                    return 'SUCCESS'
                else:
                    if verbose:
                        print(f">> ERRMAT: No se pudo eliminar la matrícula del curso {course_id}")
                    return 'FAIL'
            else:
                if verbose:
                    print(f">> ERRMAT: No se pudo obtener las matrículas del usuario {user_id}")
                return 'FAIL'
        else:
            if verbose:
                print(f">> ERRMAT: No se pudo obtener las matrículas del usuario {user_id}")
            return 'FAIL'
    else:
        print('ERRMAT: Acción inválida. Debe ser 1 (matricular usuario) o 0 (eliminar matrícula)')
        return 'FAIL'