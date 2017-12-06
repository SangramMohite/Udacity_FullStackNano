#!/usr/bin/env python3
#
# Test script for BookmarksServer.py

import http.server
import requests
from urllib.parse import unquote, parse_qs

memory = {}

form = """
<!DOCTYPE html>
<title>Bookmark Server</title>
<form method="POST">
    <label>Long URI:
        <input name="longuri">
    </label>
    <br>
    <label>Short name:
        <input name="shortname">
    </label>
    <br>
    <button type="submit">Save it!</button>
</form>
<p>URIs I know about:
<pre>
{}
</pre>
"""

def CheckURI(uri, timeout = 5):
	try:
		request = requests.get(uri, timeout=timeout)
		return request.status_code == 200
	except requests.RequestException:
		return False

class Shortener(http.server.BaseHTTPRequestHandler):
	def do_GET(self):

		name = unquote(self.path[1:])
		
		if name:
			if name in memory:
				self.send_response(303)
				self.send_header('Location', memory[name])
				self.end_headers()
			else:
				self.send_response(404)
				self.send_header('Content-type', 'text/html; charset=utf-8')
				self.end_headers()
				self.wfile.write("short Name does not exist".encode())
				return
		else:
			self.send_response(200)
			self.send_header('Content-type', 'text/html; charset=utf-8')
			self.end_headers()
			shortnames = "\n".join("<a href={} target=\"_blank\">{}</a>:	{}".format(
				memory[key], key, memory[key])
			for key in sorted(memory.keys()))
			self.wfile.write(form.format(shortnames).encode())

	def do_POST(self):		
		#get the params
		length = int(self.headers.get('Content-Length', 0))
		body = self.rfile.read(length).decode()
		params = parse_qs(body)

		longuri_text_constant = "longuri"
		shortname_text_constant = "shortname"

		#check if all params are present
		if longuri_text_constant not in params or shortname_text_constant not in params:
			self.send_response(400)
			self.send_header('Content-type', 'text/html; charset=utf-8')
			self.end_headers()
			self.wfile.write("Missing Form Fields".encode())
			return

		# read the params
		longuri = params[longuri_text_constant][0]
		shortname = params[shortname_text_constant][0]

		# check if long uri is a valid uri
		if CheckURI(longuri):
			# check if shortname already exists and add to the memory
			if (shortname not in memory):				
				print ("Shortname not foind")
				print (memory)
				memory[shortname] = longuri
			else:				
				self.send_response(400)
				self.send_header('Content-type', 'text/html; charset=utf-8')
				self.end_headers()
				self.wfile.write(("Shortname already used for {}".format(memory[shortname])).encode())
				return
		else:
			#raise exceptipon
			self.send_response(404)
			self.send_header('Content-type', 'text/html; charset=utf-8')
			self.end_headers()
			self.wfile.write(("Invalid URI {}".format(longuri)).encode())
			return

		# redirect to the get request 
		self.send_response(303)
		self.send_header('Location', '/')
		self.end_headers()


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, Shortener)
    httpd.serve_forever()