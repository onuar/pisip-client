def get_value(key):
    in_memory = dict(
            public_ip_url="http://myexternalip.com/raw",
            interval="2",  # seconds
            api_get="http://127.0.0.1:5000/api/get", # "https://pisip.herokuapp.com/api/get",
            api_post="http://127.0.0.1:5000/api/add" # "https://pisip.herokuapp.com/api/add"
    )
    return in_memory[key]
