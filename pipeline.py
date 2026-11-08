from datetime import datetime
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET

RESTORATION_PROJECTS = [
    "Boeing 747 Restoration",
    "Giant Submarine Restoration",
    "Luxury Yacht Restoration",
    "Space Shuttle Restoration",
    "Giant Train Restoration"
]

CHARACTERS = """
CHARACTER 1:
Original thin white cartoon character,
black hand-drawn outline, expressive face.

CHARACTER 2:
Different original thin white cartoon character,
black hand-drawn outline, expressive face.

Both characters must remain visually identical
in every scene and every episode.
"""

def get_trends():
    url = "https://trends.google.com/trending/rss?geo=US"

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        with urllib.request.urlopen(request, timeout=20) as response:
            root = ET.fromstring(response.read())

        return [
            item.findtext("title")
            for item in root.findall(".//item")
            if item.findtext("title")
        ][:10]

    except Exception as error:
        print("Trend research unavailable:", error)
        return []

def create_video_plan():

    today = datetime.now()
    output = Path("output")
    output.mkdir(exist_ok=True)

    trends = get_trends()

    week = today.isocalendar().week
    restoration = RESTORATION_PROJECTS[
        (week - 1) % len(RESTORATION_PROJECTS)
    ]

    videos = [
        {
            "type": "2D CARTOON ANIMATION",
            "topic": "Funny Two Friends Story",
            "characters": CHARACTERS,
            "story": (
                "Two friends discover a mysterious box. "
                "They misunderstand what is inside, "
                "creating a funny situation and ending."
            )
        },
        {
            "type": "2D CARTOON ANIMATION",
            "topic": "Funny Food Challenge",
            "characters": CHARACTERS,
            "story": (
                "Two friends try the same unusual food. "
                "Their reactions create a funny competition "
                "with an unexpected ending."
            )
        },
        {
            "type": "REALISTIC RESTORATION",
            "topic": restoration,
            "characters": "Not required",
            "story": (
                "Show damaged condition, transport, cleaning, "
                "inspection, repair and final transformation."
            )
        }
    ]

    filename = output / "weekly_video_plan.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("WEEKLY AI YOUTUBE VIDEO PLAN\n")
        file.write(f"Date: {today}\n\n")

        file.write("USA TRENDING TOPICS\n")

        for trend in trends:
            file.write(f"- {trend}\n")

        if not trends:
            file.write("Trending data unavailable.\n")

        for number, video in enumerate(videos, 1):

            file.write(f"\n{'=' * 40}\n")
            file.write(f"VIDEO {number}\n")
            file.write(f"TYPE: {video['type']}\n")
            file.write(f"TOPIC: {video['topic']}\n")

            file.write("\nCHARACTER DETAILS:\n")
            file.write(video["characters"])

            file.write("\nSTORY:\n")
            file.write(video["story"] + "\n")

            file.write("\nVIDEO FORMAT:\n")
            file.write("Vertical 9:16\n")
            file.write("HD cinematic quality\n")
            file.write("Consistent visual style\n")
            file.write("Natural sound effects\n")

            file.write("\nPRODUCTION REQUIREMENTS:\n")
            file.write("Image prompts for every scene\n")
            file.write("Separate 10-second video prompts\n")
            file.write("Voiceover script\n")
            file.write("Thumbnail prompt\n")

            file.write("\nTITLE:\n")
            file.write(f"Amazing {video['topic']}!\n")

            file.write("\nDESCRIPTION:\n")
            file.write(
                f"Watch this amazing {video['topic']}. "
                "Subscribe for more videos!\n"
            )

            file.write("\nTAGS:\n")
            file.write(
                "animation, cartoon, restoration, "
                "AI video, satisfying, entertainment\n"
            )

            file.write(
                "\nSTATUS: WAITING FOR SAGAR'S APPROVAL\n"
            )

    print("Weekly video plan created successfully!")
    print("2 Animation + 1 Restoration")
    print("Waiting for approval.")

if __name__ == "__main__":
    create_video_plan()
