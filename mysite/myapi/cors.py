

from django.http import HttpResponse, response
class CorsMiddleware(object):
    def process_response(self, req, resp):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "*" 
        response["Access-Control-Request-Method"] = "*" 
        response["Access-Control-Request-Headers"] = "*" 
        response["Access-Control-Request-Origin"] = "*"
        
        return response
