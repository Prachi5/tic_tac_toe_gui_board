import tic_tac_toe_menu 

def evClick(row,col):
	mb.showinfo("Cell clicked", "row;{}, col;{}".format(row,col))
def buildBoard(parent):
	outer = tk.Frame(parent, border=2 , relief="sunken")
	inner = tk.Frame(outer)
	inner.pack()
	for row in range(3):
		for col in range(3):
			cell = tk.Button(inner, text=" ", width="5", height="2",command=lambda r=row, c=col : evClick(r,c) )
			cell.grid(row=row,column=col)
	return outer
mbar = buildMenu(top)
top["menu"] = mbar
board = buildBoard(top)
board.pack()
status = tk.Label(top,text="testing",border=0,background="lightgrey", foreground="red")
status.pack(anchor="s", fill="x", expand=True)
tk.mainloop()



gameover = False
def evClick(row,col):
        global gameover
        if gameover:
                mb.showerror("Game over", "Game over!")
                return
        game = cells2game()
        index = (3*row) + col
        result = tic_tac_toe_logic.userMove(game, index)
        game2cells(game)
        if not result:
                result = tic_tac_toe_logic.computerMove(game)
                game2cells(game)
        if result == "D":
                mb.showinfo("Result","It's a Draw!")
                gameover = True
        else:
                if result == "X" or result == "O":
                        mb.showinfo("Result", "The winner is: {}".format(result))
                        gameover = True
def game2cells(game):
	table = board.pack_slaves()[0]
	for row in range(3):
		for col in range(3):
			table.grid_slaves(row=row,column=col)[0]['text'] = game[3*row+col]


def cells2game():
	values = []
	table = board.pack_slaves()[0]
	for row in range(3):
		for col in range(3):
			values.append(table.grid_slaves(row=row, column=col)[0]['text'])
	return values
	
