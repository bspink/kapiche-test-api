import os
import datetime
import csv

from flask import request, jsonify
from typing import Dict, Optional


def get_nps_data():

    start_date = request.args.get('start_date')
    if start_date:
        start_date = convert_date(date=start_date)

    end_date = request.args.get('end_date')
    if end_date:
        end_date = convert_date(date=end_date)

    print(f'start date is {start_date}')
    print(f'end date is {end_date}')

    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(
        base_dir,
        'data',
        'nps.csv'
    )
    nps_data = _get_nps_csv_data(
        filepath=filepath,
        start_date=start_date,
        end_date=end_date,
    )
    return jsonify({'nps': nps_data})


def _get_nps_csv_data(filepath: str,
                      start_date: Optional[datetime.date],
                      end_date: Optional[datetime.date]) -> Dict[str, int]:
    """
    Return the NPS data stored in the csv file at "filepath"
    Returns a dict of the form "date -> score", where date is an IOS 8601
    formatted date string.
    """

    nps_records = []

    with open(filepath) as csv_file:

        reader = csv.DictReader(csv_file)

        for row in reader:

            # Parse the time from the CSV.
            response_date = convert_date(date=row['Date Published'])

            # Don't return records outside of the specified time range
            # (there may be no time range specified).
            if start_date and response_date < start_date:
                continue
            elif end_date and response_date > end_date:
                continue

            try:
                nps = int(row['NPS'])
            except:
                # Error parsing score - just skip and continue.
                continue

            nps_records.append(
                dict(
                    year=response_date.year,
                    month=response_date.month,
                    day=response_date.day,
                    nps=int(nps),
                )
            )

    return nps_records


def convert_date(date: str) -> datetime.date:
    return datetime.datetime.strptime(date, '%d/%m/%Y')
