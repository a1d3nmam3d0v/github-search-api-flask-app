#  make requests to github API

import requests
import logging

# 404 username not found
# other errors
# success


def get_github_user(username):
    #   return a tuple of (data, error)
    #   if things work return (data, None)
    #   if they don't work, return (None, error)
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code == 404:  # not found
            return None, f"Username {username} not found"
        response.raise_for_status()
        response_json = response.json()
        user_info = extract_user_info(response_json)
        return user_info, None  # return data, error
    except Exception as e:
        logging.exception(e)
        return None, "Error connecting to Github"


def extract_user_info(json_response):
    return {
        "login": json_response.get("login"),
        "name": json_response.get("name"),
        "avatar_url": json_response.get("avatar_url"),
        "home_page": json_response.get("html_url"),
        "login": json_response.get("login"),
        "repos": json_response.get("public_repos"),
    }
