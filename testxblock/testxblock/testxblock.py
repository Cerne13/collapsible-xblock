"""
Simple collapsable xBlock with editable title and content.
Made as a test task.
"""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, String


class TestXBlock(XBlock):
    title = String(
        default="The titliest title ever",
        scope=Scope.content,
        help="Block header title"
    )

    content = String(
        default="Just add some text content here.",
        scope=Scope.content,
        help="Block text content"
    )

    editable_fields = ("title", "content")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        html = self.resource_string("static/html/testxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/testxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/testxblock.js"))
        frag.initialize_js('TestXBlock')
        return frag

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("TestXBlock",
             """<testxblock/>
             """),
            ("Multiple TestXBlock",
             """<vertical_demo>
                <testxblock/>
                <testxblock/>
                <testxblock/>
                </vertical_demo>
             """),
        ]
