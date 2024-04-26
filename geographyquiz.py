#Starting Question/Prompt
print("""Welcome to the Geography Quiz!
You will be asked questions. Some questions are:

    "What is the capital of Canada?"
    "Where is the Taj Mahal Located?"
    
The answer for those two questions are:

    "Ottawa"
    "India"
    
  You can capitalize or put symbols (like periods, hyphens, etc.) in your answer.
  When you're giving the place of a important location, put the country, not the city or state.
If your answer matches 80% or higher the actual answer, then it will be considered right.
You can have 1 redemption question at the end of the quiz if you get something wrong.
For every question you get right, you earn 4 points, and for every redemption question you get right, you earn 2 points.
You will have 10 questions, and I will tell how many points you have along the way. 
Good Luck! """)

questions = {
    "What is the Capital of Argentina?": "Buenos Aires",
    "What is the Capital of Australia?": "Canberra",
    "What is the Capital of Brazil?": "Brasília",
    "What is the Capital of Canada?": "Ottawa",
    "What is the Capital of China?": "Beijing",
    "What is the Capital of Egypt?": "Cairo",
    "What is the Capital of France?": "Paris",
    "What is the Capital of Germany?": "Berlin",
    "What is the Capital of India?": "New Delhi",
    "What is the Capital of Indonesia?": "Jakarta",
    "What is the Capital of Iran?": "Tehran",
    "What is the Capital of Italy?": "Rome",
    "What is the Capital of Japan?": "Tokyo",
    "What is the Capital of Mexico?": "Mexico City",
    "What is the Capital of Netherlands?": "Amsterdam",
    "What is the Capital of Nigeria?": "Abuja",
    "What is the Capital of Pakistan?": "Islamabad",
    "What is the Capital of Philippines?": "Manila",
    "What is the Capital of Poland?": "Warsaw",
    "What is the Capital of Russia?": "Moscow",
    "What is the Capital of Saudi Arabia?": "Riyadh",
    "What is the Capital of South Africa?": "",
    "What is the Capital of South Korea?": "Seoul",
    "What is the Capital of Spain?": "Madrid",
    "What is the Capital of Sweden?": "Stockholm",
    "What is the Capital of Thailand?": "Bangkok",
    "What is the Capital of Turkey?": "Ankara",
    "What is the Capital of United Kingdom?": "London",
    "What is the Capital of United States?": "Washington, D.C.",
    "What is the Capital of Vietnam?": "Hanoi",
    "Where is the Taj Mahal located?": "India",
    "Where is the Eiffel Tower located?": "France",
    "Where is the Great Wall of China located?": "China",
    "Where is the Statue of Liberty located?": "United States",
    "Where is Machu Picchu located?": "Peru",
    "Where is the Pyramids of Giza located?": "Egypt",
    "Where is the Colosseum located?": "Italy",
    "Where is the Petra located?": "Jordan",
    "Where is the Christ the Redeemer located?": "Brazil",
    "Where is the Sydney Opera House located?": "Australia",
    "Where is the Angkor Wat located?": "Cambodia",
    "Where is the Acropolis of Athens located?": "Greece",
    "Where is Stonehenge located?": "United Kingdom",
    "Where is the Sagrada Familia located?": "Spain",
    "Where is the Burj Khalifa located?": "United Arab Emirates",
    "Where is Mount Rushmore located?": "United States",
    "Where is the Kremlin located?": "Russia",
    "Where is the Neuschwanstein Castle located?": "Germany",
    "Where is Chichen Itza located?": "Mexico",
    "Where is the Moai Statues of Easter Island located?": "Chile"
}
