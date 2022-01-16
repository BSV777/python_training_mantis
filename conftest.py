import pytest
from fixture.application import Application
import json
import os.path
from fixture.db import DBFixture
import ftputil


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request, config):
    global fixture
    #web_config = config['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(config=config)
    web_admin = config['webadmin']
    fixture.session.ensure_login(username=web_admin["username"], password=web_admin["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DBFixture(host=db_config['host'], name=db_config['name'],
                          user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def configure_server(request, config):
    install_server_configurator(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])

    def fin():
        restore_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
    request.addfinalizer(fin)


def install_server_configurator(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config/config_inc.php.bak"):
            remote.remove("config/config_inc.php.bak")
        if remote.path.isfile("config/config_inc.php"):
            remote.rename("config/config_inc.php", "config/config_inc.php.bak")
        remote.upload(os.path.join(os.path.dirname(__file__), "resources/config_inc.php"), "config/config_inc.php")


def restore_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config/config_inc.php.bak"):
            if remote.path.isfile("config/config_inc.php"):
                remote.remove("config/config_inc.php")
            remote.rename("config/config_inc.php.bak", "config/config_inc.php")
