import short_url


def short_url_encode(data):
    if isinstance(data, int):
        return short_url.encode_url(data)
    elif isinstance(data, str):
        encoded_data = int.from_bytes(data.encode(), "big")
        return short_url.encode_url(encoded_data)
    else:
        raise ValueError(
            "Unsupported data type. Only integers and strings are supported."
        )


if __name__ == "__main__":
    url = input("Enter the URL: ")
    short_url_encode(url)
