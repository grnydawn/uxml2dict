from microapp import MicroappProject

import os

here = os.path.dirname(os.path.abspath(__file__))

data = """
<mydocument has='an attribute'>
  <and>
    <many>elements</many>
    <many>more elements</many>
  </and>
  <plus a='complex'>
    element as well
  </plus>
</mydocument>
"""


def test_basic(capsys):

    prj = MicroappProject()
    cmd = "uxml2dict \"%s\" -p" % data

    ret, fwds = prj.run_command(cmd)

    assert ret == 0
    captured = capsys.readouterr()
    assert captured.out.startswith("OrderedDict")
    assert captured.err == ""
