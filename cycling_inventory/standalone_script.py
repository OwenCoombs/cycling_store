import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "cycling_inventory.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW


from cycling_inv_app.models import Vehicle, Customer, CustomerOrder





# Function to display menu options
def display_menu():
    print("1. Add Vehicle")  # Option to add a new vehicle
    print("2. Update Vehicle")  
    print("3. Delete Vehicle")  
    print("4. Show All Vehicles")  
    print("5. Exit") 

# Function to create a new vehicle object and add it to the database
def create_vehicle(type, number_in_stock):
    vehicle = Vehicle.objects.create(type=type, number_in_stock=number_in_stock)
    print("Vehicle added successfully.")
    return vehicle

# Function to add a new vehicle
def add_vehicle():
    type = input("Enter vehicle type (unicycle, bicycle, tricycle): ")  # choose which type
    number_in_stock = int(input("Enter number in stock: "))  # how much in stock
    create_vehicle(type, number_in_stock)  #call create vehicle

# Function to update an existing vehicle
def update_vehicle():
    vehicle_id = int(input("Enter vehicle ID to update: "))  # input ID of the vehicle to update
    vehicle = Vehicle.objects.get(id=vehicle_id)  # Retrieve the vehicle object from the database
    type = input("Enter new vehicle type (leave blank to keep current): ")  # new vehicle type
    number_in_stock = input("Enter new number in stock (leave blank to keep current): ")  # amount of stock
    if type:
        vehicle.type = type  # Update vehicle type if user provided a new type
    if number_in_stock:
        vehicle.number_in_stock = number_in_stock  # Update stock number if user provided a new number
    vehicle.save()  # Save the changes to the vehicle object
    print(f"Vehicle with ID {vehicle_id} updated successfully.")  # print msg

# Function to delete an existing vehicle
def delete_vehicle():
    vehicle_id = int(input("Enter vehicle ID to delete: "))  # id to delete
    vehicle = Vehicle.objects.get(id=vehicle_id)  # grabbing vehicle from data
    vehicle.delete()  # deletes vehicle
    print(f"Vehicle with ID {vehicle_id} deleted successfully.")  # conf msg

# Function to show all vehicles stored in the database
def show_all_vehicles():
    vehicles = Vehicle.objects.all()  # Retrieve all vehicle objects from the database
    if vehicles:
        print("All Vehicles:")  # list of vehicles
        for vehicle in vehicles:
            print(f"ID: {vehicle.id}, Type: {vehicle.type}, Stock: {vehicle.number_in_stock}")  # details of veh
    else:
        print("No vehicles found.")  # not found

# Main function to run the program
def main():
    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ")  # Prompt user to enter their choice
        if choice == '1':
            add_vehicle()  # Call add_vehicle function if user chooses option 1
        elif choice == '2':
            update_vehicle()  # Call update_vehicle function if user chooses option 2
        elif choice == '3':
            delete_vehicle()  # Call delete_vehicle function if user chooses option 3
        elif choice == '4':
            show_all_vehicles()  # Call show_all_vehicles function if user chooses option 4
        elif choice == '5':
            break  # Exit the program if user chooses option 5
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")  # Print error message for invalid choices

if __name__ == "__main__":
    main()  # Call the main function to start the program






