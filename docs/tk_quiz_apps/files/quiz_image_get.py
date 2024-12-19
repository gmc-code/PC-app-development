from pygoogle_image import image as pi
import os


quiz_data = {
    "250 GT Berlinetta SWB": "Ferrari",
    "GT40": "Ford",
    "M1": "BMW",
    "DB5": "Aston Martin",
    "Cobra 427": "AC Shelby",
    "Type 57SC Atlantic": "Bugatti",
    "Countach": "Lamborghini",
    "Torpedo": "Tucker",
    "E-Type": "Jaguar",
    "DB4 GT Zagato": "Aston Martin",
    "P1800": "Volvo",
    "Corvette Sting Ray Coupe": "Chevrolet",
    "Skyline GTR R34": "Nissan",
    "DMC-12": "DeLorean",
    "Miata": "Mazda",
    "GTO": "Pontiac",
    "3500 GT Vignale Spyder": "Maserati",
    "Quattro": "Audi",
    "240Z-280Z": "Datsun",
    "959": "Porsche",
    "365GTB/4 Daytona Spyder": "Ferrari",
    "Phantom": "Rolls-Royce",
    "2000GT": "Toyota",
    "2002 Model": "BMW",
    "Cooper": "Mini",
    "F1": "McLaren",
    "Willys": "Jeep",
    "3000": "Austin Healey",
    "Mustang GT350/500": "Ford Shelby",
    "F40": "Ferrari",
    "300 SL": "Mercedes-Benz",
    "Beetle": "Volkswagen",
    "DS": "Citroen",
    "356 Speedster": "Porsche",
    "280SL Roadster": "Mercedes-Benz",
    "250 GTO": "Ferrari",
    "Miura": "Lamborghini",
    "Veyron EB 16.4": "Bugatti",
    "911": "Porsche",
    "Golf": "Volkswagen",
    "Enzo": "Ferrari",
    "LM002": "Lamborghini",
    "Blower": "Bentley",
    "Stratos": "Lancia",
    "288 GTO": "Ferrari",
    "8C Competizione": "Alfa Romeo",
    "S8": "Audi",
    "911 Turbo 3.6": "Porsche",
    "Impreza WRX": "Subaru"
}



# for img_search in quiz_data.keys():
#     img_path = "docs/tk_quiz_apps/files/quiz_images/" # + img_search

#     # creates subdirectory for topic
#     pi.download(keywords=img_search, limit=5, directory=img_path)

for k, v in quiz_data.items():
    img_path = "docs/tk_quiz_apps/files/quiz_images/" # + img_search
    img_search = v + " " + k
    # creates subdirectory for topic
    pi.download(keywords=img_search, limit=2, directory=img_path)
