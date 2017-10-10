import six
import pytest

from sixpackage.util import my_universal_function


@pytest.mark.skipif(not six.PY2,
                    reason="Requires python2")
def test_sixpackage_my_universal_function_py2():
    assert my_universal_function() == u'This is a unicode string'


@pytest.mark.skipif(not six.PY3,
                    reason="Requires python3")
def test_sixpackage_my_universal_function_py3():
    assert my_universal_function() == 'This is a unicode string'
