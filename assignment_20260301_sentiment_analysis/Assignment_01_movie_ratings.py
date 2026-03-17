# Task #1
# Fill you movie choices in this: https://docs.google.com/spreadsheets/d/1951ur7lq5idQWOV16CN1iM0XZMUnoFB_6mKa20nB2os/edit?usp=sharing 
# Give a rating out of 10

# Task #2
# Then, normalize the values for each movie. Convert each person's rating into a unit vector. 
# Compute the doct product of every person against every other.

import numpy as np


def main():
    movie_watchers = np.array(['Sandeep Giri','GK','sneha','Deep','Tanya','Nigam','Supriya','Indu','Simar','Anubhav','Gurpreet'])
    movie_names = np.array(['Matrix','Inception','Harry Potter','Sholay','Titanic','Hangover','Sarfarosh','Joker','Bahubali','Jab We Met'])
    ratings = np.array([[9,7,6.5,6,8,6,7,7,7,6.5],
                        [8,9,8,5,6,8,3,0,4,5],
                        [7,7,5,7,8,5,9,6,7,9],
                        [8,7,9,6,6,8,4,8,6,5],
                        [9,5,9.5,5,5,5,5,5,7.5,7],
                        [6,5,5,9,7,6,7,6,9,9],
                        [8,9,9,5,7,7,7,0,8,8],
                        [6,9,9,5,9,4,4,8,9,6],
                        [6,8,8,9,9,5,9,7.2,9,9],
                        [8,8,8,6,6,6,7,8,8,6],
                        [9,8,7,6,6,6,6,5,9,5]])
    ratings_normalized = ratings / np.linalg.norm(ratings, axis=1)[:, np.newaxis]
    similarity_matrix = np.dot(ratings_normalized, ratings_normalized.T)
    print("Similarity Matrix:")
    print(similarity_matrix)

if __name__ == "__main__":
    main()
