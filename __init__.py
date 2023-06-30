import os
from typing import Optional

import requests
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class KVConfig(BaseModel):
    url: str
    rest_api_url: str
    rest_api_token: str
    rest_api_read_only_token: str


class Opts(BaseModel):
    ex: Optional[int]
    px: Optional[int]
    exat: None
    pxat: None
    keepTtl: None


class KV:
    """
    wapper for https://vercel.com/docs/storage/vercel-kv/rest-api
    """

    def __init__(self, kv_config: Optional[KVConfig] = None):
        if kv_config is None:
            self.kv_config = KVConfig(
                url=os.getenv("VERCEL_KV_URL"),
                rest_api_url=os.getenv("VERCEL_KV_REST_API_URL"),
                rest_api_token=os.getenv("VERCEL_KV_REST_API_TOKEN"),
                rest_api_read_only_token=os.getenv(
                    "VERCEL_KV_REST_API_READ_ONLY_TOKEN"
                ),
            )
        else:
            self.kv_config = kv_config

    def get_kv_conf(self) -> KVConfig:
        return self.kv_config

    def has_auth(self) -> bool:
        kv_config = KV.get_kv_conf()
        headers = {
            'Authorization': f'Bearer {self.kv_config.rest_api_token}',
        }
        resp = requests.get(self.kv_config.rest_api_url, headers=headers)
        return resp.json()['error'] != 'Unauthorized'

    def set(self, key, value, opts: Optional[Opts] = None) -> bool:
        headers = {
            'Authorization': f'Bearer {self.kv_config.rest_api_token}',
        }

        url = f'{self.kv_config.rest_api_url}/set/{key}/{value}'

        if opts is not None and opts.ex is not None:
            url = f'{url}/ex/{opts.ex}'

        resp = requests.get(url, headers=headers)
        return resp.json()['result']

    def get(self, key) -> bool:
        headers = {
            'Authorization': f'Bearer {self.kv_config.rest_api_token}',
        }

        resp = requests.get(f'{self.kv_config.rest_api_url}/get/{key}', headers=headers)
        return resp.json()['result']
