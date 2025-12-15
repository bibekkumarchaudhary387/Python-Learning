#Daily Challenge: "The ID Checker"
#Scenario: You are managing an event. You have a list of people who registered, and a list of people who actually attended. You want to know who skipped.

#Instructions:
#Create a set registered = {"Alice", "Bob", "Charlie", "David"}.
#Create a set attended = {"Alice", "Charlie"}.
#Use the Difference (-) operator to find who registered but did not attend.
#Print: "The following people missed the event: [Result]".

registered = {"Alice", "Bob", "Charlie", "David"}
attended = {"Alice", "Charlie"}
result = registered - attended
print(f"The following people missed the even {result}")
