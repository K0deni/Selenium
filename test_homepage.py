##New selenium simple test project##
import time
import pytest
from pom.homepage_nav import HomepageNav
@pytest.mark.usefixtures('setup')

class TestHomepage:
    
    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actuall_links = homepage_nav.get_element_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert actuall_links == expected_links, 'Validation Nav Links text'
        homepage_nav.get_nav_link_by_name('Home').click()
        time.sleep(5)
        