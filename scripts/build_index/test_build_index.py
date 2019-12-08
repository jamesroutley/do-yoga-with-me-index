from list_videos import get_video_urls, get_video_details


def _class_list_html() -> str:
    with open("_testdata/class_list.html") as f:
        return f.read()


def _class_html() -> str:
    with open("_testdata/class.html") as f:
        return f.read()


def test_get_video_urls():
    expected = [
        "/content/fundamentals-day-7",
        "/content/fundamentals-day-6",
        "/content/fundamentals-day-5",
        "/content/fundamentals-day-4",
        "/content/fundamentals-day-3",
        "/content/fundamentals-day-2",
        "/content/fundamentals-day-1",
        "/content/cool-calm-yoga",
        "/content/happy-wrists-class",
        "/content/pilates-creative-challenge",
        "/content/pilates-focus-balance",
        "/content/advanced-pilates-flow",
        "/content/slow-flow-shoulders",
        "/content/release-resistance-meditation",
        "/content/open-hips-spine",
        "/content/prana-4",
        "/content/prana-3",
        "/content/prana-2",
        "/content/prana-1",
        "/content/elements-day-3",
        "/content/slow-flow-knees",
        "/content/desk-antidote",
        "/content/breathe-better",
        "/content/modified-sun-salutations",
    ]
    assert get_video_urls(_class_list_html()) == expected


def test_get_video_details():
    expected = {
        "difficulty": "intermediate",
        "duration": "37m51s",
        "teacher": "Rachel Scott",
        "rating": 5.0,
        "subscriber_only": False,
        "title": "Fundamentals of Practice Day 7",
        "votes": 7,
    }
    assert (get_video_details(_class_html())) == expected
