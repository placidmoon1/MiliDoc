import requests

def makeRequest(path, method, headers=None, data=None):
  """
    Makes a request to the specified URL.

    :param path: The full path of the request.
    :param method: The HTTP method for the request.
    :param headers: A dictionary o
  """
  if (method == "GET"):
    response_data = requests.get("https://milidoc.web.app" + path)
    print("status code:", response_data.status_code)
    print("headers:", response_data.headers)
    print("text:", response_data.text)
      
  if (method == "POST"):
    response_data = requests.post("https://milidoc.web.app" + path, 
          data = data).json()

if __name__ == "__main__":
  makeRequest("/", "GET")