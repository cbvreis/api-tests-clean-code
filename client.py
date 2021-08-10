import requests
import argparse
import json
from loguru import logger

def send(data):
    response = requests.post('http://localhost:5000/data', json = {'data': data})
    return response.json()



def get(uuid):
    response = requests.get(f'http://localhost:5000/data/{uuid}')
    logger.debug(uuid)
    return response.json()

def request_operator(uuid, op):
    response = requests.get(f'http://localhost:5000/data/{uuid}/{op}')
    return response.json()

def main():
    parser =  argparse.ArgumentParser(description='Test API')
    parser.add_argument('--send',action='store_true')
    parser.add_argument('--get', action='store_true')
    parser.add_argument('--calc', action='store_true')
    parser.add_argument('--uuid', dest='uuid', type=str)
    parser.add_argument('--data', dest='data', type=str)
    parser.add_argument('--op',dest='op', type=str)

    args = parser.parse_args()

    if args.send and args.data:
        logger.info(f'Sending data {args.data}')
        response = send(args.data)
        logger.info(f'Response {response}')

    elif args.get and args.uuid:
        logger.info(f'Retrieving data using UUID {args.uuid}')
        response = get(args.uuid)
        logger.info(f'Response {response}')

    elif args.calc and args.op and args.uuid:
        logger.info(f'Requesting operation {args.op} using UUID {args.uuid}')
        response = request_operator(args.uuid,args.op)
        #response = get(args.uuid)
        logger.info(f'Response {response}')
    else:
        logger.warning(f'No action')



if __name__ == '__main__':
    main()
