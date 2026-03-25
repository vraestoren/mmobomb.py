from requests import Session

class MmoBomb:
    def __init__(self) -> None:
        self.api = "https://www.mmobomb.com/api1"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
        }

    def _get(self, endpoint: str) -> dict:
        return self.session.get(f"{self.api}{endpoint}").json()

    def get_games(self) -> dict:
        return self._get("/games")

    def get_games_by_platform(
            self, platform: str = "pc") -> dict:
        return self._get(f"/games?platform={platform}")

    def get_games_by_category(self, category: str) -> dict:
        return self._get(f"/games?category={category}")

    def get_games_by_tag(self, tag: str) -> dict:
        return self._get(f"/games?tag={tag}")

    def sort_games(self, sort: str) -> dict:
        return self._get(f"/games?sort-by={sort}")

    def get_games_by_all(
            self,
            platform: str = "browser",
            category: str = "mmorpg",
            sort: str = "release-date") -> dict:
        return self._get(
            f"/games?platform={platform}&category={category}&sort-by={sort}")

    def filter_games(
            self,
            platform: str = "pc",
            tag: str = "3d.mmorpg.fantasy.pvp") -> dict:
        return self._get(f"/filter?tag={tag}&platform={platform}")

    def get_game_details(self, game_id: int) -> dict:
        return self._get(f"/game?id={game_id}")

    def get_mmo_giveaways(self) -> dict:
        return self._get("/giveaways")

    def get_latest_mmo_news(self) -> dict:
        return self._get("/latestnews")
