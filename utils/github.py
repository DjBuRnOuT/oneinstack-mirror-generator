import httpx

BLACKLIST_WORD = ["rc", "beta", "alpha"]


def download_repo_by_tag(owner_name: str, repo_name: str, archive_type: str = "tar.gz",
                         filter_blacklist: bool = True) -> list:
    """
    Download repository archive by tag

    This function will list all repository tags and download them one by one

    This function is suitable for GitHub repositories that does not make any releases and package is
    repository content itself

    :param owner_name: GitHub account name
    :param repo_name: repository name, e.g. "alibaba/tengine"
    :param archive_type: "tar.gz" or "zip"
    :param filter_blacklist: Boolean of trigger if filter blacklist word in tag name
    :return: list of dict, each dict contains at least "url" and "file_name"
    """
    if archive_type not in ["tar.gz", "zip"]:
        raise ValueError("archive_type must be 'tar.gz' or 'zip'")

    resource_list = []

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/git/refs/tags"
    if filter_blacklist:
        tag_list = [tag["ref"].replace("refs/tags/", "") for tag in httpx.get(url).json()
                    if not any(w in tag["ref"] for w in BLACKLIST_WORD)]
    else:
        tag_list = [tag["ref"].replace("refs/tags/", "") for tag in httpx.get(url).json()]
    for tag in tag_list:
        tag_archive_url = f"https://github.com/{owner_name}/{repo_name}/archive/refs/tags/{tag}.{archive_type}"
        resource_list.append({
            "url": tag_archive_url,
            "file_name": f"{repo_name}-{tag}.{archive_type}"
        })
    return resource_list
