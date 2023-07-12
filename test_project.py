import pytest
from project import RemoteController

@pytest.fixture
def remote():
    return RemoteController()

def test_tv_status(remote):
    assert isinstance(remote.tv_status(), str)

def test_on_off_main(remote):
    assert isinstance(remote.on_off_main(), str)

def test_add_channel(remote):
    channel_name = "Test Channel"
    assert remote.add_channel(channel_name) == f"{channel_name} is added"
    assert channel_name in remote.channels

def test_delete_channel(remote):
    channel = "A-Haber"
    assert remote.delete_channel(channel) == f"Channel {channel} is deleted"
    assert channel not in remote.channels

def test_see_channels(remote):
    assert isinstance(remote.see_channels(), str)





