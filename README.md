# Game Analytics

A small Python program for querying the PlaySorcery game analytics API using filter configurations stored in JSON files.

Requirements
uv

# Setup

Clone the repository and install the dependencies:

```bash
  uv sync
```

# Query Filter Configuration

Create a JSON file containing one or more API requests.

For example, query.json:

{
  "requests": [
    {
      "selection": {
        "format": "constructed"
      },
      "filter": {
        "kind": "group",
        "operator": "and",
        "children": [
          {
            "kind": "condition",
            "field": "avatar",
            "value": "Archimago"
          }
        ]
      }
    }
  ]
}


Multiple requests can be added to the requests array.

Running

Pass the JSON filename to the program:

uv run main.py filters.json


You can also provide a path:

uv run main.py config/filters.json


The program will execute each request in the JSON file and load the results into a Pandas DataFrame.

Output

The API returns aggregate statistics such as:

Player games

Matches

Wins

Win rate

Unresolved player games

Unresolved turn player games

For example:

   playerGames  matches  wins  winRate
0           60       60    34   0.566667


The winRate value is represented as a decimal. For example:

0.566667 = 56.67%

Project Structure

A typical project might look like:

.
├── main.py
├── query.json
├── pyproject.toml
├── uv.lock
└── README.md

Adding More Filters

To query multiple avatars, add additional entries to the requests array:

{
  "requests": [
    {
      "selection": {
        "format": "constructed",
        "from": "2026-09-01",
        "through": "2026-10-02"
      },
      "filter": {
        "kind": "group",
        "operator": "and",
        "children": [
          {
            "kind": "condition",
            "field": "avatar",
            "value": "Archimago"
          }
        ]
      }
    },
    {
      "selection": {
        "format": "constructed",
        "from": "2026-09-01",
        "through": "2026-10-02"
      },
      "filter": {
        "kind": "group",
        "operator": "and",
        "children": [
          {
            "kind": "condition",
            "field": "avatar",
            "value": "AnotherAvatar"
          }
        ]
      }
    }
  ]
}


Each request will produce a separate row in the resulting DataFrame.

