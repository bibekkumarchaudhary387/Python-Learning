#Task A: The Student Profile Create a dictionary called student with keys: name, score, and subject. Print a formatted sentence: "Alex scored 95 in Math".

student = {
	"name": "Bibek",
	"score": 99,
	"subject": "DSA"
	}
print(f"{student.get("name")} scored {student.get("score")} in {student.get("subject")}")
