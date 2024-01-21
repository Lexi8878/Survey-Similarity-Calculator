# -*- coding: utf-8 -*-
# SFU Favourite Spots Similarity Counter - Matches you with the first person that has the highest score 

# Open the file 
file = open("sfu_best_cmpt120.csv") 

# Get rid of the first line 
junk = file.readline() 

# Get your list of answers 
my_favourites = ["Starbucks", "Noodle Waffle Cafe", "Uncle Fatih's", "Guadalupe (MBC)", "Chopped Leaf\n"] 

# Initialize the similarity scores 
similarity_score = 0 
similarity_score_old = 0
similarity_score_highest = 0

# For every line of data in the file, starting from the second line 
for data in file: 
    
    # Split the lines of data into lists 
    datalist = data.split(",")  

    # Go through all of your favourite SFU spots in your list 
    for favourite in my_favourites:
     
        # If they have the same favourite spot at SFU in their list 
        if favourite in datalist:   
                 
            # Add to the general similarity score 
            similarity_score += 1 
            
            # Store the number of same spots in another variable 
            similarity_score_old += similarity_score
            
            # Reset the general similarity score back to zero 
            similarity_score = 0
            
    # If the number of same spots is greater than the last  
    if similarity_score_old > similarity_score_highest: 
                    
        # Replace it with the new highest score 
        similarity_score_highest = similarity_score_old 
                
        # If new one greater, get the name of the person 
        name = datalist[1] 
                
        # Reset the similarity score back to zero 
        similarity_score_old = 0 
            
        # Update the name and score of the person with the highest similarity score so far  
        print("So far, " + name + " has the highest score of " + str(similarity_score_highest) + " with you!")
          
    # If the number of same spots is the same or less than the last  
    elif similarity_score_old <= similarity_score_highest: 
                
        # Keep the original highest score the same 
        similarity_score_highest == similarity_score_highest 
   
        # Reset the similarity score back to zero 
        similarity_score_old = 0 
   
# Print who has the final highest similarity score as you 
print(name + " has the highest final similarity score of " + str(similarity_score_highest) + " with you!")           

# Close the file 
file.close() 
