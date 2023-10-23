import pandas as pd

people = {
    "first_name": ["Michael", "Michael", 'Jane', 'John'], 
    "last_name": ["Jackson", "Jordan", 'Doe', 'Doe'], 
    "email": ["mjackson@email.com", "mjordan@email.com", 'JaneDoe@email.com', 'JohnDoe@email.com'],
    "birthday": ["29.09.1958", "17.02.1963", "15.03.1978", "12.05.1979"],
    "height": [1.75, 1.98, 1.64, 1.8]
}
df = pd.DataFrame(people)

df.head()