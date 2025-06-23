import streamlit as st
import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# --- Expanded Quiz Questions ---
quiz_questions = [
    {"q": "Which is heavier: 1 kg of steel or 1 kg of cotton?", "options": ["Steel", "Cotton", "Equal", "Depends on size"], "ans": "Equal"},
    {"q": "A plane crashes on the border of India and Nepal. Where do they bury the survivors?", "options": ["India", "Nepal", "Both", "Nowhere"], "ans": "Nowhere"},
    {"q": "What comes once in a minute, twice in a moment, but never in a thousand years?", "options": ["Time", "Letter M", "Memory", "Air"], "ans": "Letter M"},
    {"q": "If you throw a red stone into the blue sea, what will it become?", "options": ["Pink", "Sank", "Wet", "Invisible"], "ans": "Wet"},
    {"q": "Which month has 28 days?", "options": ["February", "None", "All", "April"], "ans": "All"},
    {"q": "How many animals did Moses take on the ark?", "options": ["2", "7", "None", "Moses didn’t"], "ans": "Moses didn’t"},
    {"q": "What starts and ends with 'E' but contains only one letter?", "options": ["Envelope", "Eagle", "Eye", "Edge"], "ans": "Envelope"},
    {"q": "You see a boat filled with people, yet there isn’t a single person on board. How?", "options": ["They’re ghosts", "They’re under deck", "They’re married", "It’s invisible"], "ans": "They’re married"},
    {"q": "If a doctor gives you 3 pills and tells you to take one every 30 minutes, how long will they last?", "options": ["90 mins", "60 mins", "30 mins", "2 hrs"], "ans": "60 mins"},
    {"q": "How many times can you subtract 5 from 25?", "options": ["5", "Infinite", "1", "None"], "ans": "1"},
    {"q": "What has keys but can’t open locks?", "options": ["Piano", "Map", "Locksmith", "Door"], "ans": "Piano"},
    {"q": "What is always coming but never arrives?", "options": ["Tomorrow", "Yesterday", "Today", "Now"], "ans": "Tomorrow"},
    {"q": "If you have me, you want to share me. If you share me, you don’t have me. What am I?", "options": ["Secret", "Money", "Love", "Knowledge"], "ans": "Secret"},
    # Add more if you want
]
# Add these to your existing quiz_questions list
additional_quiz_questions = [
    {"q": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Perth"], "ans": "Canberra"},
    {"q": "Which planet is closest to the Sun?", "options": ["Venus", "Earth", "Mars", "Mercury"], "ans": "Mercury"},
    {"q": "Who painted the Mona Lisa?", "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"], "ans": "Leonardo da Vinci"},
    {"q": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Fe", "Gd"], "ans": "Au"},
    {"q": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Thailand", "Japan", "South Korea"], "ans": "Japan"},
    {"q": "What is the largest organ in the human body?", "options": ["Heart", "Liver", "Brain", "Skin"], "ans": "Skin"},
    {"q": "Which of these is NOT a primary color?", "options": ["Red", "Blue", "Green", "Yellow"], "ans": "Green"},
    {"q": "Who wrote 'Romeo and Juliet'?", "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "ans": "William Shakespeare"},
    {"q": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Platinum"], "ans": "Diamond"},
    {"q": "Which country gifted the Statue of Liberty to the United States?", "options": ["England", "France", "Spain", "Italy"], "ans": "France"},
    {"q": "What is the smallest prime number?", "options": ["0", "1", "2", "3"], "ans": "2"},
    {"q": "Which gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "ans": "Carbon Dioxide"},
    {"q": "Which of these animals is NOT a mammal?", "options": ["Dolphin", "Bat", "Penguin", "Elephant"], "ans": "Penguin"},
    {"q": "What is the main component of the Sun?", "options": ["Liquid Lava", "Molten Iron", "Hydrogen Gas", "Solid Rock"], "ans": "Hydrogen Gas"},
    {"q": "Which famous scientist developed the theory of relativity?", "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"], "ans": "Albert Einstein"},
    {"q": "What is the national flower of India?", "options": ["Rose", "Lotus", "Sunflower", "Lily"], "ans": "Lotus"},
    {"q": "Which of these is NOT a continent?", "options": ["Australia", "Antarctica", "Greenland", "Africa"], "ans": "Greenland"},
    {"q": "Who invented the telephone?", "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Guglielmo Marconi"], "ans": "Alexander Graham Bell"},
    {"q": "What is the largest species of shark?", "options": ["Great White Shark", "Hammerhead Shark", "Whale Shark", "Tiger Shark"], "ans": "Whale Shark"},
    {"q": "Which of these countries is NOT in Africa?", "options": ["Egypt", "Nigeria", "Pakistan", "Kenya"], "ans": "Pakistan"},
    {"q": "What is the tallest mountain in the world?", "options": ["K2", "Mount Everest", "Kangchenjunga", "Makalu"], "ans": "Mount Everest"},
    {"q": "Which instrument has 88 keys?", "options": ["Guitar", "Violin", "Piano", "Flute"], "ans": "Piano"},
    {"q": "What is the most abundant element in the Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "ans": "Nitrogen"},
    {"q": "Who discovered penicillin?", "options": ["Louis Pasteur", "Alexander Fleming", "Marie Curie", "Joseph Lister"], "ans": "Alexander Fleming"},
    {"q": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "ans": "Pacific Ocean"},
    {"q": "Which of these is NOT a type of cloud?", "options": ["Cumulus", "Stratus", "Nimbus", "Celsius"], "ans": "Celsius"},
    {"q": "What is the capital of Japan?", "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"], "ans": "Tokyo"},
    {"q": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Mercury"], "ans": "Mars"},
    {"q": "What is the chemical formula for water?", "options": ["CO2", "H2O", "O2", "N2"], "ans": "H2O"},
    {"q": "Which famous Indian leader was known as 'Mahatma'?", "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "Subhas Chandra Bose"], "ans": "Mahatma Gandhi"},
    {"q": "What is the largest species of big cat?", "options": ["Lion", "Leopard", "Jaguar", "Tiger"], "ans": "Tiger"},
    {"q": "Which planet has the most moons?", "options": ["Jupiter", "Saturn", "Uranus", "Neptune"], "ans": "Saturn"},
    {"q": "What is the smallest bone in the human body?", "options": ["Stapes", "Femur", "Tibia", "Radius"], "ans": "Stapes"},
    {"q": "Which of these is NOT a programming language?", "options": ["Java", "Python", "Cobra", "Crocodile"], "ans": "Crocodile"},
    {"q": "What is the main gas that makes up the Sun?", "options": ["Helium", "Hydrogen", "Oxygen", "Nitrogen"], "ans": "Hydrogen"},
    {"q": "Which of these animals can fly?", "options": ["Penguin", "Ostrich", "Emu", "Bat"], "ans": "Bat"},
    {"q": "What is the name of the biggest desert in the world?", "options": ["Gobi Desert", "Sahara Desert", "Arabian Desert", "Antarctic Desert"], "ans": "Antarctic Desert"},
    {"q": "Which of these is NOT a noble gas?", "options": ["Helium", "Neon", "Argon", "Hydrogen"], "ans": "Hydrogen"},
    {"q": "Who was the first woman to win a Nobel Prize?", "options": ["Mother Teresa", "Marie Curie", "Rosalind Franklin", "Dorothy Hodgkin"], "ans": "Marie Curie"},
    {"q": "Which blood type is known as the universal donor?", "options": ["A+", "B+", "AB+", "O-"], "ans": "O-"},
]

# Brain teasers
brain_teasers = [
    {"q": "I'm light as a feather, but even the strongest person can't hold me for more than a few minutes. What am I?", "options": ["Breath", "Thought", "Feather", "Air"], "ans": "Breath"},
    {"q": "What has a head, a tail, but no body?", "options": ["Snake", "Coin", "Arrow", "Kite"], "ans": "Coin"},
    {"q": "What gets wetter as it dries?", "options": ["Sponge", "Towel", "Hair", "Clothes"], "ans": "Towel"},
    {"q": "What has keys but no locks, space but no room, and you can enter but not go in?", "options": ["House", "Car", "Keyboard", "Mind"], "ans": "Keyboard"},
    {"q": "What can travel around the world while staying in a corner?", "options": ["Light", "Sound", "Stamp", "Wind"], "ans": "Stamp"},
    {"q": "What has many teeth but cannot bite?", "options": ["Comb", "Zipper", "Saw", "Fork"], "ans": "Comb"},
    {"q": "What has a neck but no head?", "options": ["Shirt", "Bottle", "River", "Giraffe"], "ans": "Bottle"},
    {"q": "What can you catch but not throw?", "options": ["Ball", "Cold", "Butterfly", "Fish"], "ans": "Cold"},
    {"q": "What has hands but cannot clap?", "options": ["Gloves", "Clock", "Monkey", "Robot"], "ans": "Clock"},
    {"q": "What has legs but cannot walk?", "options": ["Chair", "Table", "Bed", "All of these"], "ans": "All of these"},
]

# Science questions
science_questions = [
    {"q": "Which gas makes up the majority of Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "ans": "Nitrogen"},
    {"q": "What is the process by which plants make their own food called?", "options": ["Photosynthesis", "Respiration", "Digestion", "Fermentation"], "ans": "Photosynthesis"},
    {"q": "Which of these is NOT a state of matter?", "options": ["Solid", "Liquid", "Gas", "Energy"], "ans": "Energy"},
    {"q": "What is the smallest unit of matter?", "options": ["Atom", "Molecule", "Cell", "Electron"], "ans": "Atom"},
    {"q": "Which of these is NOT a type of rock?", "options": ["Igneous", "Sedimentary", "Metamorphic", "Metallic"], "ans": "Metallic"},
    {"q": "What is the process called when a solid changes directly to a gas?", "options": ["Melting", "Freezing", "Sublimation", "Condensation"], "ans": "Sublimation"},
    {"q": "Which vitamin is produced when your skin is exposed to sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "ans": "Vitamin D"},
    {"q": "What is the name of the force that pulls objects toward Earth?", "options": ["Magnetic force", "Nuclear force", "Gravity", "Friction"], "ans": "Gravity"},
    {"q": "Which of these animals is cold-blooded?", "options": ["Dog", "Cat", "Snake", "Human"], "ans": "Snake"},
    {"q": "What is the name of the process by which water changes from liquid to gas?", "options": ["Condensation", "Evaporation", "Precipitation", "Sublimation"], "ans": "Evaporation"},
]

# History questions
history_questions = [
    {"q": "Who was the first Prime Minister of India?", "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "Dr. Rajendra Prasad"], "ans": "Jawaharlal Nehru"},
    {"q": "Which year did World War II end?", "options": ["1943", "1945", "1947", "1950"], "ans": "1945"},
    {"q": "Who discovered America?", "options": ["Vasco da Gama", "Christopher Columbus", "Ferdinand Magellan", "James Cook"], "ans": "Christopher Columbus"},
    {"q": "Who was the first person to step on the Moon?", "options": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "John Glenn"], "ans": "Neil Armstrong"},
    {"q": "Which ancient civilization built the pyramids?", "options": ["Greek", "Roman", "Egyptian", "Mesopotamian"], "ans": "Egyptian"},
    {"q": "Who wrote the Indian national anthem?", "options": ["Rabindranath Tagore", "Bankim Chandra Chattopadhyay", "Sarojini Naidu", "Mahatma Gandhi"], "ans": "Rabindranath Tagore"},
    {"q": "Which famous Indian emperor converted to Buddhism?", "options": ["Chandragupta Maurya", "Ashoka", "Akbar", "Shivaji"], "ans": "Ashoka"},
    {"q": "When did India gain independence from British rule?", "options": ["1945", "1947", "1950", "1952"], "ans": "1947"},
    {"q": "Who invented the light bulb?", "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Albert Einstein"], "ans": "Thomas Edison"},
    {"q": "Which Indian leader is known as the 'Iron Man of India'?", "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Vallabhbhai Patel", "Subhas Chandra Bose"], "ans": "Sardar Vallabhbhai Patel"},
]

# --- Expanded Bonus True/False Questions ---
tf_questions = [
    {"q": "Can a man legally marry his widow’s sister? (yes/no)", "ans": "no"},
    {"q": "Is it possible to lift an elephant with one hand? (yes/no)", "ans": "yes"},
    {"q": "Is it correct to say 'The yolk of the egg are white'? (yes/no)", "ans": "no"},
    {"q": "Is it possible for a square to have 3 sides? (yes/no)", "ans": "no"},
    {"q": "Can you spell 'cow' in thirteen letters? (yes/no)", "ans": "yes"},
    {"q": "Does a leap year occur every 4 years? (yes/no)", "ans": "yes"},
    {"q": "Is water made of hydrogen and oxygen? (yes/no)", "ans": "yes"},
    {"q": "Can humans breathe underwater without equipment? (yes/no)", "ans": "no"},
    {"q": "The sun rises from the west. (yes/no)", "ans": "no"},
    {"q": "Lightning never strikes the same place twice. (yes/no)", "ans": "no"},
]
# Add these to your existing tf_questions list
additional_tf_questions = [
    {"q": "The Great Wall of China is visible from the Moon. (yes/no)", "ans": "no"},
    {"q": "A group of crows is called a murder. (yes/no)", "ans": "yes"},
    {"q": "Humans have 206 bones in their body. (yes/no)", "ans": "yes"},
    {"q": "Sharks are mammals. (yes/no)", "ans": "no"},
    {"q": "The capital of India is Mumbai. (yes/no)", "ans": "no"},
    {"q": "Mount Everest is the tallest mountain in the world. (yes/no)", "ans": "yes"},
    {"q": "The chemical symbol for silver is Si. (yes/no)", "ans": "no"},
    {"q": "Sound travels faster in water than in air. (yes/no)", "ans": "yes"},
    {"q": "The Earth has only one natural satellite. (yes/no)", "ans": "yes"},
    {"q": "The human brain stops growing after age 18. (yes/no)", "ans": "no"},
    {"q": "Goldfish have a memory span of only 3 seconds. (yes/no)", "ans": "no"},
    {"q": "Chameleons change color to match their surroundings. (yes/no)", "ans": "no"},
    {"q": "The Pacific Ocean is the largest ocean on Earth. (yes/no)", "ans": "yes"},
    {"q": "A tomato is a vegetable. (yes/no)", "ans": "no"},
    {"q": "The Statue of Liberty was a gift from France. (yes/no)", "ans": "yes"},
    {"q": "Pluto is still classified as a planet. (yes/no)", "ans": "no"},
    {"q": "The human eye can distinguish between approximately 10 million different colors. (yes/no)", "ans": "yes"},
    {"q": "Bats are blind. (yes/no)", "ans": "no"},
    {"q": "The currency of Japan is the Yuan. (yes/no)", "ans": "no"},
    {"q": "Spiders are insects. (yes/no)", "ans": "no"},
    {"q": "The heart is the largest muscle in the human body. (yes/no)", "ans": "no"},
    {"q": "Dolphins are fish. (yes/no)", "ans": "no"},
    {"q": "The Amazon River is the longest river in the world. (yes/no)", "ans": "no"},
    {"q": "Vitamin C prevents the common cold. (yes/no)", "ans": "no"},
    {"q": "Water boils at 100 degrees Celsius at sea level. (yes/no)", "ans": "yes"},
    {"q": "The Sahara Desert is the largest desert in the world. (yes/no)", "ans": "no"},
    {"q": "A day on Venus is longer than a year on Venus. (yes/no)", "ans": "yes"},
    {"q": "Humans share 50% of their DNA with bananas. (yes/no)", "ans": "yes"},
    {"q": "The Great Barrier Reef is the largest living structure on Earth. (yes/no)", "ans": "yes"},
    {"q": "An octopus has three hearts. (yes/no)", "ans": "yes"},
]

# Science true/false
science_tf = [
    {"q": "Atoms are mostly empty space. (yes/no)", "ans": "yes"},
    {"q": "The sun is a star. (yes/no)", "ans": "yes"},
    {"q": "Lightning never strikes the same place twice. (yes/no)", "ans": "no"},
    {"q": "Humans use only 10% of their brains. (yes/no)", "ans": "no"},
    {"q": "The Earth is perfectly round. (yes/no)", "ans": "no"},
    {"q": "All plants perform photosynthesis. (yes/no)", "ans": "no"},
    {"q": "Blood in your veins is blue. (yes/no)", "ans": "no"},
    {"q": "The human body has four lungs. (yes/no)", "ans": "no"},
    {"q": "Diamonds are made from compressed coal. (yes/no)", "ans": "no"},
    {"q": "The speed of light is the fastest speed possible. (yes/no)", "ans": "yes"},
]


# --- Expanded Math Challenge Puzzles ---
math_puzzles = [
    {
        "question": "I am a number. If you multiply me by 3 and add 12, the result is 42. What am I?",
        "answer": 10,
        "explanation": "Let the number be x. Then 3x + 12 = 42 → 3x = 30 → x = 10."
    },
    {
        "question": "Find the next number: 2, 4, 8, 16, ?",
        "answer": 32,
        "explanation": "Each number doubles: 2 × 2=4, 4 × 2=8, 8 × 2=16, so next is 16 × 2=32."
    },
    {
        "question": "If 3 apples cost 15 rupees, how much do 5 apples cost?",
        "answer": 25,
        "explanation": "Cost per apple = 15 / 3 = 5 rupees; so 5 apples cost 5 × 5 = 25 rupees."
    },
    {
        "question": "Calculate the area of a rectangle with length 7 and width 4.",
        "answer": 28,
        "explanation": "Area = length × width = 7 × 4 = 28."
    },
    {
        "question": "Solve for x: 2x + 3 = 11.",
        "answer": 4,
        "explanation": "2x + 3 = 11 → 2x = 8 → x = 4."
    },
    {
        "question": "What is the square root of 144?",
        "answer": 12,
        "explanation": "Square root of 144 is 12."
    },
    {
        "question": "If a car travels 60 km in 1.5 hours, what is its average speed?",
        "answer": 40,
        "explanation": "Speed = Distance / Time = 60 / 1.5 = 40 km/h."
    },
    {
        "question": "What is 15% of 200?",
        "answer": 30,
        "explanation": "15% of 200 = 0.15 × 200 = 30."
    },
    {
        "question": "A train travels 120 km in 2 hours. What is its speed in km/hr?",
        "answer": 60,
        "explanation": "Speed = Distance / Time = 120 / 2 = 60 km/hr."
    },
]
# Add these to your existing math_puzzles list
additional_math_puzzles = [
    {
        "question": "If 2x + 5 = 15, what is the value of x?",
        "answer": 5,
        "explanation": "2x + 5 = 15 → 2x = 10 → x = 5."
    },
    {
        "question": "What is the value of 3² + 4²?",
        "answer": 25,
        "explanation": "3² + 4² = 9 + 16 = 25."
    },
    {
        "question": "If a rectangle has a length of 8 cm and a width of 5 cm, what is its perimeter?",
        "answer": 26,
        "explanation": "Perimeter = 2 × (length + width) = 2 × (8 + 5) = 2 × 13 = 26 cm."
    },
    {
        "question": "What is 20% of 150?",
        "answer": 30,
        "explanation": "20% of 150 = 0.2 × 150 = 30."
    },
    {
        "question": "If a shirt costs ₹800 after a 20% discount, what was the original price?",
        "answer": 1000,
        "explanation": "If x is the original price, then x - 0.2x = 800. Solving: 0.8x = 800, so x = 800/0.8 = 1000."
    },
    {
        "question": "Find the next number in the sequence: 3, 6, 12, 24, ?",
        "answer": 48,
        "explanation": "Each number is doubled to get the next number: 3 × 2 = 6, 6 × 2 = 12, 12 × 2 = 24, 24 × 2 = 48."
    },
    {
        "question": "If the average of five numbers is 15, what is their sum?",
        "answer": 75,
        "explanation": "If the average is 15, then the sum divided by 5 is 15. So the sum = 15 × 5 = 75."
    },
    {
        "question": "A car travels at 60 km/h. How far will it travel in 2.5 hours?",
        "answer": 150,
        "explanation": "Distance = Speed × Time = 60 × 2.5 = 150 km."
    },
    {
        "question": "If 3/4 of a number is 18, what is the number?",
        "answer": 24,
        "explanation": "Let the number be x. Then 3/4 × x = 18. Solving: x = 18 ÷ (3/4) = 18 × (4/3) = 24."
    },
    {
        "question": "What is the value of 5! ÷ 3! ?",
        "answer": 20,
        "explanation": "5! = 5 × 4 × 3 × 2 × 1 = 120. 3! = 3 × 2 × 1 = 6. So 5! ÷ 3! = 120 ÷ 6 = 20."
    },
    {
        "question": "If the radius of a circle is 7 cm, what is its area? (Use π = 22/7)",
        "answer": 154,
        "explanation": "Area = πr² = (22/7) × 7² = (22/7) × 49 = 22 × 7 = 154 cm²."
    },
    {
        "question": "Solve for x: 3x - 7 = 8",
        "answer": 5,
        "explanation": "3x - 7 = 8 → 3x = 15 → x = 5."
    },
    {
        "question": "What is the sum of the first 10 natural numbers?",
        "answer": 55,
        "explanation": "Sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55."
    },
    {
        "question": "If a triangle has angles of 30° and 60°, what is the measure of the third angle?",
        "answer": 90,
        "explanation": "Sum of angles in a triangle = 180°. So the third angle = 180° - 30° - 60° = 90°."
    },
    {
        "question": "What is the value of √(9 × 16)?",
        "answer": 12,
        "explanation": "√(9 × 16) = √144 = 12."
    },
    {
        "question": "If 5 workers can build a wall in 12 days, how many days will it take 3 workers to build the same wall?",
        "answer": 20,
        "explanation": "Workers × days = constant. So 5 × 12 = 3 × days → days = (5 × 12) / 3 = 20 days."
    },
    {
        "question": "What is the LCM of 12 and 18?",
        "answer": 36,
        "explanation": "12 = 2² × 3, 18 = 2 × 3². LCM = 2² × 3² = 4 × 9 = 36."
    },
    {
        "question": "If the cost price of an article is ₹400 and the profit is 15%, what is the selling price?",
        "answer": 460,
        "explanation": "Selling price = Cost price + Profit = 400 + 15% of 400 = 400 + 60 = 460."
    },
    {
        "question": "What is the value of 2³ × 3²?",
        "answer": 72,
        "explanation": "2³ × 3² = 8 × 9 = 72."
    },
    {
        "question": "If a = 5 and b = 3, what is the value of a² - b²?",
        "answer": 16,
        "explanation": "a² - b² = 5² - 3² = 25 - 9 = 16."
    },
]

# Add additional multiple choice questions
quiz_questions.extend(additional_quiz_questions)
quiz_questions.extend(brain_teasers)
quiz_questions.extend(science_questions)
quiz_questions.extend(history_questions)
# Add additional true/false questions
tf_questions.extend(additional_tf_questions)
tf_questions.extend(science_tf)
# Add additional math puzzles
math_puzzles.extend(additional_math_puzzles)

# Constants
QUIZ_COUNT = 7
TF_COUNT = 5
MATH_COUNT = 5

# Set page configuration
st.set_page_config(
    page_title="Interactive Quiz Challenge",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def load_css():
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem !important;
        color: #1E88E5;
        text-align: center;
        text-shadow: 2px 2px 4px #cccccc;
        padding: 20px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .question-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    .timer {
        font-size: 1.5rem;
        font-weight: bold;
        color: #FF5722;
    }
    
    .correct-answer {
        color: #4CAF50;
        font-weight: bold;
    }
    
    .wrong-answer {
        color: #F44336;
        font-weight: bold;
    }
    
    .btn-primary {
        background-color: #1E88E5;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .btn-primary:hover {
        background-color: #1565C0;
        transform: translateY(-2px);
    }
    
    .category-tag {
        background-color: #E3F2FD;
        color: #1565C0;
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
        margin-right: 5px;
    }
    
    .stProgress > div > div > div > div {
        background-color: #1E88E5;
    }
    </style>
    """, unsafe_allow_html=True)

# timer_component.py
import streamlit as st
import streamlit.components.v1 as components
import time
import uuid

def create_timer_html(time_limit, timer_id, height=100):
    """Create HTML/JS for a real-time timer"""
    return f"""
    <div style="font-family: Arial, sans-serif; padding: 10px;">
        <div style="font-size: 1.5rem; font-weight: bold; color: #FF5722; margin-bottom: 10px;">
            Time remaining: <span id="timer_{timer_id}">0.0</span> seconds
        </div>
        <div style="background-color: #e0e0e0; border-radius: 5px; height: 20px; width: 100%;">
            <div id="progress_{timer_id}" style="background-color: #1E88E5; height: 100%; width: 100%; border-radius: 5px; transition: width 0.1s linear;"></div>
        </div>
        
        <script>
            (function() {{
                const timerElement = document.getElementById("timer_{timer_id}");
                const progressElement = document.getElementById("progress_{timer_id}");
                let timeLeft = {time_limit};
                
                timerElement.textContent = timeLeft.toFixed(1);
                
                const interval = setInterval(() => {{
                    timeLeft -= 0.1;
                    
                    if (timeLeft <= 0) {{
                        timeLeft = 0;
                        clearInterval(interval);
                        
                        // Send message to parent when timer ends
                        window.parent.postMessage({{
                            type: "timer_end",
                            timer_id: "{timer_id}"
                        }}, "*");
                    }}
                    
                    // Update timer display
                    timerElement.textContent = timeLeft.toFixed(1);
                    
                    // Update progress bar
                    const progressWidth = (timeLeft / {time_limit}) * 100;
                    progressElement.style.width = `${{progressWidth}}%`;
                    
                    // Send current time to parent
                    window.parent.postMessage({{
                        type: "timer_update",
                        timer_id: "{timer_id}",
                        time_left: timeLeft
                    }}, "*");
                    
                }}, 100);
                
                // Clean up on unmount
                window.addEventListener("beforeunload", () => {{
                    clearInterval(interval);
                }});
            }})();
        </script>
    </div>
    """

def countdown_timer(time_limit, key=None, height=100):
    """
    Display a real-time countdown timer
    
    Parameters:
    - time_limit: Time in seconds
    - key: Optional unique key
    - height: Height of the component in pixels
    
    Returns:
    - time_left: The time left when the component was last updated
    """
    if key is None:
        key = f"timer_{str(uuid.uuid4())}"
    
    # Store the timer ID in session state
    timer_key = f"timer_id_{key}"
    if timer_key not in st.session_state:
        st.session_state[timer_key] = str(uuid.uuid4())
    
    timer_id = st.session_state[timer_key]
    
    # Create the HTML/JS for the timer
    timer_html = create_timer_html(time_limit, timer_id, height)
    
    # Display the timer using components
    components.html(timer_html, height=height)
    
    # Store time when timer was started
    start_key = f"timer_start_{key}"
    if start_key not in st.session_state:
        st.session_state[start_key] = time.time()
    
    # Calculate time left
    elapsed = time.time() - st.session_state[start_key]
    time_left = max(0, time_limit - elapsed)
    
    # Check if timer has ended
    if time_left <= 0 and f"timer_ended_{key}" not in st.session_state:
        st.session_state[f"timer_ended_{key}"] = True
    
    return time_left

def reset_timer(key):
    """Reset a timer by key"""
    if f"timer_start_{key}" in st.session_state:
        del st.session_state[f"timer_start_{key}"]
    if f"timer_ended_{key}" in st.session_state:
        del st.session_state[f"timer_ended_{key}"]

# Welcome page
def welcome_page():
    st.markdown('<h1 class="main-header">🎮 Interactive Quiz Challenge 🎮</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Welcome to the Ultimate Quiz Challenge!
        
        Test your knowledge across different subjects with our interactive quiz game.
        
        ### Game Rounds:
        1. **Quiz Round**: Multiple choice questions on various topics
        2. **True/False Lightning Round**: Quick yes/no questions with a 10-second time limit
        3. **Math Challenge**: Solve math puzzles against the clock with bonus points for fast answers
        
        Are you ready to challenge yourself?
        """)
        
        st.session_state.username = st.text_input("Enter your name:", value=st.session_state.get("username", ""))
        
        # Difficulty selection
        st.subheader("Game Settings")
        col_diff, col_cat = st.columns(2)
        
        with col_diff:
            st.session_state.difficulty = st.select_slider(
                "Difficulty Level",
                options=["Easy", "Medium", "Hard"],
                value=st.session_state.get("difficulty", "Medium")
            )
        
        with col_cat:
            st.session_state.time_limit_tf = st.slider(
                "True/False Time Limit (seconds)",
                min_value=5,
                max_value=20,
                value=st.session_state.get("time_limit_tf", 10)
            )
            
            st.session_state.time_limit_math = st.slider(
                "Math Time Limit (seconds)",
                min_value=10,
                max_value=30,
                value=st.session_state.get("time_limit_math", 15)
            )
        
        # Category selection
        st.subheader("Select Question Categories")
        
        col_cat1, col_cat2, col_cat3 = st.columns(3)
        
        with col_cat1:
            st.session_state.include_science = st.checkbox("Science", value=st.session_state.get("include_science", True))
            st.session_state.include_history = st.checkbox("History", value=st.session_state.get("include_history", True))
        
        with col_cat2:
            st.session_state.include_geography = st.checkbox("Geography", value=st.session_state.get("include_geography", True))
            st.session_state.include_brainteasers = st.checkbox("Brain Teasers", value=st.session_state.get("include_brainteasers", True))
        
        with col_cat3:
            st.session_state.include_general = st.checkbox("General Knowledge", value=st.session_state.get("include_general", True))
            st.session_state.include_art = st.checkbox("Art & Literature", value=st.session_state.get("include_art", True))
        
        if st.button("Start Quiz", type="primary", use_container_width=True):
            if st.session_state.username:
                st.session_state.page = 'quiz'
                st.session_state.total_score = 0
                st.rerun()
            else:
                st.error("Please enter your name to begin!")
    
    with col2:
        st.image("https://img.freepik.com/free-vector/quiz-word-concept_23-2147844150.jpg", width=300)
        
        # Display leaderboard if available
        if 'leaderboard' in st.session_state:
            st.subheader("Top Scorers")
            df_leader = pd.DataFrame(st.session_state.leaderboard)
            if not df_leader.empty:
                st.dataframe(df_leader.head(5)[['Name', 'Score', 'Percentage']], hide_index=True)

def quiz_round_page():
    st.title("📝 Quiz Round")
    st.progress(1/3)
    
    # Filter questions based on selected categories
    filtered_questions = []
    for q in quiz_questions:
        category = q.get("category", "general")
        if (category == "science" and st.session_state.get("include_science", True)) or \
           (category == "history" and st.session_state.get("include_history", True)) or \
           (category == "geography" and st.session_state.get("include_geography", True)) or \
           (category == "brainteaser" and st.session_state.get("include_brainteasers", True)) or \
           (category == "art" and st.session_state.get("include_art", True)) or \
           (category == "literature" and st.session_state.get("include_art", True)) or \
           (category == "general" and st.session_state.get("include_general", True)) or \
           ("category" not in q and st.session_state.get("include_general", True)):
            filtered_questions.append(q)
    
    # Initialize quiz state
    if 'quiz_questions_selected' not in st.session_state:
        if len(filtered_questions) < QUIZ_COUNT:
            st.warning(f"Not enough questions match your category selections. Using all available questions.")
            st.session_state.quiz_questions_selected = filtered_questions
        else:
            st.session_state.quiz_questions_selected = random.sample(filtered_questions, k=QUIZ_COUNT)
        st.session_state.current_quiz_question = 0
        st.session_state.quiz_score = 0
    
    # Display current question
    if st.session_state.current_quiz_question < len(st.session_state.quiz_questions_selected):
        q = st.session_state.quiz_questions_selected[st.session_state.current_quiz_question]
        
        # Simple question display
        st.subheader(f"Question {st.session_state.current_quiz_question + 1} of {len(st.session_state.quiz_questions_selected)}")
        
        # Display the question text directly
        st.subheader(q['q'])
        
        # Display category if available
        if "category" in q:
            st.caption(f"Category: {q['category'].title()}")
        
        # Use radio buttons for options
        answer = st.radio("Select your answer:", q['options'], key=f"quiz_{st.session_state.current_quiz_question}")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("Submit Answer", type="primary", use_container_width=True):
                if answer.lower() == q['ans'].lower():
                    st.success("✅ Correct!")
                    st.session_state.quiz_score += 1
                else:
                    st.error(f"❌ Wrong! The correct answer is: {q['ans']}")
                
                # Move to next question
                st.session_state.current_quiz_question += 1
                st.rerun()  # Changed from experimental_rerun
        
        with col2:
            if st.button("Skip Question", use_container_width=True):
                st.session_state.current_quiz_question += 1
                st.rerun()  # Changed from experimental_rerun
        
    
    else:
        # Quiz round completed
        st.success(f"Quiz Round Complete! Your score: {st.session_state.quiz_score}/{len(st.session_state.quiz_questions_selected)}")
        st.session_state.total_score += st.session_state.quiz_score
        
        if st.button("Continue to True/False Round", type="primary"):
            st.session_state.page = 'tf'
            # Reset for next round
            if 'quiz_questions_selected' in st.session_state:
                del st.session_state.quiz_questions_selected
                del st.session_state.current_quiz_question
            st.rerun()  # Changed from experimental_rerun

def tf_round_page():
    st.title("⚡ True/False Lightning Round")
    st.progress(2/3)
    
    # Initialize TF round state
    if 'tf_questions_selected' not in st.session_state:
        st.session_state.tf_questions_selected = random.sample(tf_questions, k=TF_COUNT)
        st.session_state.current_tf_question = 0
        st.session_state.tf_score = 0
    
    # Display current question
    if st.session_state.current_tf_question < len(st.session_state.tf_questions_selected):
        q = st.session_state.tf_questions_selected[st.session_state.current_tf_question]
        
        # Simple question display
        st.subheader(f"Question {st.session_state.current_tf_question + 1} of {len(st.session_state.tf_questions_selected)}")
        
        # Display the question text directly
        st.subheader(q['q'])
        
        # Get time limit from session state or use default
        time_limit = st.session_state.get("time_limit_tf", 10)
        
        # Display the timer
        timer_key = f"tf_timer_{st.session_state.current_tf_question}"
        time_left = countdown_timer(time_limit, key=timer_key)
        
        # Check if timer has ended
        timer_ended = f"timer_ended_{timer_key}" in st.session_state
        
        # Answer buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("YES", key=f"yes_{st.session_state.current_tf_question}", use_container_width=True):
                if time_left > 0:
                    if "yes" == q['ans']:
                        st.success("✅ Correct!")
                        st.session_state.tf_score += 1
                    else:
                        st.error(f"❌ Wrong! The correct answer is: {q['ans'].upper()}")
                else:
                    st.warning("Too slow! No points awarded.")
                
                # Move to next question
                st.session_state.current_tf_question += 1
                time.sleep(1)  # Brief pause to see result
                st.rerun()
        
        with col2:
            if st.button("NO", key=f"no_{st.session_state.current_tf_question}", use_container_width=True):
                if time_left > 0:
                    if "no" == q['ans']:
                        st.success("✅ Correct!")
                        st.session_state.tf_score += 1
                    else:
                        st.error(f"❌ Wrong! The correct answer is: {q['ans'].upper()}")
                else:
                    st.warning("Too slow! No points awarded.")
                
                # Move to next question
                st.session_state.current_tf_question += 1
                time.sleep(1)  # Brief pause to see result
                st.rerun()
        
        # Auto-advance if timer has ended
        if timer_ended:
            st.warning("Time's up!")
            st.session_state.current_tf_question += 1
            time.sleep(1)  # Brief pause to see the warning
            st.rerun()
    
    else:
        # TF round completed
        st.success(f"True/False Round Complete! Your score: {st.session_state.tf_score}/{len(st.session_state.tf_questions_selected)}")
        st.session_state.total_score += st.session_state.tf_score
        
        if st.button("Continue to Math Challenge", type="primary"):
            st.session_state.page = 'math'
            # Reset for next round
            if 'tf_questions_selected' in st.session_state:
                del st.session_state.tf_questions_selected
                del st.session_state.current_tf_question
                del st.session_state.tf_score
                
                # Clean up timer keys
                for key in list(st.session_state.keys()):
                    if key.startswith("tf_timer_"):
                        reset_timer(key)
            st.rerun()

def math_challenge_page():
    st.title("🧮 Math Challenge")
    st.progress(3/3)
    
    # Initialize math challenge state
    if 'math_puzzles_selected' not in st.session_state:
        st.session_state.math_puzzles_selected = random.sample(math_puzzles, k=MATH_COUNT)
        st.session_state.current_math_puzzle = 0
        st.session_state.math_score = 0
    
    # Display current puzzle
    if st.session_state.current_math_puzzle < len(st.session_state.math_puzzles_selected):
        puzzle = st.session_state.math_puzzles_selected[st.session_state.current_math_puzzle]
        
        # Simple puzzle display
        st.subheader(f"Puzzle {st.session_state.current_math_puzzle + 1} of {len(st.session_state.math_puzzles_selected)}")
        
        # Display the puzzle text directly
        st.subheader(puzzle['question'])
        
        # Get time limit from session state or use default
        time_limit = st.session_state.get("time_limit_math", 15)
        
        # Display the timer
        timer_key = f"math_timer_{st.session_state.current_math_puzzle}"
        time_left = countdown_timer(time_limit, key=timer_key)
        
        # Check if timer has ended
        timer_ended = f"timer_ended_{timer_key}" in st.session_state
        
        # Answer input
        answer = st.text_input("Your answer:", key=f"math_input_{st.session_state.current_math_puzzle}")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            if st.button("Submit Answer", type="primary", use_container_width=True):
                if time_left > 0:
                    try:
                        user_ans = float(answer)
                        if abs(user_ans - puzzle["answer"]) < 0.001:
                            # Calculate if user gets bonus points based on time left
                            if time_left >= time_limit / 2:
                                points = 3
                                st.success(f"✅ Correct! Fast answer bonus +3 points!")
                            else:
                                points = 1
                                st.success(f"✅ Correct! +1 point")
                            st.session_state.math_score += points
                        else:
                            st.error(f"❌ Wrong answer. The correct answer is {puzzle['answer']}.")
                            st.info(f"Explanation: {puzzle['explanation']}")
                    except ValueError:
                        st.error("Please enter a valid number.")
                else:
                    st.warning("Time's up! No points awarded.")
                
                # Move to next puzzle
                st.session_state.current_math_puzzle += 1
                time.sleep(1.5)  # Brief pause to see result
                st.rerun()
        
        with col2:
            if st.button("Skip", use_container_width=True):
                st.session_state.current_math_puzzle += 1
                st.rerun()
        
        # Auto-advance if timer has ended
        if timer_ended:
            st.warning("Time's up!")
            st.session_state.current_math_puzzle += 1
            time.sleep(1)  # Brief pause to see the warning
            st.rerun()
    
    else:
        # Math challenge completed
        max_possible = len(st.session_state.math_puzzles_selected) * 3
        st.success(f"Math Challenge Complete! Your score: {st.session_state.math_score}/{max_possible} (max with bonuses)")
        st.session_state.total_score += st.session_state.math_score
        
        if st.button("See Final Results", type="primary"):
            st.session_state.page = 'results'
            # Reset for next round
            if 'math_puzzles_selected' in st.session_state:
                del st.session_state.math_puzzles_selected
                del st.session_state.current_math_puzzle
                del st.session_state.math_score
                
                # Clean up timer keys
                for key in list(st.session_state.keys()):
                    if key.startswith("math_timer_"):
                        reset_timer(key)
            st.rerun()

def results_page():
    st.title("🏆 Quiz Results 🏆")
    
    # Calculate total possible score
    quiz_max = QUIZ_COUNT
    tf_max = TF_COUNT
    math_max = MATH_COUNT * 3
    max_score = quiz_max + tf_max + math_max
    percentage = (st.session_state.total_score / max_score) * 100
    
    # Display results with animation
    st.balloons()
    
    st.header(f"Congratulations, {st.session_state.username}!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Performance display code remains the same...
        st.subheader("Your Performance:")
        st.write(f"Total Score: {st.session_state.total_score} out of {max_score}")
        st.write(f"Percentage: {percentage:.1f}%")
        
        # Performance feedback
        if percentage >= 90:
            st.success("🌟 Outstanding! You're a quiz master!")
        elif percentage >= 70:
            st.success("🎉 Great job! You have excellent knowledge!")
        elif percentage >= 50:
            st.info("👍 Good effort! Keep learning!")
        else:
            st.warning("📚 Keep practicing! You'll improve with time.")
        
        # Chart code remains the same...
        try:
            # Get scores, using 0 as default if not found
            quiz_score = st.session_state.get("quiz_score", 0)
            tf_score = st.session_state.get("tf_score", 0)
            math_score = st.session_state.get("math_score", 0)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Create data
            categories = ['Quiz Round', 'True/False Round', 'Math Challenge']
            scores = [quiz_score, tf_score, math_score]
            max_scores = [quiz_max, tf_max, math_max]
            
            # Create chart
            x = range(len(categories))
            width = 0.35
            
            ax.bar([i - width/2 for i in x], scores, width, label='Your Score', color='#1f77b4')
            ax.bar([i + width/2 for i in x], max_scores, width, label='Maximum', color='#ff7f0e', alpha=0.7)
            
            ax.set_ylabel('Score')
            ax.set_title('Performance by Round')
            ax.set_xticks(x)
            ax.set_xticklabels(categories)
            ax.legend()
            
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Could not display chart: {e}")
            st.info("Scores may not be available for all rounds.")
    
    with col2:
        # Modified leaderboard code to prevent duplicates
        if 'leaderboard' not in st.session_state:
            st.session_state.leaderboard = []
            
        # Check if this is the first time reaching results page in this session
        if 'results_recorded' not in st.session_state:
            new_entry = {
                'Name': st.session_state.username,
                'Score': st.session_state.total_score,
                'Percentage': round(percentage, 1),
                'Date': datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            
            # Add entry to leaderboard
            st.session_state.leaderboard.append(new_entry)
            st.session_state.leaderboard = sorted(st.session_state.leaderboard, key=lambda x: x['Score'], reverse=True)
            
            # Mark that we've recorded this result
            st.session_state.results_recorded = True
        
        # Display leaderboard
        st.subheader("Leaderboard")
        if st.session_state.leaderboard:
            # Convert to DataFrame and ensure we have unique entries
            df_leaderboard = pd.DataFrame(st.session_state.leaderboard)
            
            # Optional: If you want to keep only the best score for each player
            # df_leaderboard = df_leaderboard.sort_values('Score', ascending=False).drop_duplicates('Name').reset_index(drop=True)
            
            st.dataframe(df_leaderboard[['Name', 'Score', 'Percentage']], hide_index=True)
    
    # Play again or exit
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Play Again", type="primary", use_container_width=True):
            st.session_state.page = 'welcome'
            # Reset scores
            if 'quiz_score' in st.session_state:
                del st.session_state.quiz_score
            if 'tf_score' in st.session_state:
                del st.session_state.tf_score
            if 'math_score' in st.session_state:
                del st.session_state.math_score
            # Reset results_recorded flag so next game will be recorded
            if 'results_recorded' in st.session_state:
                del st.session_state.results_recorded
            st.rerun()
    
    with col2:
        if st.button("View Statistics", use_container_width=True):
            st.session_state.page = 'stats'
            st.rerun()

def statistics_page():
    st.title("📊 Quiz Statistics")
    
    if 'leaderboard' in st.session_state and len(st.session_state.leaderboard) > 0:
        df_stats = pd.DataFrame(st.session_state.leaderboard)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Top Performers")
            top_players = df_stats.head(5)[['Name', 'Score', 'Percentage']]
            st.dataframe(top_players, hide_index=True)
            
            st.subheader("Score Distribution")
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Create histogram of scores
            ax.hist(df_stats['Score'], bins=10, color='#1f77b4', alpha=0.7)
            ax.set_xlabel('Score')
            ax.set_ylabel('Number of Players')
            ax.set_title('Score Distribution')
            
            st.pyplot(fig)
        
        with col2:
            st.subheader("Average Score")
            avg_score = df_stats['Score'].mean()
            max_score = QUIZ_COUNT + TF_COUNT + (MATH_COUNT * 3)
            avg_percentage = (avg_score / max_score) * 100
            
            st.metric("Average Score", f"{avg_score:.1f}/{max_score}", f"{avg_percentage:.1f}%")
            
            # Create pie chart of score ranges - FIXED VERSION
            st.subheader("Performance Categories")
            
            # Define score ranges
            ranges = [
                (90, 100, "Excellent", "#4CAF50"),
                (70, 90, "Good", "#2196F3"),
                (50, 70, "Average", "#FFC107"),
                (0, 50, "Needs Improvement", "#F44336")
            ]
            
            # Initialize counts for each range
            range_counts = [0, 0, 0, 0]
            range_labels = [r[2] for r in ranges]
            range_colors = [r[3] for r in ranges]
            
            # Count players in each range
            max_possible = QUIZ_COUNT + TF_COUNT + (MATH_COUNT * 3)
            
            # Make sure we have at least one entry in each category for demonstration
            # Remove this in production if you want actual data only
            demo_data = False
            if demo_data:
                range_counts = [1, 2, 3, 1]  # Demo data
            else:
                # Count actual data
                for i, (min_val, max_val, _, _) in enumerate(ranges):
                    min_score = min_val * max_possible / 100
                    max_score_range = max_val * max_possible / 100
                    count = df_stats[(df_stats['Score'] >= min_score) & (df_stats['Score'] < max_score_range)].shape[0]
                    range_counts[i] = count
            
            # If all counts are 0, add a dummy value to avoid empty chart
            if sum(range_counts) == 0:
                range_counts = [0, 0, 0, 1]  # Default to "Needs Improvement" if no data
                st.info("Not enough data to show meaningful performance distribution.")
            
            # Create pie chart
            fig, ax = plt.subplots(figsize=(8, 8))
            wedges, texts, autotexts = ax.pie(
                range_counts, 
                labels=range_labels, 
                autopct='%1.1f%%', 
                startangle=90, 
                colors=range_colors,
                wedgeprops={'edgecolor': 'white', 'linewidth': 1}
            )
            
            # Enhance text visibility
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontsize(12)
                autotext.set_fontweight('bold')
            
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
            
            st.pyplot(fig)
    
    else:
        st.info("No quiz data available yet. Play some games to see statistics!")
    
    if st.button("Back to Results", type="primary"):
        st.session_state.page = 'results'
        st.rerun()

def sidebar():
    with st.sidebar:
        st.title("Quiz Game")
        
        if st.session_state.page != 'welcome':
            st.info(f"Player: {st.session_state.username}")
            st.metric("Current Score", st.session_state.get("total_score", 0))
        
        st.subheader("Game Settings")
        
        # Sound toggle
        sound_on = st.checkbox("Sound Effects", value=True, key="sound")
        
        # Help section
        with st.expander("How to Play"):
            st.write("""
            1. **Quiz Round**: Select the correct answer from multiple choices.
            2. **True/False Round**: Answer yes/no questions within the time limit.
            3. **Math Challenge**: Solve math puzzles within the time limit. Fast answers earn bonus points!
            """)
        
        # About section
        with st.expander("About"):
            st.write("""
            This interactive quiz game was created with Streamlit. 
            It features multiple question types and challenges to test your knowledge.
            
            Created for grades 8-10 students.
            """)
        
        # Reset game button
        if st.button("Reset Game", type="secondary"):
            for key in list(st.session_state.keys()):
                if key not in ['leaderboard']:
                    del st.session_state[key]
            st.session_state.page = 'welcome'
            st.rerun()  # Changed from experimental_rerun

def main():
    # Session state initialization
    if 'page' not in st.session_state:
        st.session_state.page = 'welcome'
    if 'total_score' not in st.session_state:
        st.session_state.total_score = 0
    
    # Display sidebar
    sidebar()
    
    # Navigation with error handling
    try:
        if st.session_state.page == 'welcome':
            welcome_page()
        elif st.session_state.page == 'quiz':
            quiz_round_page()
        elif st.session_state.page == 'tf':
            tf_round_page()
        elif st.session_state.page == 'math':
            math_challenge_page()
        elif st.session_state.page == 'results':
            results_page()
        elif st.session_state.page == 'stats':
            statistics_page()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Resetting to welcome page...")
        st.session_state.page = 'welcome'
        if st.button("Return to Welcome Page"):
            st.rerun()  # Changed from experimental_rerun

if __name__ == "__main__":
    main()