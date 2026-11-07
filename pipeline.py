from datetime import datetime
from pathlib import Path

PROJECTS = [
    "Boeing 747 Restoration",
    "Giant Submarine Restoration",
    "Luxury Yacht Restoration",
    "Space Shuttle Restoration",
    "Giant Train Restoration"
]

def create_video_plan():
    today = datetime.now()
    output = Path("output")
    output.mkdir(exist_ok=True)

    week = today.isocalendar().week
    start = (week * 3) % len(PROJECTS)

    selected = [
        PROJECTS[(start + i) % len(PROJECTS)]
        for i in range(3)
    ]

    filename = output / "weekly_video_plan.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("WEEKLY YOUTUBE VIDEO PLAN\n")
        file.write(f"Date: {today}\n\n")

        for number, topic in enumerate(selected, 1):
            file.write(f"\nVIDEO {number}\n")
            file.write(f"Topic: {topic}\n")
            file.write(f"Title: Amazing {topic} | Full Transformation\n")
            file.write(
                f"Description: Watch this incredible {topic} "
                "transformation. Subscribe for more restorations!\n"
            )
            file.write(
                "Tags: restoration, airplane repair, AI restoration, "
                "satisfying transformation\n"
            )
            file.write("Status: WAITING FOR SAGAR'S APPROVAL\n")

    print("Weekly video drafts created successfully!")
    print("All 3 videos are waiting for approval.")

if __name__ == "__main__":
    create_video_plan()
