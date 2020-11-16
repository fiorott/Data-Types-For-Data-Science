# Tuples are commonly created by zipping lists together with zip ()
#Two lists: us_cookies, in_coockies
us_cookies = ['chocolate', 'banana']
in_cookies = ['mangoo','avocado']
top_pairs = list(zip(us_cookies, in_cookies))
print(top_pairs)

#Also called tuple expansion
# Allow to assign the elements of a tuple to named variables for later use.

us_num_1, in_num_1 = top_pairs[0]
print(us_num_1)
print(in_num_1)

#Unpacking in Loops

# Here is a for Loop that uses unpacking when iterating over the top_pairs list.
# It splits each tuple in the list into its Indian and US Cookie elements.
# We then use each od these variables to print the cookies in order.

for us_cookie, in_cookie in top_pairs:
    print(in_cookie)
    print(us_cookie)

#Enumerating Options

# Know the index of a element in the iterable
# The function (method actually) enumerate() help us to return "index-value" pairs while looping.
# We can use this to track rankings in our data or skip elements we are not interested in.



