def main(request, response):
    response.headers.set("Content-Security-Policy", "default-src * 'unsafe-inline'")
    response.headers.set("X-Content-Security-Policy", "default-src * 'unsafe-inline'")
    response.headers.set("X-WebKit-CSP", "default-src * 'unsafe-inline'")
    return """<!DOCTYPE html>
<!--
Copyright (c) 2013 Intel Corporation.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of works must retain the original copyright notice, this list
  of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the original copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of Intel Corporation nor the names of its contributors
  may be used to endorse or promote products derived from this work without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Authors:
        Hao, Yunfei <yunfeix.hao@intel.com>

-->

<html>
  <head>
    <title>CSP Test: csp_default-src_asterisk_script</title>
    <link rel="author" title="Intel" href="http://www.intel.com"/>
    <link rel="help" href="http://www.w3.org/TR/2012/CR-CSP-20121115/#default-src"/>
    <meta name="flags" content=""/>
    <meta name="assert" content="default-src * 'unsafe-inline'"/>
    <meta charset="utf-8"/>
    <script src="../resources/testharness.js"></script>
    <script src="../resources/testharnessreport.js"></script>
    <script src="../resources/server.js?pipe=sub"></script>
    <script src="support/csp.js"></script>
    <script id="test"></script>
    <script>
        document.getElementById("test").src = "http://" + __SERVER__NAME + ":" + __CORS__PORT + "/tests/csp/support/test.js";
    </script>
  </head>
  <body>
    <div id="log"></div>
    <script>
      var t1 = async_test(document.title + "_allowed_int");
      var t2 = async_test(document.title + "_allowed_ext");
      function runTest() {
        t1.step(function() {
            assert_true(typeof X == "number", "attribute defined internal");
        }, document.title + "_allowed_int");
        t1.done();
        t2.step(function() {

            assert_true(typeof getVideoURI == "function", "Function getVideoURI is defined");
        }, document.title + "_allowed_ext");
        t2.done();
      }
      setTimeout(runTest,1000);
    </script>
  </body>
</html> """
