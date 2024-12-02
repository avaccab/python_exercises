#
# 1)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
#
# NOTE: Don't use any built-in functions!

def dictionary_maker(list_of_tuples):
    my_dictionary = {}
    for tuple in list_of_tuples:
        my_dictionary[tuple[0]]=tuple[1]
    
    return my_dictionary
# Commented code
# list_of_tuples = [('foo', 1), ('bar', 3)]
# print(type(list_of_tuples))
# print(list_of_tuples)
# print(dictionary_maker(list_of_tuples))

############################################
############################################
#
# You are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'foo', 'jobs': ['bar', 'baz', 'qux']}
#
# we will refer to this as a "CV".
#
############################################
############################################



#
# 2)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

def has_experience_as(list_of_cvs, job_tittle):
    usernames = []
    for cv in list_of_cvs:
        for job in cv["jobs"]:
            if job == job_tittle:
                usernames.append(cv["user"])
    return usernames


# Commented code
# list_of_cvs=[{ 'user': 'foo', 'jobs': ['bar', 'baz', 'qux']}]
# print(has_experience_as(list_of_cvs,'it'))

#
# 3)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def job_counts(list_of_cvs):
    dictionary = {}
    for cv in list_of_cvs:
        for job in cv["jobs"]:
            if job in dictionary:
                dictionary[job] = dictionary[job]+1
            else:
                dictionary[job] = 1
    return dictionary

# Commented code
# list_of_cvs = [{'user': 'foo', 'jobs': ['data monkey', 'copyist', 'wrecking ball operator']},
#            {'user': 'bar', 'jobs': ['wrecking ball operator', 'poet']},
#            {'user': 'baz', 'jobs': ['dancer', 'waitstaff']},
#            {'user': 'qux', 'jobs': ['wrecking ball operator', 'waitstaff']}]
# print(job_counts(list_of_cvs))


#
# 4)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.

def most_popular_job(list_of_cvs):
    dictionary = job_counts(list_of_cvs)
    list_of_items = dictionary.items()
    most_popular_count = 0
    most_popular_job = ""
    for item in list_of_items:
        if item[1] > most_popular_count:
            most_popular_job = item[0]
            most_popular_count = item[1]
    return(most_popular_job, most_popular_count)

# Commented code
# list_of_cvs = [{'user': 'foo', 'jobs': ['data monkey', 'copyist', 'wrecking ball operator']},
#            {'user': 'bar', 'jobs': ['wrecking ball operator', 'poet']},
#            {'user': 'baz', 'jobs': ['dancer', 'waitstaff']},
#            {'user': 'qux', 'jobs': ['wrecking ball operator', 'waitstaff']}]
# print(most_popular_job(list_of_cvs))


############################################
############################################
# Scoreboard
#
# In this part we will pretend
# we have an imaginary arcade
# game and we need to keep track
# of users and their scores on
# each level.
#
# You will create:
# 1. A class "User" with some methods.
# 2. Some separate functions that
#    use the User class.
#
############################################
############################################


#
# 5)
# Create a class called "User"
#
# The class should be instantiated
# with one attribute: "name"
# which is a string.
# 
#
# 6)
# Add methods "add_score" and
# "get_scores" to the User class.
#
# "add_score" should store the user's
# score for a given level. The choice
# of how to store it is up to you,
# but each user can have multiple
# scores for each level.
#
# "add_score" should have parameters:
# 1. level (str)
# 2. score (int)
# and should return nothing.
#
# "get_scores" should have one parameter:
# 1. level (str)
# and should return a list of integers
# representing the scores the user
# has achieved for that level
#

# Commented code
# class User:
#     def __init__(self, name: str) -> None:  # class constructor
#         self.name = name


class User:
    scores = []
    def __init__(self, name: str) -> None:  # class constructor
        self.name = name
       

    def add_score(self, level: str, score: int) -> None:  # class method

        if isinstance(score, int) and score>0:
            self.scores.append((level, score))
        else:
            raise Exception("Given score is not an integer or is negative")

    def get_scores(self, level):
        list_of_integers = []
        for score in self.scores:
            list_of_integers.append(score[1])
        return list_of_integers
    
    def top_score(self, level: str):
        scores_of_level = [score[1] for score in self.scores if score[0]==level]
        if len(scores_of_level)==0:
            return None
        else:
            return max(scores_of_level)
""" 
user = User('foo')
user.add_score('bar', 100)
user.add_score('bar', 250)
print(user.top_score('baz'))
     """

#
# 7)
# Modify the "add_score" method
# so that it throws an error if the
# "score" it is given is not an integer
# or is negative.
#
#
#
# 8)
# Create a "top_score" method
# that has one parameter: "level"
# and returns the user's top score
# for that level.
#
# If the user has no score for that
# level, the method should return None


#
# 9)
# Now create a separate function
# called "top_player" that has two
# parameters:
# 1. a list of User objects
# 2. a level (str)
#
# And returns a tuple with the following
# form: (str, int) where the values
# represent: (player_name, score)


#
# 10)
# Now modify the function "top_player"
# so that it returns None if given a level
# that no player has played


#
# 11)
# Create a separate function
# called "best_scores".
#
# This function should have one
# parameter: a list of User objects
# and should return a list of tuples
# of the following form:
# (str, str, int)
# where the values represent:
# (level, player_name, score)
#
# The list should be sorted with
# the top score coming first
# and should be truncated to the
# top 3 scores.
#
# HINT: use the builtin "sorted"
# function to sort a list and
# look how to use key-functions:
# https://docs.python.org/3/howto/sorting.html
