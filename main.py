import argparse
import json
import requests
import pandas as pd


def main():
    parser = argparse.ArgumentParser(
        description="Run game analytics queries from a JSON file."
    )

    parser.add_argument(
        "filename",
        help="Path to the JSON filter file"
    )

    args = parser.parse_args()

    with open(args.filename, "r", encoding="utf-8") as file:
        config = json.load(file)

    url = "https://playsorceryonline.com/api/game-analytics/cohort"

    results = []

    for request_config in config["requests"]:
        response = requests.post(url, json=request_config)
        response.raise_for_status()

        data = response.json()
        cohort = data["cohort"]

        results.append({
            "playerGames": cohort["playerGames"],
            "matches": cohort["matches"],
            "wins": cohort["wins"],
            "winRate": cohort["winRate"],
            "unresolvedPlayerGames": data["unresolvedPlayerGames"],
            "unresolvedTurnPlayerGames": data["unresolvedTurnPlayerGames"]
        })

    df = pd.DataFrame(results)

    print(df)


if __name__ == "__main__":
    main()

