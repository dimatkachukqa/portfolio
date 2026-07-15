"""
Page Object Class for automating the Index page
defines all the locators and methods to use them through tests
"""

from playwright.sync_api import Page


class IndexPage:
    def __init__(self, page:Page):
        self.page = page

    def header(self):
        return self.page.get_by_role("heading", name="Website for Automation Practice")

    def paragraph(self):
        return self.page.get_by_text("Welcome to my")

    def form_link(self):
        return self.page.get_by_role("link" ,name="Form Page")

    def iframe_link(self):
        return self.page.get_by_role("link" ,name="iframe Page")