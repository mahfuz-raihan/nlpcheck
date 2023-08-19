import requests

url = "https://api.themoviedb.org/3/account/20321801/rated/movies?language=en-US&page=1&sort_by=created_at.asc"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZmQ5OTY5ZDUzNDdhNWYzOWY2ODgzZmZhOTk0MDdhMSIsInN1YiI6IjY0ZTA4N2NmMzcxMDk3MDBhYzQ1MjdhZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.VGMNnyz1WllHEQ_zuZ7WAdpnuuJWTYVWIwFQiJDYCVw"
}

response = requests.get(url, headers=headers)

print(response.text)