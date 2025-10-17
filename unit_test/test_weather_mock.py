from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from weather import WeatherService

def test_get_temperature_with_mocking_monkeypatch(
    monkeypatch:pytest.MonkeyPatch
) -> None:
    def fake_get(url:str, params:dict[str,Any]) -> Any:
        mock_response = MagicMock()  # MagicMock allows you to set up an object with different kinds of methods, properties and responses in any way
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "current":{
                "temp_c":27}
        }
        return mock_response
    
    monkeypatch.setattr("httpx.get", fake_get)
    service = WeatherService(api_key="fake-key")
    temp = service.get_temperature("Singapore")
    assert temp == 27

    # MagicMock 的作用是创建一个“魔法模拟对象”，它可以模拟任何 Python 对象的行为。
    # 在本例中，mock_response = MagicMock() 创建了一个假的响应对象（模拟 httpx.get 的返回值）。
    # 通过设置 mock_response.raise_for_status.return_value = None，
    # 我们让 raise_for_status() 方法在被调用时什么都不做（不会抛出异常）。
    # 通过 mock_response.json.return_value = {...}，
    # 我们让 json() 方法在被调用时返回指定的字典数据（模拟真实 API 返回的数据结构）。
    # 这样就可以在不发起真实网络请求的情况下，测试 WeatherService.get_temperature 的逻辑。


# magicmock 的优点还有 assertions

def test_get_temperature_with_mocking_patch() -> None:
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "current":{
            "temp_c":27}
    }
    # 这里没有使用fake_get，而是使用patch，patch是一个context manager 可以模拟任何对象，包括httpx.get
    with patch("httpx.get", return_value=mock_response) as mock_get: # 这里指出来httpx.get被mock了，返回值是mock_response
        service = WeatherService(api_key="fake-key")
        temp = service.get_temperature("Beijing")
        assert temp == 27
        mock_get.assert_awaited_once()