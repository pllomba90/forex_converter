### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript? 
JavaScript is:
* scripting language
* no concept of mutable and immutable
* uses curly brackets e.g. {}
* used to build websites and native applications
Python is:
* object-oriented programming language
* has built-in data structures
* ideal for rapid application development
* has mutable and immutable types
* uses indentation in place of brackets
* used for data analytics
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  1. get('c', '3')
  2. setdefault('c', '3')

- What is a unit test?
  A unit test is a test that is designed to test typically a single function or method. They ensure that the code works on the individual function level

- What is an integration test?
  An integration test is a test for multiple components of an application. It ensures that the whole application functions as it should. 

- What is the role of web application framework, like Flask?
    Flask is a framework that is designed to enable someone to create and scale a web application simply and quickly.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  Using the query param is more applicable if you are using a search input in which to capture the query. The route URL is better used when you have a clickable link and using the link as the director to the desired page.

- How do you collect data from a URL placeholder parameter using Flask? 
    In the function decorator you can add the parameter to the route using <someparam> and then the value will be passed to the following function

- How do you collect data from the query string using Flask?
  request.args.get('someplaceholder')

- How do you collect data from the body of the request using Flask?
    request.get_json() if json is being used or
    request.data['someplaceholder']

- What is a cookie and what kinds of things are they commonly used for?
    A cookie is a small text file that is stored on a user's computer or device by a website. Cookies are commonly used to store information about the user or their interactions with the website, which can then be used to personalize their experience or provide additional functionality.

- What is the session object in Flask?
    In Flask, the session object is a way to store data that persists across multiple requests made by the same client. The session object is essentially a dictionary that can be used to store any type of data, such as user IDs, preferences, or shopping cart items.

- What does Flask's `jsonify()` do?
    Flask's jsonify() function is a utility function that returns a JSON response from a Python dictionary. It takes a dictionary as an argument and returns a JSON-encoded response with the appropriate Content-Type header
