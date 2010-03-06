import os
import logging
from nose.plugins import Plugin

log = logging.getLogger('nose.plugins.nose-exclude')

class NoseExclude(Plugin):

    def options(self, parser, env=os.environ):
        """Define the command line options for the plugin."""
        super(NoseExclude, self).options(parser, env)

        parser.add_option(
            "--exclude-dirs", action="append",
            dest="exclude_dirs",
            help="Directories to exclude from test discovery. \
                Paths can be relative to current working directory \
                or an absolute path. [NOSE_EXCLUDE_DIRS]")
    
    def configure(self, options, conf):
        """Configure plugin based on command line options"""
        super(NoseExclude, self).configure(options, conf)

        #TODO add logging
        if not options.exclude_dirs:
            self.enabled = False
            return

        self.enabled = True
        root = os.getcwd()
        log.debug('cwd: %s' % root)

        cleaned_dirs = []
        for d in options.exclude_dirs:
            if os.path.isabs(d):
                cleaned_dirs.append(d)
            elif os.path.isdir(d):
                #see if it's relative
                new_abs_d = os.path.join(root,d)
                cleaned_dirs.append(new_abs_d)
            else:
                #bad path
                #TODO
                pass

        self.exclude_dirs = cleaned_dirs

        exclude_str = "excluding dirs: %s" % ",".join(self.exclude_dirs)
        log.debug(exclude_str)

    def wantDirectory(self, dirname):
        """Check if directory is eligible for test discovery"""
        if dirname in self.exclude_dirs:
            log.debug("excluded: %s" % dirname)
            return False
        else:
            return True



            
