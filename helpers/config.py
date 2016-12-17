def get_value(key):
    in_memory = dict(
            public_ip_url="http://myexternalip.com/raw",
            interval="2",  # seconds
            api_get="https://pisip.herokuapp.com/api/get", # "http://127.0.0.1:5000/api/get",
            api_post="https://pisip.herokuapp.com/api/add" # "http://127.0.0.1:5000/api/add"
    )
    return in_memory[key]
