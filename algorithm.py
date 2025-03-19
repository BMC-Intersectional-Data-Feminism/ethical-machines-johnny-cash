import urban_planning 
import random 
# Example algorithm: Always picks the non-vehicle option
def always_pick_non_vehicle(option1, option2):
    """This algorithm always picks the non-vehicle if possible.
    It will return first the picked option and second the non-chosen option. """
    
    if option1[0] in urban_planning.all_non_vehicles: ## Check if option 1 is a non-vehicle, if so, pick that. 
        return option1, option2
    elif option2[0] in urban_planning.all_non_vehicles:  ## If option 1 is not a non-vehicle, check if option 2 is. If so, pick that. 
        return option2, option1
    else:
        return option1, option2  # Default to first option if both are vehicles

# Student function placeholder
def student_algorithm(option1, option2): 

    # pedestrians go first 

    if option1[0] in urban_planning.non_vehicles['Pedestrian']: 

        return option1, option2 

    elif option2[0] in urban_planning.non_vehicles['Pedestrian']: 

        return option2, option1 

    # transit goes next 

    elif option1[0] in urban_planning.vehicles['Public Transport']: 

        return option1, option2 

    elif option2[0] in urban_planning.vehicles['Public Transport']: 

        return option2, option1 

    # emergency  

    elif option1[0] in urban_planning.vehicles['Emergency Vehicle']: 

        return option1, option2 

    elif option2[0] in urban_planning.vehicles['Emergency Vehicle']: 

        return option2, option1 

    # animals go last (they aren't in a rush) 

    elif option1[0] in urban_planning.non_vehicles['Animal']: 

        return option2, option1 

    elif option2[0] in urban_planning.non_vehicles['Animal']: 

        return option1, option2 

    # whoever is there first 

    else: 

        return option1, option2 

# Function to run the simulation using a given algorithm
# Run the activity
#urban_planning.run_activity()

# Run the activity using the example algorithm
print("\n🔹 Running Our Algorithm: Pedestrians, Public Transit, Emergency 🔹")
urban_planning.run_activity(num_scenarios=25, decision_function = student_algorithm)

#print("\n🔹 Now it's your turn! Modify 'student_algorithm' and run again. 🔹")
