import zombiedice

class MyZombie:
    def _init_(self,name):
        #All zombies need a name
        self.name = name

    def turn(self, gameState):
        # gameState is a dictionary with info about the current state of the game

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotguns', and 'footsteps' with how many rolls of each type there were
        # the 'rolls' key is a list of (color, icon) tuples with the exact roll information
        
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
    
zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns = 2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns = 1),
    MyZombie(),
    # add other zombie players here

)

    # Uncomment/Comment one of the following lines to run in CLI or in WEB Gui Mode

    #zombieDice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)