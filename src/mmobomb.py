from requests import Session

class MmoBomb:
    def __init__(self) -> None:
        self.api = "https://www.mmobomb.com/api1"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
        }
    
    def get_games(self) -> dict:
        return self.session.get(f"{self.api}/games").json()
    
    def get_games_by_platform(
            self,
            platform: str = "pc") -> dict:
        return self.session.get(
            f"{self.api}/games?platform={platform}").json()
    
    def get_games_by_category(
            self,
            category: str) -> dict:
        return self.session.get(
            f"{self.api}/games?category={category}").json()
    
    def get_games_by_tag(self, tag: str) -> dict:
        return self.session.get(
            f"{self.api}/games?tag={tag}").json()
    
    def sort_games(self, sort: str) -> dict:
        return self.session.get(
            f"{self.api}/games?sort-by={sort}").json()
    
    def get_games_by_all(
            self,
            platform: str = "browser",
            category: str = "mmorpg",
            sort: str = "release-date") -> dict:
        return self.session.get(
            f"{self.api}/games?platform={platform}&category={category}&sort-by={sort}").json()
    
    def filter_games(
            self,
            platform: str = "pc",
            tag: str = "3d.mmorpg.fantasy.pvp") -> dict:
        return self.session.get(
            f"{self.api}/filter?tag={tag}&platform={platform}").json()
        
    def get_game_details(self, game_id: int) -> dict:
        return self.session.get(
            f"{self.api}/game?id={game_id}").json()
    
    def get_mmo_giveaways(self) -> dict:
        return self.session.get(f"{self.api}/giveaways").json()
    
    def get_latest_mmo_news(self) -> dict:
        return self.session.get(f"{self.api}/latestnews").json()
