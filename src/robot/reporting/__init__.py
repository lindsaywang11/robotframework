#  Copyright 2008-2013 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""Implements report, log, output XML, and xUnit file generation.

The public API of this package is the :class:`~.ResultWriter` class. It
can write result files based on XML output files on the file system,
as well as based on the result objects returned by
the :func:`~robot.result.resultbuilder.ExecutionResult` factory method or
an executed :class:`~robot.running.model.TestSuite`.

It is highly recommended to use the public API via the :mod:`robot.api`
package like in the example below::

    from robot.api import ResultWriter

    writer = ResultWriter('output.xml')
    writer.write_results(report='my_report.hml', log=None, xunit='xunit.xml')

This package is considered stable.
"""

from .resultwriter import ResultWriter
