import tkinter as tk
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.welcome_message = tk.Label(root, text="NATIONAL INSTITUTE OF TECHNOLOGY , RAIPUR", font=("Arial", 40))
        self.welcome_message.pack(pady=10)
        self.welcome_message = tk.Label(root, text="WARM WELCOME TO ALL THE STUDENTS IN ELECTRICAL ENGINEERING DEPARTMENT, #batch23-27 #eed\nTEAM ELECTRICAL ENGINEERING ASSOCIATION(EEA)", font=("Arial", 12))
        self.welcome_message.pack(pady=10)
        self.root.geometry("800x400")  

        
        self.top_frame = tk.Frame(root, bg="black")
        self.top_frame.pack(fill=tk.BOTH, expand=True)

        
        self.bottom_frame = tk.Frame(root, bg="pink")
        self.bottom_frame.pack(fill=tk.BOTH, expand=True)

        self.names = [
            "Aaroh Kanoje", "Aarya Shastri", "Aashi Umrao", "Aayush", "Abhijeet Singh",
            "Adarsh Mukund Jha", "Aditya Bhattacharya", "Aditya Kale", "Aditya Kumar", "Ajay Kumar",
            "Alwaru Yashashwini", "Aman Kumar Sharma", "Amurtya Rai", "Andra Manoj", "Aniruddha Tiwari",
            "Anmol Kumar Agrawal", "Anoushka Panda", "Anshul Prasad", "Anupam Poddar", "Anurag Gadhwal",
            "Anurag Mishra", "Aparna Prasad", "Archit Soni", "Arthav", "Aryan Singh",
            "Ashish Kumar Jangid", "Ashish Kumar Raj", "Ayush Dewangan", "Ayush Jha", "Ayush Kumar Mishra",
            "Ayush Sen", "B Akshay Kumar", "B. Gangothri", "Bhupinder Singh", "Chayan Solanki", "Chhavi Rajput",
            "Daksh Tripathi", "Deepak Kumar", "Divyanshu Verma", "Durgesh Kumar", "Galisusanth", "Girdhari Yadav",
            "Hardeep Singh", "Harsh Patel", "Hemkumar Dhruw", "Himanshu Bisht", "Hitesh", "Hiteshwar Karanga",
            "Ishant Gupta", "J. Avinash", "Jadi Pavani", "K. Sucharita", "Karandeep Taram", "Khushboo Kumari",
            "Krishnapriya Matala", "Kumar Shashwat", "Kushagra Gupta", "Lokesh Dewangan", "Mayank Somkuwar",
            "Mitesh Dewangan", "Mohd. Sohil", "Mokshda Bhatt", "Mouryan Kosare", "Mudadla Gnana Prasoona",
            "Naincy Vaishya", "Nikhil Kumar Dewangan", "Nipun Modi", "Nisha Thakur", "Nishant Diwate", "Nooka Rahul",
            "Parth Dubey", "Piyush Sarkar", "Prabhas Keerthan", "Pragna Gode", "Pragyeshwar Nirmalkar", "Prashant Mishra",
            "Prateek Kurrey", "Praveen Kumar", "Prince Kumar Singh", "R. Krishneshwar Reddy", "R. Rohan", "Raghav Agrawal",
            "Raghvendra Pratap Singh", "Rahul Kumar Sao", "Reena Dewangan", "Rikshi Robinson Kindo", "Rishi Prajapati",
            "Rohit Khatri", "S. Satwik", "Sahil Pundpal", "Sakshi Singh", "Sanskar Gupta", "Savita Singhal",
            "Shikhar Kashyap", "Shivam Jha", "Shivam Singh", "Shivam Vashistha", "Siddharth Jaiswal", "Sumeet Kumar",
            "Sundaram Kumar Rai", "Suyash Dwivedi", "Swarnadeep Patra"
        ]

        self.current_name = None
        self.current_question = None

        self.questions = [
            "If you could have any superpower, what would it be and why?",
            "What's the weirdest food combination you have ever tried and liked?",
            "What's your go-to dance move when no one's watching?",
            "If you could swap lives with a cartoon character for a day, who would it be and why?",
            "If you could invent a new college rule, what would it be?",
            "What's the silliest thing that's ever made you laugh uncontrollably?",
            "What is the most useless talent you have?",
            "What will you do when you're alone in your room?",
            "What is the thing you like the most and the thing you hate the most?",
            "What is your favorite sad song that makes you laugh?",
            "What is the most disturbing and irritating thing for you?",
            "If you had a chance to be a hero or a villain, what would it be and why?",
            "What is the thing you like the most about your college or school?",
            "What is something you have never experienced but want to do in the future?",
             "If you could have any superpower, what would it be and why?",
            "What's the weirdest food combination you have ever tried and liked?",
            "What's your go-to dance move when no one's watching?",
            "If you could swap lives with a cartoon character for a day, who would it be and why?",
            "If you could invent a new college rule, what would it be?",
            "What's the silliest thing that's ever made you laugh uncontrollably?",
            "What is the most useless talent you have?",
            "What will you do when you're alone in your room?",
            "What is the thing you like the most and the thing you hate the most?",
            "What is your favorite sad song that makes you laugh?",
            "What is the most disturbing and irritating thing for you?",
            "If you had a chance to be a hero or a villain, what would it be and why?",
            "What is the thing you like the most about your college or school?",
            "What is something you have never experienced but want to do in the future?"
        ]

        self.label = tk.Label(self.top_frame, text="", font=("Arial", 18), bg="black", fg="white")
        self.label.pack(pady=10)

        self.next_name_button = tk.Button(self.top_frame, text="Next Name", command=self.next_name, bg="black", fg="white")
        self.next_name_button.pack(pady=10)

        self.next_question_button = tk.Button(self.top_frame, text="Next Question", command=self.next_question, bg="black", fg="white")
        self.next_question_button.pack(pady=10)

        self.quit_button = tk.Button(self.top_frame, text="Quit", command=root.quit, bg="black", fg="white")
        self.quit_button.pack(pady=10)

        self.welcome_message = tk.Label(self.bottom_frame, text="TEAM EEA", font=("Arial", 12), fg="pink", bg="black")
        self.welcome_message.pack(pady=10)
        self.welcome_message = tk.Label(self.bottom_frame, text="DESIGNED AND CODED BY ANONYMOUS", font=("Arial", 20), fg="pink", bg="black")
        self.welcome_message.pack(pady=10)

    def start_game(self):
        if self.names and self.questions:
            self.next_name()
            self.next_name_button.config(state=tk.NORMAL)
            self.next_question_button.config(state=tk.NORMAL)
        else:
            self.label.config(text="No more names or questions!")

    def next_name(self):
        if self.names:
            self.current_name = random.choice(self.names)
            self.names.remove(self.current_name)
            self.display_current_name_question()

    def next_question(self):
        if self.questions:
            self.current_question = random.choice(self.questions)
            self.questions.remove(self.current_question)
            self.display_current_name_question()

    def display_current_name_question(self):
        display_text = f"Name: {self.current_name}\nQuestion: {self.current_question}"
        self.label.config(text=display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


