from typing import Any


class RequestLoggingmMiddleware:
      
      def __init__(self,get_response) -> None:
            self.get_response = get_response
            
      def __call__(self,request) -> Any:
            # request_info = request
            # print(vars(request_info))
            # print(self.get_response(request))
            
            return self.get_response(request)