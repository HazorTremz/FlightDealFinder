from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

sheet_data = DataManager()
sheet_prices = sheet_data.get_info()
flight_response = FlightSearch()
flight_info = FlightData()
message = NotificationManager()
mail_list = sheet_data.get_emails()
for item in sheet_prices:
    city = item["city"]
    iata_data = flight_response.get_iata(city)
    # sheet_data.update(item["id"],iata_data)
    try:
        travel_data = flight_info.get_flight_details(iata_data)
        ticket_price = travel_data["price"]
    except IndexError:
        continue
    else:

        print(f"{city} : £{ticket_price}")
        if item["lowestPrice"] > ticket_price:
            message.send_message(price=ticket_price, from_iata=travel_data["flyFrom"], to_iata=travel_data["flyTo"],
                                 from_=travel_data["cityFrom"], to_=travel_data["cityTo"],
                                 date_f=travel_data["local_arrival"].split("T")[0],
                                 date_t=travel_data["local_departure"].split("T")[0])
            for emails in mail_list:

                message.send_email(price=ticket_price, from_iata=travel_data["flyFrom"], to_iata=travel_data["flyTo"],
                                   from_=travel_data["cityFrom"], to_=travel_data["cityTo"],
                                   date_f=travel_data["local_arrival"].split("T")[0],
                                   date_t=travel_data["local_departure"].split("T")[0],
                                   mail=emails["email"])

