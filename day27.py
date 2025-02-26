# Day 27
# Exercise 3

# Kaun Banega Crorepati
# Create a program which shows the questions to the player like kbc
# Use list data type to store the questions and correct answers
# Display the final amount which the winner is taking home
import time

questions = [
    ("What is the capital of India?", ["Mumbai", "Delhi", "Nagpur" , "Kolkata"] , "B" ,1000),
    ("Which is the national bird of India?",["Eagle", "KingFisher", "Great Indian Bustard", "Peacock"], "D" , 5000),
    ("Which planet is known as the 'Red Planet'?", ["Mars", "Venus", "Jupiter", "Saturn"], "A", 10000),
    ("Who wrote the Indian national anthem?", ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Subramania Bharati", "Sarojini Naidu"], "A", 20000),
    ("Which festival is known as the 'Festival of Lights'?", ["Holi", "Navratri", "Diwali", "Eid"], "C", 50000),
    ("What is the chemical symbol for Gold?", ["Ag", "Au", "Pb", "Fe"], "B", 100000),
    ("Which Mughal Emperor built the Taj Mahal?", ["Akbar", "Babur", "Shah Jahan", "Aurangzeb"], "C", 200000),
    ("Who was the first Indian to travel in space?", ["Kalpana Chawla", "Rakesh Sharma", "Sunita Williams", "Vikram Sarabhai"], "B", 500000),
    ("What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond", "Platinum"], "C", 1000000),
    ("Which country won the FIFA World Cup in 2018?", ["Brazil", "Germany", "France", "Argentina"], "C", 3000000),
    ("Which scientist developed the Theory of Relativity?", ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"], "B", 5000000),
    ("Who was the first President of independent India?", ["Jawaharlal Nehru", "Dr. Rajendra Prasad", "Sardar Patel", "Dr. B.R. Ambedkar"], "B", 10000000),
    ("What is the square root of 625?", ["15", "20", "25", "30"], "C", 50000000),
    ("Who was the first person to climb Mount Everest?", ["Edmund Hillary", "Tenzing Norgay", "George Mallory", "Reinhold Messner"], "A", 70000000)
]

print("\n Swagat hai aapka kaun banega Crorepati me!!!")
print("Aapse 14 prashna puche jaynege jinke sahi jawab dene par aap utni he dhanrashi kamayiega!")
print("To tyar hai aap")
print(f"Press Enter to start the game....")

for i,(questions,options,correct_answers,prize) in enumerate(questions):
    print(f"\n🔹First question is {i+1} for ₹{prize}:")
    print(f"Q: {questions}")

# Options printing
    print("A",options[0])
    print("B",options[1])
    print("C",options[2])
    print("D",options[3])

    answer = input("Your answer (A, B, C, D): ").strip().upper()

    if answer == correct_answers:
        total_prize = prize
        print(f"Jeet gaye aap ₹{prize}")
    else:
        print(f"Maaf Kijiye manyavar aapka uttar galat hai sahi uttar hai {correct_answers}")
        print(f"Khel ko yahi samapt karna hoga aapne jeete hai ₹{total_prize}")
        break

    # Time rendering for 1 sec
    time.sleep(1)

    print("Mubarakho ! 🙌")