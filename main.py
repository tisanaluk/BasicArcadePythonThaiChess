
import arcade
import arcade.gui

# Screen title and size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Test Game with Menu"

class MenuView(arcade.View):
    """Main menu view class."""

    def __init__(self, main_view):
        super().__init__()

        self.manager = arcade.gui.UIManager()

        resume = arcade.gui.UIFlatButton(text="Resume", width=150)
        start_new_game = arcade.gui.UIFlatButton(text="Start New Game", width=150)
        volume = arcade.gui.UIFlatButton(text="Volume", width=150)
        options = arcade.gui.UIFlatButton(text="Options", width=150)

        exit = arcade.gui.UIFlatButton(text="Exit", width=320)

        # Initialise a grid in which widgets can be arranged.
        self.grid = arcade.gui.UIGridLayout(
            column_count=2, row_count=3, horizontal_spacing=20, vertical_spacing=20
        )

        # Adding the buttons to the layout.
        self.grid.add(resume, column=0, row=0)
        self.grid.add(start_new_game, column=1, row=0)
        self.grid.add(volume, column=0, row=1)
        self.grid.add(options, column=1, row=1)
        self.grid.add(exit, column=0, row=2, column_span=2)

        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.grid,
        )

        self.main_view = main_view

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()

    def on_show_view(self):
        """This is run once when we switch to this view"""

        # Makes the background darker
        arcade.set_background_color([rgb - 50 for rgb in arcade.color.DARK_BLUE_GRAY])

        self.manager.enable()

    def on_draw(self):
        """Render the screen."""

        # Clear the screen
        self.clear()
        self.manager.draw()


class MainView(arcade.View):
    """ Main application class."""

    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        
        switch_button = arcade.gui.UIFlatButton(text="Pause", width=250)
        
        # Initialise the button with an on_click event.
        @switch_button.event("on_click")
        def on_click_switch_button(event):
            # Passing the main view into menu view as an argument.
            menu_view = MenuView(self)
            self.window.show_view(menu_view)

        # Use the anchor to position the button on the screen.
        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=switch_button,
        )

    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        
        self.manager.enable()

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()
        
        # draw the ui manager
        self.manager.draw()

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()

class ChessBoard(arcade.Sprite):
    """ Board sprite """

    def __init__(self, suit, value, scale=1):
        """ Board constructor """

        # Attributes for suit and value
        self.suit = suit
        self.value = value


class MyChessGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.board_list = arcade.SpriteList()

        self.background_color = arcade.color.AMAZON

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.squares = [] # = arcade.SpriteSolidColor(100, 100, arcade.color.BISQUE)
        for row in range(8):
            for column in range(8):
                if (row + column) % 2 == 0:
                    color = arcade.color.BISQUE
                else:
                    color = arcade.color.BROWN
                square = arcade.SpriteSolidColor(90, 90, color)
                square.center_x = 200 + column * 100
                square.center_y = 100 + row * 100
                self.squares.append(square)
                self.board_list.append(square)

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()
        self.board_list.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        pass


def main():
    """ Main function """
    window = MyChessGame()
    window.setup()
    arcade.run()

#def main():
#    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
#    main_view = MainView()
#    window.show_view(main_view)
#    arcade.run()


if __name__ == "__main__":
    main()
