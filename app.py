from helpers import config, client_ip, api_client, console
import time
import sys


def loop(interval_sec):
    while True:
        current = client_ip.get_ip_address()
        last = api_client.get_last_ip_address()

        if last != "CONNFAIL" and current != "CONNFAIL":
            if current != last:
                api_client.save_current_ip_address(current)
            else:
                console.log("IP not changed")

        time.sleep(interval_sec)


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')

    interval_seconds = int(config.get_value("interval"))
    loop(interval_seconds)
