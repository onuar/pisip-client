import requests, sys
import config, console
import rsa_encryption


def get_last_ip_address():
    get_url = config.get_value("api_get")
    try:
        signature = _get_signature()
        payload = {'token': signature}
        get_result = requests.get(get_url, params=payload)
        response = get_result.json()
        ip_address = response["last_ip_address"]
        console.log("Last: {}".format(ip_address))
        return ip_address
    except requests.exceptions.ConnectionError:
        console.log("Connection failed: "+ get_url)
        return "CONNFAIL"
    except Exception as ex:
       console.log("An exeption occured: " + ex.message)


def save_current_ip_address(current_ip):
    signature = _get_signature()
    post_url = config.get_value("api_post")
    request_data = {'ipaddress': current_ip, 'token':signature}
    response = requests.post(post_url, json=request_data)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError(response.reason)
    console.log("Changed: {}".format(current_ip))


def _get_signature():
    signature = rsa_encryption.get_signature()
    return signature
