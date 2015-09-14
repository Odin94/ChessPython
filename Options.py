import configparser



class Options():

    style = None

    window_width = None
    window_height = None

    highlight_selected = None
    highlight_capturable = None
    highlight_possible_moves = None
    show_captured_pieces = None


    backup_options = None # used to cancel editing options



    def load(config = None):
        if config == None: # no config -> load from file
            config = configparser.ConfigParser()

            config.read("Options/options.txt")


        Options.window_width = int(config['GAME WINDOW']['Window_width'])
        Options.window_height = int(config['GAME WINDOW']['Window_height'])

        Options.style = config['VISUALS']['style']
        Options.highlight_selected = config['VISUALS']['highlight_selected'] == 'True'
        Options.highlight_capturable = config['VISUALS']['highlight_capturable'] == 'True'
        Options.highlight_possible_moves = config['VISUALS']['highlight_possible_moves'] == 'True'
        Options.show_captured_pieces = config['VISUALS']['show_captured_pieces'] == 'True'


    def save_current_options():
        config = configparser.ConfigParser()

        hl_sel = "False"
        hl_cap = "False"
        hl_poss = "False"
        show_cap = "False"

        if Options.highlight_selected:
            hl_sel = "True"
        if Options.highlight_capturable:
            hl_cap = "True"
        if Options.highlight_possible_moves:
            hl_poss = "True"
        if Options.show_captured_pieces:
            show_cap = "True"


        config["GAME WINDOW"] = {'window_width' : str(Options.window_width),
                                 'window_height' : str(Options.window_height)}

        config["VISUALS"] = {'style' : Options.style,
                             'highlight_selected' : hl_sel,
                             'highlight_capturable' : hl_cap,
                             'highlight_possible_moves' : hl_poss,
                             'show_captured_pieces' : show_cap}

        with open("Options/options.txt", 'w') as options_file:
            config.write(options_file)


    def set_backup_options():
        config = configparser.ConfigParser()
        config.read("Options/options.txt")

        Options.backup_options = config


    def reset_options():
        config = configparser.ConfigParser()

        config["GAME WINDOW"] = {'window_width' : '800',
                                 'window_height' : '600'}

        config["VISUALS"] = {'style' : 'Default',
                             'highlight_selected' : 'True',
                             'highlight_capturable' : 'True',
                             'highlight_possible_moves' : 'True',
                             'show_captured_pieces:' : 'True'}

        with open("Options/options.txt", 'w') as options_file:
            config.write(options_file)




Options.load() # this needs to be run before the Graphics module. Might not always be the case, and if it isn't some refactoring is in order