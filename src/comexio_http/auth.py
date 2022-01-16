from aiohttp import ClientSession, ClientResponse
import base64


class Auth:
  """Class to make authenticated requests."""

  def __init__(self, host: str, user_name: str, password: str):
      """Initialize the auth."""
      self.host = host
      self.user_name = user_name
      self.password = password
      self.url = f"http://{self.host}/api"

  async def request(self, params: dict) -> str:
    """Get or set a data point"""

    headers = {
      "authorization": f"Basic {self.encoded_login()}"
    }

    async with ClientSession(read_timeout=5) as client:
      async with client.get(self.url, params=params, headers=headers) as resp:
        resp.raise_for_status()
        return await resp.text()

  def encoded_login(self):
    login = f"{self.user_name}:{self.password}"
    return base64.b64encode(login.encode("utf-8")).decode("ascii")
