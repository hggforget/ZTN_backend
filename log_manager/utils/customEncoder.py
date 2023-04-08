import datetime
import json



class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
      if isinstance(obj, datetime.datetime):
        print("MyEncoder-datetime.datetime")
        return obj.strftime("%Y-%m-%d %H:%M:%S")
      if isinstance(obj, bytes):
        return str(obj, encoding='utf-8')
      if isinstance(obj, int):
        return int(obj)
      elif isinstance(obj, float):
        return float(obj)
      # elif isinstance(obj, array):
      #    return obj.tolist()
      else:
        return super(CustomEncoder, self).default(obj)