#Importing the google search api client
import googleapiclient

from googleapiclient.discovery import build
#these are the api and cse_id issued for google developers to create custom search engines.
digital_footprint_api_key = "AIzaSyDZy7rJtaiXbvGpspDRN0PnWiULCSiygMU"
digital_footprint_cse_id = "002218691429702604885:xs3xwythtf4"

#defining search term, this can be anything
web_search = "Caroline Muthambiri"

#using build method to define digital footprint search function
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

#printing out the results 
print google_search(web_search, digital_footprint_api_key, digital_footprint_cse_id)
