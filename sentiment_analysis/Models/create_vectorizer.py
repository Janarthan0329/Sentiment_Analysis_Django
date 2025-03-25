import pickle

# Assuming 'cv' is your CountVectorizer object
cv = ...  # Initialize or load your CountVectorizer object here

# Save the CountVectorizer object to a pickle file
pickle.dump(cv, open('countVectorizer.pkl', 'wb')) 