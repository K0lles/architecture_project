import json

from datetime import datetime


class BaseRequestParser:

    def __init__(self, initial_request: None):
        self.initial_request = initial_request

    def parse_request(self):
        # Split the request into headers and body
        headers, body = self.initial_request.split(b'\r\n\r\n', 1)

        # Split the headers into a list
        header_list = headers.decode().split('\r\n')

        # Parse the method, path, and version from the first line of the headers
        method, path, version = header_list[0].split()

        print(f'{datetime.now().strftime("%H:%M")} - {method}: {path}: {body}')

        # Parse the headers into a dictionary
        headers_dict = {}
        for header in header_list[1:]:
            key, value = header.split(': ')
            headers_dict[key] = value

        # Check if Content-Type header contains form-data
        if 'Content-Type' in headers_dict and 'form-data' in headers_dict['Content-Type']:
            boundary = headers_dict['Content-Type'].split('boundary=')[1].encode()

            # Split the body into form-data fields
            form_data_fields = body.split(b'--' + boundary)[1:-1]

            # Parse each field into a dictionary
            form_data_dict = {}
            for field in form_data_fields:
                field_header, field_body = field.split(b'\r\n\r\n', 1)
                field_header_list = field_header.decode().split('\r\n')

                field_name = field_header_list[1].split('; ')[1].split('=')[1][1:-1]
                form_data_dict[field_name] = field_body[:-2].decode()

            body_dict = form_data_dict

        # If Content-Type is not form-data, assume it is JSON
        else:
            body_dict = json.loads(body.decode())

        # Combine everything into a single dictionary and return it
        return {
            'method': method,
            'path': path,
            'version': version,
            'headers': headers_dict,
            'body': body_dict
        }
