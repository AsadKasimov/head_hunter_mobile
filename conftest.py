import pytest


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import hh_ru_mobile.utils.selene.patch_selector_strategy  # noqa
    import hh_ru_mobile.utils.selene.patch_element_mobile_commands  # noqa
