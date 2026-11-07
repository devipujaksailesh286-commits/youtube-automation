from datetime import datetime
from pathlib import Path

def create_video_plan():
    videos = [
        "Boeing 747 Restoration",
        "Giant Submarine Restoration",
        "Luxury Yacht Restoration"
    ]

    folder = Path("output")
    folder.mkdir(exist_ok=True)

    filename = folder / "weekly_video_plan.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("WEEKLY YOUTUBE VIDEO PLAN\n")
        file.write(f"Date: {datetime.now()}\n\n")

        for number, video in enumerate(videos, 1):
            file.write(f"{number}. {video}\n")

    print("Weekly video plan created successfully!")

if __name__ == "__main__":
    create_video_plan()
