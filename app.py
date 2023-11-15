import tkinter as tk
from tkinter.simpledialog import askstring
from cards import StandardDeck
from players import Player

class CardGameApp:

    def __init__(self, master):
        self.master = master
        self.master.title("Card Game")
        
        self.deck = StandardDeck()
        self.players = []

        self.label = tk.Label(master, text="Card Game")
        self.label.pack()

        self.shuffle_button = tk.Button(master, text="Shuffle", command=self.shuffle_deck)
        self.shuffle_button.pack()

        self.add_player_button = tk.Button(master, text = "Add Player", command = self.add_player)
        self.add_player_button.pack()

        self.deal_button = tk.Button(master, text="Deal", command=self.deal_card)
        self.deal_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def shuffle_deck(self):
        self.deck.shuffle()
        self.result_label["text"] = "Deck shuffled"

    def deal_card(self):

        if not self.players:
            self.result_label["text"] = "No players added."
            return
        
        for player in self.players:
            for _ in range(2):
                card = self.deck.deal()
                if card is not None:
                    player.hand.append(card)
                else:
                    self.result_label["text"] = "The deck is empty"
                    return
                
        self.result_label["text"] = "Cards dealt to players"        
        

    def add_player(self):
        player_name = askstring("Input", "Enter player name:")

        if player_name:
            player = Player(player_name)
            self.players.append(player)
            self.result_label["text"] = f"{player_name} added."
        else:
            self.result_label["text"] = "Player name cannot be empty"

    def run_gui():
        root = tk.Tk()
        app = CardGameApp(root)
        root.mainloop()