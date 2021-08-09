def get_entries_ids(url):
    """
        url : filled form url

        provider : form creator

        returns list of form entries ids
        """
    from urllib import parse
    L = []
    for i in dict(parse.parse_qsl(parse.urlsplit(url).query)).keys():
        # noinspection PyTypeChecker
        if i.startswith("entry"):
            L.append(i)
    return L


def generate_post_request_url(url):
    post_url = url.split("/")
    post_url[-1] = "formResponse"
    return "/".join(post_url)
