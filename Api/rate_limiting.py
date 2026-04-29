import redis
from rest_framework.exceptions import Throttled


redis_client=redis.StrictRedis(host="localhost",port="6379",decode_responses=True)

def rate_limits(Max_request : int , Window_time : int):
  def decorator(func):

    def wrapper(self,request,*args,**kwargs):
     client_id=request.user.id if request.user.is_authenticated else request.META.get('REMOTE_ADDR')

     endpoint_path=request.path

     redis_key=f"rate_limit:{client_id}:{endpoint_path}"

     current_request=redis_client.get(redis_key)

    #  if user is new never access this url set request 1
     if current_request is None:
       redis_client.set(redis_key, 1 ,ex=Window_time)
     elif int (current_request) < Max_request:
       redis_client.incr(redis_key)
     else:
       retry_after=redis_client.ttl(redis_key)
       raise Throttled(detail=f"Rate Limited Exceed Try Agin after {retry_after} sec")  

     return func(self,request,*args,**kwargs) 
    
    return wrapper
  return decorator
       
  

