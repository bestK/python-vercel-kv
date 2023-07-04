import pytest

from vercel_kv import KV


@pytest.mark.asyncio
async def test():
    kv = KV()
    print(kv.has_auth())
    print(kv.set(key="sss", value="asasd"))
    print(kv.get("sss"))
