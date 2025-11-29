#The Challenge: "The Variable Swap" Scenario: You have two variables. a holds milk, b holds tea. You want to swap them so a holds tea and b holds milk.

glass_a = "Milk"
glass_b = "Tea"

print("Glass A contains: " + glass_a)
print("Glass B contains: " + glass_b)

# --- YOUR CODE GOES HERE ---
# Logic: How do you switch the contents? 
# Hint: You might need a third empty glass (variable).
glass_empty = glass_a
glass_a = glass_b
glass_b = glass_empty


print("Glass A contains: " + glass_a) # Should say Tea
print("Glass B contains: " + glass_b) # Should say Milk