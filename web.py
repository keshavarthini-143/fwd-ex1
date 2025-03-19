from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
    <title>Marks Table</title>
</head>
<body>

    <h2>Student Marks</h2>
    <table border="1">
        <tr>
            <th>Name</th>
            <th>Subject</th>
            <th>Marks</th>
        </tr>
        <tr>
            <td>Abi</td>
            <td>Math</td>
            <td>85</td>
        </tr>
        <tr>
            <td>Arun</td>
            <td>Science</td>
            <td>90</td>
        </tr>
        <tr>
            <td>Anu</td>
            <td>English</td>
            <td>78</td>
        </tr>
    </table>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',80)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()