#YASHWANTH_SAI_BATHINI
#Imported the respective libraries which are used in the below following program
import tkinter as tk
import random
from PIL import Image, ImageTk
from tkinter import messagebox
#These are the global variables for game statistics
games_played = 0
games_won = 0
games_tied = 0
games_lost = 0
def game_result(player_name, player_selection, computer_selection):
    """
    #This function is used to determine the winner of each round

    Parameters:
    player_name (str): The name of the player.
    player_selection (str): The player's choice (image1, image2, image3).
    computer_selection (str): The computer's random choice (image1, image2, image3).

    Returns:
    str: The result of the game based on the selections.
    """   
    if player_selection == computer_selection: #If both selections are the same, it's a tie
        return "Give it another shot, it's a tie!"
    elif player_selection == 'image1' and computer_selection == 'image3': #If player selects rock and computer selects scissors, player wins
        return f"Excellent {player_name}, you won the game!"
    elif player_selection == 'image2' and computer_selection == 'image1': #If player selects paper and computer selects rock, player wins
        return f"Excellent {player_name}, you won the game!"
    elif player_selection == 'image3' and computer_selection == 'image2': #If player selects scissors and computer selects paper, player wins
        return f"Excellent {player_name}, you won the game!"
    else: #In all other cases, the computer wins the game
        return "Oops, Computer won the game!"
def update_game_stats(outcome): #Update global game statistics based on the outcome of each round
    global games_played, games_won, games_tied, games_lost
    games_played += 1
    if outcome.startswith("Excellent"): #If the outcome indicates a win, increment the games won
        games_won += 1
    elif outcome == "Give it another shot, it's a tie!": #If the outcome indicates a tie, increment tied games
        games_tied += 1
    else:  #If the outcome is a loss, increment games lost
        games_lost += 1
    #Updates the GUI to display with the latest game statistics
    result_stats.config(text=f"PLAYED = {games_played} || WON = {games_won} || TIE = {games_tied} || LOST = {games_lost}")
def game_play_module(selected_var):
    global games_played, games_won, games_tied, games_lost
    
    if not user_entry.get(): #Check if the user has entered their name
        messagebox.showerror("Error Encountered", "Please enter your name and start the game!")
        return
    player_selection = selected_var.get()
    if not player_selection: #If the user hasn't selected anything, show an error message
        messagebox.showerror("Error Encountered", "Please choose one of the shapes to start the game round!")
        return
    computer_selection = random.randint(1, 3)  #Generate a random selection for the computer shape
    #Here it will display the user's selected image shape
    user_image_path = f"image{player_selection}.jpg"
    user_image = Image.open(user_image_path).resize((100, 100))
    user_image_tk = ImageTk.PhotoImage(user_image)
    user_label.config(image=user_image_tk)
    user_label.image = user_image_tk
    #Here it will display the computer's selected image shape
    computer_image_path = f"image{computer_selection}.jpg"
    computer_image = Image.open(computer_image_path).resize((100, 100))
    computer_image_tk = ImageTk.PhotoImage(computer_image)
    computer_label.config(image=computer_image_tk)
    computer_label.image = computer_image_tk
    player_name = user_entry.get()
    #Here it will determine the winner of the every round based on selections
    winner = game_result(player_name, f'image{player_selection}', f'image{computer_selection}')
    result_label.config(text=winner)
    if winner.startswith("Excellent"): #Here it will set the color(Green,Red,Orange) of result label based on the outcome
        result_label.config(fg="green")
    elif winner == "Give it another shot, it's a tie!":
        result_label.config(fg="orange")
    else:
        result_label.config(fg="red")
    update_game_stats(winner)
    #Here it will ask if the user wants to play another round
    if messagebox.askyesno("Another Round", "Do you want to play one more round?"):
        result_label.config(text="")
        selected_var.set(0)  # Set radio buttons to unselected state
        user_label.config(image='')
        computer_label.config(image='')
    else: #If the user chooses not to play another round, close the window
        root.destroy()
def game_play_starts():
    player_name = user_entry.get()
    if not player_name: #Here it will prompt an error message if the user hasn't entered a name
        messagebox.showerror("Error Encountered", "Please enter your name and start the game!")
        return
    #These will hide unnecessary interface elements related to name input
    name_prompt.pack_forget()
    user_entry.pack_forget()
    submit_button.pack_forget()
    #Here it will display a welcome message to the player
    welcome_label = tk.Label(root, text=f"Welcome, {player_name}! Please choose one of the shapes below to begin the game.")
    welcome_label.config(font=("Arial", 10, "bold"))
    welcome_label.pack()
    choice_frame = tk.Frame(root)
    choice_frame.pack()
    #The list of image paths for the choices
    image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    selected_var = tk.IntVar()
    #Here it will display the set of radio buttons with images for user selection
    for i, img_path in enumerate(image_paths):
        img = Image.open(img_path).resize((100, 100))
        img_tk = ImageTk.PhotoImage(img)
        image_label = tk.Radiobutton(choice_frame, image=img_tk, variable=selected_var, value=i + 1)
        image_label.image = img_tk
        image_label.pack()
     #Here it will set the command of start button to initiate game play module
    start_button.config(command=lambda: game_play_module(selected_var))
    start_button.pack()
root = tk.Tk()
root.title("<--ROCK <-> PAPER <-> SCISSORS-->")
window_size = 600
root.geometry(f"{window_size}x{window_size}")
#Interface elements for user input and game display
name_prompt = tk.Label(root, text="What do you want to be called in this game?")
name_prompt.pack()
computer_label = tk.Label(root)
computer_label.pack()
user_entry = tk.Entry(root)
user_entry.pack()
submit_button = tk.Button(root, text="Submit", command=game_play_starts)
submit_button.pack()
user_selection = tk.StringVar()
choice_frame = tk.Frame(root)
choice_frame.pack()
user_choice_label = tk.Label(choice_frame, text="Your Choice")
user_choice_label.grid(row=0, column=0, padx=10)
user_label = tk.Label(choice_frame)
user_label.grid(row=1, column=0, padx=10)
versus_label = tk.Label(choice_frame, text="VS")
versus_label.grid(row=0, column=1, padx=10)
computer_choice_label = tk.Label(choice_frame, text="Computer Choice")
computer_choice_label.grid(row=0, column=2, padx=10)
computer_label = tk.Label(choice_frame)
computer_label.grid(row=1, column=2, padx=10)
start_button = tk.Button(root, text="Start Round")
result_label = tk.Label(root)
result_label.pack()
result_stats = tk.Label(root, text="PLAYED = 0 || WON = 0 || TIE = 0 || LOST = 0")
result_stats.pack()
root.mainloop() #Runs the Tkinter main loop
