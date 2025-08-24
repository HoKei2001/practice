from weather import WeatherService
import pytest
from typing import Any

def test_get_temperature_success(monkeypatch:pytest.MonkeyPatch):
    def fake_get(url:str, params:dict[str,Any]) -> Any:
        class FakeResponse:
            def raise_for_status(self):
                pass
            def json(self):
                return {
                    "current":{
                        "temp_c": 30}
                }
        return FakeResponse()
    
    # 这里的 setttattr 是 pytest 提供的 monkeypatch 工具的方法，用于临时替换模块或对象的属性。
    # 具体来说，monkeypatch.setattr("httpx.get", fake_get) 的作用是把 httpx.get 这个函数替换成 fake_get，
    # 这样在测试期间，所有对 httpx.get 的调用都会变成调用 fake_get，从而避免真实的网络请求。
    monkeypatch.setattr("httpx.get", fake_get)
    service = WeatherService(api_key="fake-key")
    temp = service.get_temperature("Singapore")
    assert temp == 30

"""
hokei@CHINAMI-9OGE83F:~/project/practice/unit_test$ uv run pytest
========================================== test session starts ===========================================
platform linux -- Python 3.12.11, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/hokei/project/practice
configfile: pyproject.toml
plugins: anyio-4.10.0
collected 1 item                                                                                         

test_weather_patch.py .                                                                            [100%]
"""
# 即使我并没有配置环境变量，测试也能通过，因为测试用例中用到了 monkeypatch 工具，
# 它允许我们临时替换模块或对象的属性，从而实现对真实依赖的隔离。
# 这种用 fake 数据（伪造数据）替换真实依赖（如 httpx.get）的做法就是 monkey patching。
# 在单元测试中，monkey patching 可以让我们隔离外部依赖（如网络请求、数据库等），
# 只关注我们要测试的函数或类的逻辑是否正确。
# 这样测试既快又稳定，也不会因为外部服务不可用而失败。
