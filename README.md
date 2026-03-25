# <img src="https://www.mmobomb.com/logo.png" width="96" style="vertical-align:middle;" /> mmobomb.py

> Web-API for [MMOBomb](https://www.mmobomb.com) browse free-to-play MMOs, MMORPGs, multiplayer online and browser games, giveaways, and latest news.

## Quick Start
```python
from mmobomb import MmoBomb

mmobomb = MmoBomb()

# Get all games
games = mmobomb.get_games()
print(games)
```

---

## Methods

| Method | Description |
|--------|-------------|
| `get_games()` | Get all available games |
| `get_games_by_platform(platform)` | Filter games by platform |
| `get_games_by_category(category)` | Filter games by category |
| `get_games_by_tag(tag)` | Filter games by tag |
| `sort_games(sort)` | Get games sorted by a field |
| `get_games_by_all(platform, category, sort)` | Filter and sort in one call |
| `filter_games(platform, tag)` | Filter by multiple tags and platform |
| `get_game_details(game_id)` | Get full details for a specific game |
| `get_mmo_giveaways()` | Get active MMO giveaways |
| `get_latest_mmo_news()` | Get the latest MMO news |

---

## Reference

**Platforms:** `pc`, `browser`

**Categories:** `mmorpg`, `mmo`, `mmofps`, `mmotps`, `3d`, `2d`, `anime`, `fantasy`, `sci-fi`, `fighting`, `action`, `adventure`, `sports`, `racing`, `strategy`, `card`, `casual`

**Sort options:** `release-date`, `popularity`, `alphabetical`, `relevance`

---

## Examples
```python
mmobomb = MmoBomb()

# Filter by platform
mmobomb.get_games_by_platform(platform="browser")

# Filter by category
mmobomb.get_games_by_category(category="mmorpg")

# Filter by tag
mmobomb.get_games_by_tag(tag="fantasy")

# Filter and sort together
mmobomb.get_games_by_all(
    platform="pc",
    category="mmorpg",
    sort="popularity"
)

# Filter by multiple tags
mmobomb.filter_games(
    platform="pc",
    tag="3d.mmorpg.fantasy.pvp"
)

# Get details for a specific game
mmobomb.get_game_details(game_id=3)

# Get active giveaways
mmobomb.get_mmo_giveaways()

# Get latest news
mmobomb.get_latest_mmo_news()
```
