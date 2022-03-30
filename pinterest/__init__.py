import requests
import random
import time

bookmark = "22Y2JVSG81V2sxcmNHRlpWM1J5VFVaU1YxcEhSbFJTYTNBd1ZGWmtSMVV3TVZkV1dHaFhVa1ZLVkZreU1WSmtNREZXVm14d1RrMXRhRkJXYlhCSFkyMVJlRlZZWkdGU1ZGWnlWRlZTVjAxR1dYbE5TR2hWVFZWd1IxWXlOVk5XVjBwSFUyNXNZVlpXY0ROV01GcExaRWRXUjJOSGVHaGxiRmwzVm10YWIyUXlSWGxTYTJScVUwWktWbFpyVlRGVU1WWnlWbTVLYkdKR1NscFpNR1F3WVZaYWRHVkdiRlpOYWtaNlYxWmFZVkl5VGtsVmJHaHBVbXR3TmxkWGVGWk5WMDVYWVROd1lWSlViRmhVVldSNlpVWmFSMWt6YUZWTmExcElXVEJhVjFadFJuUmhSbHBhVmtWYWFGWXhXbmRqYkVwVllrWkdWbFpFUVRWYWExcFhVMWRLTmxWdGVGTk5XRUpIVmxSSmVHTXhVbk5UV0doWVltdEtWbGxyWkZOVVJteFdWbFJHV0ZKck5UQlVWbVJIVmpGS2NtTkVRbGRTUlZwVVdUSnpNVlpyT1ZaV2JGSllVMFZLVWxadGRHRlNhekZYVld4YVlWSnJjSE5WYkZKWFUxWlZlVTFJYUZWaVJuQkhWbTF3VjFkSFNrZFRhMDVoVmpOTk1WVXdXa3RrUjBaR1RsZDRhRTFJUWpSV2Frb3dWVEZKZVZKc1pHcFNiRnBYVm10YVMxVldWbkphUms1cVlrWktNRmt3Vmt0aVIwWTJVbTVvVm1KR1NrUldNbk40WTJzeFJWSnNWbWhoTTBKUlYxZDRWbVZIVWtkWGJrWm9VbXhhYjFSV1duZFhiR1IwWkVWYVVGWnJTbE5WUmxGNFQwVXhObFpVVmxwTmEydDVWRlZTY2sxck5WVmhlazVhWWxaRk1WUlhjRTVOVm14WVVsUkdUbEl3YkRSVVZsSkhZVEExTmxKdGJFOVdSbXcwVjFaU1ZrMUdjRWhTV0doaFVrWkZlVlJ0Y0ZkaVZteFlWbTE0VG1Gck1IaFhWekZHWlZVMVZWVnRiRkJXTUZwdlZHNXdiMkZWTVhWbFJUbFRWbTFSTkdaRVNYbE9SRkV4V1hwck5VNTZaek5aTWtwdFRrZFJkMDlFVVROWmFtZDRXbFJqZWsweVNYaGFha3B0VFcxTk1sbFVVVE5PUjBWNFdYcFplazFFUVRCT1IwcHJXVzFOTkZsdFdUTmFSMWt5VGtSSmQxcHFaRGhVYTFaWVprRTlQUT09fFVIbzVhMkZFV1RSVE1sWnJUREF4Y1ZSVU1XWk9NVGgwVFZoM01VMTZXbXhOZWxreFdrUmpORnBxVW1wUFYwa3dUbnBvYTFsVVRtbFBSMGwzV20xR2FVNTZXVEZhYW14b1dtcEtiVTVIVlRKTk1rMHdUVlJSTVUweVNURk9WMVY1VGtkRk5GcFhSVEpaTWtWNlRucEpNV1pGTlVaV00zYzl8Nzk1YTQ2N2JiZjIwNDQ5NTdlOTJlZTY0YmZmMjQyZGEyZDRjMTVlNTg2MzBjNzNhNTAxMmNhNmRlNWIwMzcwYnxORVd8"


def get_image(query):
    content = requests.get(
        "https://id.pinterest.com/resource/BaseSearchResource/get/?source_url=%2Fsearch%2Fpins%2F%3Frs%3Dtyped%26q%3D"
        + query
        + "&data=%7B%22options%22%3A%7B%22article%22%3A%22%22%2C%22appliedProductFilters%22%3A%22---%22%2C%22query%22%3A%22"
        + query
        + "%22%2C%22scope%22%3A%22pins%22%2C%22top_pin_id%22%3A%22%22%2C%22filters%22%3A%22%22%2C%22bookmarks%22%3A%5B%"
        + bookmark
        + "%22%5D%2C%22no_fetch_context_on_resource%22%3Atrue%7D%2C%22context%22%3A%7B%7D%7D&_="
        + str(int(time.time()))
    ).json()
    source = content["resource_response"]["data"]["results"]
    image = [
        {
            "small": image["images"]["236x"]["url"],
            "high": image["images"]["orig"]["url"],
        }
        for image in source[1:]
    ]
    random.shuffle(image)
    return image
