from optparse import OptionParser
from util import constants
import ConfigParser
import os
import sys

def parse_opts():
    parser = OptionParser(usage=constants.USAGE)
    parser.add_option('-c', '--conf', nargs=1, dest="new_path", help='NEW_PATH specifies a different configuration file')
    (options, args) = parser.parse_args()

    config = ConfigParser.SafeConfigParser()

    path = os.path.expanduser(constants.CONF_PATH)
    if options.new_path:
        path = options.new_path

    if os.path.exists(path) and os.access(path, os.F_OK) and os.access(path, os.W_OK):
        config.read(path)
    else:
        print "No configfile found in '{0}', aborting!".format(path)
        sys.exit(2)

    result = dict(config.items('general'))

    return result, args
