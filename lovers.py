from tkinter import *
from collections import Counter


def bi(occurance):
	
	while len(occurance) > 2:
		new_list = []
		i, j = 0, len(occurance) -1

		while i < j:
			new_list.append(occurance[i] + occurance[j])
			i += 1
			j -= 1

		if i == j:
			new_list.append(occurance[i])
		occurance = new_list

	return occurance


def calculate():
	romeo = male.get(1.0, END).strip().lower()
	juliet = female.get(1.0, END).strip().lower()

	if romeo == "":
		percent_label.config(text="NO!")
	elif juliet == "":
		percent_label.config(text="NO!")
	elif romeo == "" and juliet == "":
		percent_label.config(text="NO!")
	else:
		couple = str(romeo + juliet)
		print(f'This is what couple contains: {couple}')
		
		lett_list = Counter(couple)
		print(f'This is what lett_list contains: {lett_list}')
		
		list_only = sorted(lett_list.values(), reverse=True)
		print(f'This is what list_only contains: {list_only}')
		
		digits = bi(list_only)
		
		row_perce = int("".join(map(str, digits)))
		percentage = str(row_perce)

		love_percentage = percentage + "%"
		percent_label.config(text=love_percentage)

#------------------ GUI ---------------------------
root = Tk()
root.geometry("300x350")
root.resizable(False, False)

love_label = Label(root, text="Love Calculator")
love_label.pack(pady=5)

male_label = LabelFrame(root, text="Romeo")
female_label = LabelFrame(root, text="Juliet")

male_label.pack(pady=10)
female_label.pack(pady=10)

male = Text(male_label, width=19, height=1)
female = Text(female_label, width=19, height=1)

male.pack(pady=2, padx=2)
female.pack(pady=2, padx=2)

submit = Button(root, text="Calculate", width=23, height=2, relief="groove", command=calculate)
submit.pack()

result = LabelFrame(root, text="Love Percentage", width=200, height=100, labelanchor="s")
result.pack(pady=15)

percent_label = Label(result, text="100%", font=("Helvatica", 40))
percent_label.pack(pady=10, padx=10)

root.mainloop()
