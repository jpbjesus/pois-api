#!/usr/bin/env python3

import connexion
import logging

from swagger_server import encoder

def main():
    # logging.basicConfig(filename='app.log', filemode='w',
    #                     format='%(name)s - %(levelname)s - %(message)s')
    # logging.warning('This will get logged to a file')
    
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'POIs API'})
    app.run(port=8080, debug=True)

if __name__ == '__main__':
    main()
