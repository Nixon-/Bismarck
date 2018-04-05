

from bismarck.utils import config_helper
import urllib.parse
import urllib.request
import json

SERVICE_ENDPOINT_PARAM_NAME = "service endpoints"


def api_get(service_name, api_endpoint, args=None):
    service_config = config_helper.get_config(SERVICE_ENDPOINT_PARAM_NAME, service_name)
    return _get(service_config['hostname'], service_config['port'], api_endpoint, args)


def _get(hostname, port, api_endpoint, args=None):
    if args is None:
        formatted_url = 'http://{}:{}/{}'.format(hostname, port, api_endpoint)
    else:
        formatted_url = 'http://{}:{}/{}?{}'.format(hostname, port, api_endpoint, urllib.parse.urlencode(args))
    with urllib.request.urlopen(formatted_url) as url:
        return json.loads(url.read().decode())
