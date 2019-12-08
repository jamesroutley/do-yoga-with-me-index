import csv
import sys
import typing

import requests
from bs4 import BeautifulSoup  # type: ignore

base = "https://doyogawithme.com"


def main():

    writer = csv.DictWriter(
        sys.stdout,
        fieldnames=[
            "teacher",
            "title",
            "duration",
            "votes",
            "rating",
            "difficulty",
            "subscriber_only",
            "url",
        ],
    )
    writer.writeheader()

    page = 0
    while True:
        url = f"{base}/yoga-classes?page={page}"
        list_body = http_get(url)
        if "Sorry, but your search didn't return any results" in list_body:
            # A 200 with this string in the page body is returned when we hit
            # a page number which doesn't return any videos
            return
        urls = get_video_urls(list_body)
        for url in urls:
            video_body = http_get(base + url)
            details = get_video_details(video_body)
            details["url"] = base + url
            writer.writerow(details)
        page += 1


def http_get(url: str) -> str:
    r = requests.get(url)
    # Raise an exception for 4xx and 5xx HTTP status codes - we don't expect
    # any of these
    r.raise_for_status()
    return r.text


def get_video_urls(page: str) -> typing.List[str]:
    soup = BeautifulSoup(page, "html.parser")
    spans = soup.find_all("span", class_="field-content")
    return [_get_video_url(span) for span in spans]


def _get_video_url(span) -> str:
    a = span.find("a", href=True)
    return a["href"]


def get_video_details(page: str) -> typing.Dict:
    details = {}

    soup = BeautifulSoup(page, "html.parser")

    div = soup.find("div", {"id": "primary-info"})
    spans = div.find_all("span")
    details["teacher"] = spans[2].get_text()

    h1 = soup.find("h1", class_="page-title")
    classes = h1.attrs["class"]
    difficulty_class = classes[1]
    details["difficulty"] = remove_prefix(difficulty_class, "difficulty_")

    title = h1.get_text()
    details["title"] = title.strip()

    subscriber_only = soup.find("img", class_="subscriber-only")
    details["subscriber_only"] = subscriber_only is not None

    duration_min = soup.find("div", class_="field-name-field-minutes").get_text()
    duration_sec = soup.find("div", class_="field-name-field-seconds").get_text()
    details["duration"] = f"{duration_min}m{duration_sec}s"

    empty_span = soup.find("span", class_="empty")
    if empty_span is not None:
        empty = empty_span.get_text()
        if empty == "No votes yet":
            details["rating"] = 0
            details["votes"] = 0
            return details

    rating = soup.find("span", class_="average-rating").get_text()
    rating = rating.replace("Average: ", "")
    details["rating"] = float(rating)

    votes = soup.find("span", class_="total-votes").get_text()
    votes = votes.strip("()")
    votes = votes.replace(" votes", "")
    votes = votes.replace(" vote", "")
    details["votes"] = int(votes)

    return details


def remove_prefix(s: str, prefix: str):
    if s.startswith(prefix):
        len_prefix = len(prefix)
        return s[len_prefix:]
    return s


if __name__ == "__main__":
    main()
