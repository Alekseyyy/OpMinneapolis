
# Simple analysis script of minneapolis piggy passwords
# By Aleksey [github.com/Alekseyyy]

import math, csv
import matplotlib as mpl
import matplotlib.pyplot as plt

def common_passwords(password):
	common_passwords = (
	    "123456",
	    "123456789",
	    "qwerty",
	    "password",
	    "111111",
	    "12345678",
	    "abc123",
	    "1234567",
	    "password1",
	    "12345"
	)

	if password in str(common_passwords):
		return True
	return False

def compute_password_entropy(password):
	unique_chars = len(set(password))
	len_chars = len(list(password))

	return math.log2(unique_chars**len_chars)

# Get the data ready
formatted_passwords = dict()
with open("police_emails_passwords.txt", newline='') as password_txt:
	csv_passwords = csv.reader(password_txt, delimiter='\t')

	for k in csv_passwords:
		try:
			formatted_passwords[k[0]] = k[1]
		except:
			pass

# Do Statistics
## Are the pigs using the top 10 common passwords?

common_passwords_count = 0
for n, k in formatted_passwords.items():
	if common_passwords(k):
		common_passwords_count += 1

print ("At least", common_passwords_count, "pigs are computer illiterate.")

## What is the Shannon entropy (and thus the strength) of the pigs passwords?

shannon_entropy_list = []
for n, k in formatted_passwords.items():
	shannon_entropy_list.append(compute_password_entropy(k))

## Graph the Shannon entropy distribution on bar graph.

shannon_entropy_graph_cat = {"ur password really fucking sux": 0,
				"ur password really sux": 0,
				"ur password kinda sux": 0,
				"ur password is okay": 0,
				"ur password is actually good!": 0
}

for n in shannon_entropy_list:
	if n < 28:
		shannon_entropy_graph_cat["ur password really fucking sux"] += 1
	elif n >= 28 and n < 35:
		shannon_entropy_graph_cat["ur password really sux"] += 1
	elif n >= 35 and n < 59:
		shannon_entropy_graph_cat["ur password kinda sux"] += 1
	elif n >= 59 and n < 127:
		shannon_entropy_graph_cat["ur password is okay"] += 1
	elif n >= 127:
		shannon_entropy_graph_cat["ur password is actually good!"] += 1

print (shannon_entropy_graph_cat)

fig = plt.figure()

plt.bar(range(len(shannon_entropy_graph_cat)), shannon_entropy_graph_cat.values(), align='center')
plt.xticks(range(len(shannon_entropy_graph_cat)), list(shannon_entropy_graph_cat.keys()))

plt.title("Scientific Proof that Police are Dumb", fontsize=16)
plt.xlabel("Password Category", fontsize=14)
plt.ylabel("Frequency", fontsize=14)

plt.show()
