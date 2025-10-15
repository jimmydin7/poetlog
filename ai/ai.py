import http.client

conn = http.client.HTTPSConnection("ai.hackclub.com")

payload = "{\"messages\":[{\"content\":\"Tell me a joke!\",\"role\":\"user\"}]}"

headers = { 'Content-Type': "application/json" }

conn.request("POST", "/chat/completions", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))