import requests
import json
import math


response =requests.get("https://jobs.github.com/positions.json")
print(response.status_code)

print(response.json())



for i in range(1,226):
    print(i , end = "100 ")
    print(i-126)

{'message': 'success' }


def jprint(obj):
    text = json.dumps(obj,sort_keys=True, indent =4)
    print(text)

jprint(response.json())

{"message" : "success"
   }

parameters = {
    "description": "github",
     "location" : "New York",
       "lat" : 40.71,
        "long" : -74

}





# def data_items(description,location,lat,long,full_time):
#     description = "python"
#     location = " New York"
#     full_time = True





#    print(description + " " + location + " " + lat + " " + long + " " + full_time)



#data_items("description", "location", " lat", "long" , " full_time")

def job_title(data_analytics,software_architect,software_eng,technology):
    print(" ")


#data_items("description", "location", "lat", "long","full_time")

