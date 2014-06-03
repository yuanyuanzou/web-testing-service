def main(request, response):
    import simplejson as json
    f = file('config.json')
    source = f.read()
    s = json.JSONDecoder().decode(source)
    url1 = "http://" + s['host'] + ":" + str(s['ports']['http'][1])
    url2 = "http://" + s['host'] + ":" + str(s['ports']['http'][0])
    _CSP = "script-src 'self' 'unsafe-inline'"
    response.headers.set("Content-Security-Policy", _CSP)
    response.headers.set("X-Content-Security-Policy", _CSP)
    response.headers.set("X-WebKit-CSP", _CSP)
    return """<!DOCTYPE html>
<html>
        <head>
                <title>CSP Test: script-src 'self' 'unsafe-inline'</title>
                <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
                <meta description="Content-Security-Policy Test: script-src 'self' 'unsafe-inline'" />
                <link rel="author" title="bhill@paypal-inc.com" />
                <script src="../../resources/testharness.js"></script>
                <script src="../../resources/testharnessreport.js"></script>
                <script src="CSP_passTest001.py"></script>
        </head>
        <body>
                <div id=log></div>
        </body>
        <!--
                This test demonstrates how to test something that shouldn't happen, or
                fail when something that should happend doesn't.  Use script with
		conditional execution based on the policy being tested to set a variable,
		then use script we know will execute by policy to check if it is set.
		
		Some limitations on this approach, obviously, if policy enforcement is
		very broken - when we can't count on any script to execute - but this
		is a start, at least.
	-->	

        <script>
		test(function() {assert_true(false)}, "assert_true with false from unsafe inline script");
	</script>
</html> """
