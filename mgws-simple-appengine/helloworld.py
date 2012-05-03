import webapp2
import json

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      assembly = self.request.get('assembly')
      if assembly == 'A':
        list = [
          {'code': '01', 'label': 'cilinder'},
          {'code': '02', 'label': 'sparkplug'},
          {'code': '03', 'label': 'exhaust'}
        ]
      elif assembly == 'B':
        list = [
          {'code': '11', 'label': 'brake disc'},
          {'code': '12', 'label': 'brake shoe'},
          {'code': '13', 'label': 'ABS'}
        ]
      else:
        list = [
          {'code': '91', 'label': 'undetermined'}
        ]
      output = json.dumps(list , True, indent=4)
      self.response.out.write(output)

class SymptomController(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      assembly = self.request.get('assembly')
      if assembly == 'A':
        list = [
          {'code': 'X1', 'label': 'engine ticks'},
          {'code': 'X2', 'label': 'engine smokes'},
          {'code': 'X3', 'label': 'engine does not start'}
        ]
      elif assembly == 'B':
        list = [
          {'code': 'Y1', 'label': 'brake ticks'},
          {'code': 'Y2', 'label': 'brake smokes'},
          {'code': 'Y3', 'label': 'brake does not work'}
        ]
      else:
        list = [
          {'code': 'Z1', 'label': 'feeling strange'},
          {'code': 'Z2', 'label': 'fuzzy'},
        ]
      output = json.dumps(list , True, indent=4)
      self.response.out.write(output)

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/subassemblies', MainPage),
  ('/symptoms', SymptomController)
  ],
  debug=True)

