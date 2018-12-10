from optparse import OptionParser

# Command-line options
parser = OptionParser()
parser.add_option("-c", "--challenge", action="store_true", dest="challenge", default=False, help="Enable challenges (disabled by default)")
