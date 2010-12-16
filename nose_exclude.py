import os
import logging
from nose.plugins import Plugin

log = logging.getLogger('nose.plugins.nose_exclude')

class NoseExclude(Plugin):

    def options(self, parser, env=os.environ):
        """Define the command line options for the plugin."""
        super(NoseExclude, self).options(parser, env)
        parser.add_option(
            "--exclude-dir", action="append",
            dest="exclude_dirs",
            help="Directory to exclude from test discovery. \
                Path can be relative to current working directory \
                or an absolute path. May be specified multiple \
                times. [NOSE_EXCLUDE_DIRS]")

        parser.add_option(
            "--exclude-dir-file", type="string",
            dest="exclude_dir_file",
            help="A file containing a list of directories to exclude \
                from test discovery. Paths can be relative to current \
                working directory or an absolute path. \
                [NOSE_EXCLUDE_DIRS_FILE]")

    def _force_to_abspath(self, pathname):
        if os.path.isabs(pathname):
            abspath = pathname
        else:
            abspath = os.path.abspath(pathname)

        if os.path.exists(abspath):
            return abspath
        else:
            raise ValueError("invalid path: %s" % pathname)

    def _load_from_file(self, filename):
        infile = open(filename)
        new_list = [l.strip() for l in infile.readlines() if l.strip()]

        return new_list

    def configure(self, options, conf):
        """Configure plugin based on command line options"""
        super(NoseExclude, self).configure(options, conf)

        self.exclude_dirs = {}

        # preload directories from file
        if options.exclude_dir_file:
            if not options.exclude_dirs:
                options.exclude_dirs = []

            new_dirs = self._load_from_file(options.exclude_dir_file)
            options.exclude_dirs.extend(new_dirs)

        if not options.exclude_dirs:
            self.enabled = False
            return

        self.enabled = True
        root = os.getcwd()
        log.debug('cwd: %s' % root)

        # Normalize excluded directory names for lookup
        for exclude_param in options.exclude_dirs:
            # when using setup.cfg, you can specify only one 'exclude-dir'
            # separated by some character (new line is good enough)
            for d in exclude_param.split('\n'):
                d = d.strip()
                abs_d = self._force_to_abspath(d)
                self.exclude_dirs[abs_d] = True

        exclude_str = "excluding dirs: %s" % ",".join(self.exclude_dirs.keys())
        log.debug(exclude_str)

    def wantDirectory(self, dirname):
        """Check if directory is eligible for test discovery"""
        if dirname in self.exclude_dirs:
            log.debug("excluded: %s" % dirname)
            return False
        else:
            return True


