import argparse
import logging
import requests
import sys


def escape_string(string):
    return string.translate(string.maketrans({",": "\,", " ": "\ ", "=": "\="}))


def create_database(db_host, db_port, db_name):
    if not db_name:
        raise Exception('create_database: no database specified')

    url = f"http://{db_host}:{db_port}/query"
    response = requests.post(url, params=dict(q=f"CREATE DATABASE {db_name}"))
    logging.info(response.url)
    if response.status_code != requests.codes.ok:
        raise Exception(f'create_database: {response.status_code}:{response.reason}')


def drop_database(db_host, db_port, db_name):
    if not db_name:
        raise Exception('drop_database: no database specified')

    url = f"http://{db_host}:{db_port}/query"
    response = requests.post(url, params=dict(q=f"DROP DATABASE {db_name}"))
    logging.info(response.url)
    if response.status_code != requests.codes.ok:
        raise Exception(f'drop_database: {response.status_code}:{response.reason}')


def dump_eq_data(size, window, output):
    url = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{size}_{window}.geojson"
    response = requests.get(url)
    logging.info(response.url)
    if response.status_code != requests.codes.ok:
        raise Exception(f"dump_eq_data: {response.status_code}:{response.reason}")

    for feature in response.json()['features']:
        measure = "event"

        mag = feature['properties']['mag']
        if mag is None:
            logging.error(f"bad event: {feature}")
            continue

        place = feature['properties']['place']
        lon, lat, dep = feature['geometry']['coordinates']

        tags = [
            f"latitude={lat}",
            f"longitude={lon}",
            f"place={escape_string(place)}",
            f"magnitude={escape_string(str(mag))}"
        ]

        metrics = [
            f"magnitude={mag}",
            f"depth={dep}",
        ]

        timestamp = feature['properties']['time']

        data = f"{measure},{','.join(tags)} {','.join(metrics)} {timestamp}\n"
        logging.debug(data)
        output.write(data)

    output.close()


def load_eq_data(db_host, db_port, db_name, input_file):
    if not db_name:
        raise Exception(f'drop: no database specified')

    create_database(db_host=db_host, db_port=db_port, db_name=db_name)

    url = f"http://{db_host}:{db_port}/write"
    data = input_file.read().encode('utf-8')
    response = requests.post(url, params=dict(db=db_name, precision="ms"), data=data)
    if response.status_code != requests.codes.no_content:
        raise Exception(f"load_eq_data: {response.status_code}:{response.reason}")


def process_cli():
    parser = argparse.ArgumentParser(description="read earthquake data from USGS into Influxdb")
    file_group = parser.add_mutually_exclusive_group()

    parser.add_argument('--host', dest='host', default='localhost',
                        help='database host')
    parser.add_argument('--port', dest='port', type=int, default=8086,
                        help='database port')
    parser.add_argument('--db', dest='database',
                        help="name of database to store data in")
    parser.add_argument('--drop', dest='drop', action='store_true',
                        help='drop database')
    file_group.add_argument('--input', dest='input_file', type=argparse.FileType('r'),
                            help="input file")
    file_group.add_argument('--output', dest='output_file', type=argparse.FileType('w'),
                            help='output file')

    parser.add_argument("--size", dest="size", choices=['significant', '4.5', '2.5', '1.0', 'all'],
                        default='significant', help="earthquake size")
    parser.add_argument("--window", dest="window", choices=['hour', 'day', 'week', 'month'],
                        default='hour', help="earthquake time window")

    return parser.parse_args()


def main():
    logging.basicConfig(level=logging.INFO)
    args = process_cli()

    if args.drop:
        drop_database(db_host=args.host, db_port=args.port, db_name=args.database)

    if args.output_file:
        dump_eq_data(args.size, args.window, args.output_file)

    if args.input_file:
        load_eq_data(db_host=args.host, db_port=args.port, db_name=args.database, input_file=args.input_file)


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as err:
        logging.exception(err)
        sys.exit(1)
