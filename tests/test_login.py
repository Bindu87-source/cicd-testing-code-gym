
import pytest
from src.login import LoginSystem


@pytest.fixture
def login_system():
    return LoginSystem()


def test_valid_login(login_system):
    assert login_system.login(
        "admin", "Password123"
    ) == "Login successful"


def test_invalid_password(login_system):
    assert login_system.login(
        "admin", "wrong123"
    ) == "Invalid username or password"


def test_invalid_username(login_system):
    assert login_system.login(
        "unknown", "Password123"
    ) == "Invalid username or password"


def test_empty_username(login_system):
    assert login_system.login(
        "", "Password123"
    ) == "Username and password required"


def test_empty_password(login_system):
    assert login_system.login(
        "admin", ""
    ) == "Username and password required"


def test_account_locks_after_three_failures(login_system):
    login_system.login("admin", "wrong")
    login_system.login("admin", "wrong")

    result = login_system.login("admin", "wrong")

    assert result == "Account locked"


def test_locked_account_cannot_login(login_system):
    for _ in range(3):
        login_system.login("admin", "wrong")

    result = login_system.login("admin", "Password123")

    assert result == "Account locked"


def test_successful_login_resets_failed_attempts(login_system):
    login_system.login("admin", "wrong")
    login_system.login("admin", "Password123")

    assert login_system.failed_attempts["admin"] == 0
