from __future__ import division, print_function;
import logging;
from collections import namedtuple;

# Defaults for arguments are defined here
# These are all overwritten if called from the command line
# However, by putting defaults here, it makes it easier to
#    call FastProject from within other scripts
# These should be kept in sync with arguments in __main__.py
args = namedtuple("defalt_args",  ["data_file",  "housekeeping",
                                   "signatures",  "precomputed",  "output",
                                   "nofilter",  "nomodel",  "pca_filter",
                                   "qc",  "subsample_size",
                                   "min_signature_genes",  "projections",
                                   "weights",  "threshold"]);

args.data_file = "";
args.housekeeping = "";
args.signatures = [];
args.precomputed = [];
args.output = "";
args.nofilter = False;
args.nomodel = False;
args.pca_filter = False;
args.qc = False;
args.subsample_size = None;
args.min_signature_genes = 5;
args.projections = [];
args.weights = "";
args.threshold = None;



def FP_Output(*args):
    """
    Used to have finer control over outputs.
    """
    print(*args);
    logmessage = ' '.join([str(a) for a in args]);
    logging.info(logmessage);
