import tkinter as tk
from tkinter import messagebox, ttk


class DSAQuizApp:
    def __init__(self, master):
        self.master = master      
        self.master.title("DSA Quiz App")
        self.master.configure(bg = "green")
        self.quiz_data = [
             {
                "question": "Stacks are used for the implementation of recursion.",
                "choices": ["True", "False"],
                "answer": "True"
             },
             {
                "question": "When a pop() operation is called on an empty queue, what is the condition called?",
                "choices": ["Overflow", "Underflow", "Syntax Error", "Garbage Value"],
                "answer": "Underflow"
             },
             {
                "question": "Which of the following is a linear data structure?",
                "choices": ["Array", "AVL trees", "Binary Trees", "Graphs"],
                "answer": "Array"
             },
             {
                "question": "Which of the following data structures can be used to implement queues?",
                "choices": ["Stack", "Arrays", "Linked List", "All of the above"],
                "answer": "All of the above"
             },
             {
                "question": "Which of the following data structure works on the principle of 'First Come First Serve'?",
                "choices": ["Priority Queue", "Heap", "Queue", "Stack"],
                "answer": "Queue"
             }   
        ]
        self.current_question = 0
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.qs_label = ttk.Label(
            self.master,
            text="",
            anchor="center",
            wraplength=500,
            padding=100
        )
        self.qs_label.pack(pady=10)
        
        style = ttk.Style()
        style.configure("TButton", foreground = "black")
        self.choice_btns = []
        for i in range(4):
            button = ttk.Button(
                self.master,
                text="",               
                command=lambda i=i: self.check_answer(i),
                style = "TButton"
            )
            button.pack(pady=10)
            self.choice_btns.append(button)

        self.feedback_label = ttk.Label(
            self.master,
            text="",
            anchor="center",
            padding=10
        )
        self.feedback_label.pack(pady=10)
        style = ttk.Style()
        style.configure("Next.TButton", foreground = "blue")
        self.next_btn = ttk.Button(
            self.master,
            text="Next",
            command=self.next_question,
            state = "disabled",
            style = "Next.TButton"
        )
        self.next_btn.pack(pady=10)

        self.show_question()

    def show_question(self):
        if self.current_question < len(self.quiz_data):
            question_data = self.quiz_data[self.current_question]
            self.qs_label.config(text=question_data["question"])

            for i, choice in enumerate(question_data["choices"]):
                self.choice_btns[i].config(text=choice, state="normal")

            self.feedback_label.config(text="")
            self.next_btn.config(state="disabled")
        else:
            self.show_result()

    def check_answer(self, choice):
        selected_choice = self.quiz_data[self.current_question]["choices"][choice]
        correct_answer = self.quiz_data[self.current_question]["answer"]

        if selected_choice == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct!", foreground="green")
            
        else:
            self.feedback_label.config(text="Incorrect!", foreground="red")

        for button in self.choice_btns:
            button.config(state="disabled")
        self.next_btn.config(state="normal")

    def next_question(self):
        self.current_question += 1
        self.show_question()

    def show_result(self):
        messagebox.showinfo("DSA Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(self.score, len(self.quiz_data)))
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DSAQuizApp(root)
    root.mainloop()
