"""
Simple collapsable xBlock with editable title and content.
Made as a test task.
"""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope, String


class TestXBlock(XBlock):
    """
    The block shows a collapsable div with editable title and content.
    Title and content are passed to view as context and are edited
    inside students_view method.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0,
        scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    title = String(
        default="Here be the title!",
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

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    # @XBlock.json_handler
    # def increment_count(self, data, suffix=''):
    #     """
    #     An example handler, which increments the data.
    #     """
    #     # Just to show data coming in...
    #     assert data['hello'] == 'world'
    #
    #     self.count += 1
    #     return {"count": self.count}

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
