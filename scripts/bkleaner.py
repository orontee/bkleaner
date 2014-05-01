import argparse
import cssutils
import logging
from logging.config import dictConfig
import os.path
from zipfile import ZipFile
from bkleaner.settings import LOGGING
from bkleaner.transform import Transformer
from bkleaner.schemes import schemes
import bkleaner.errors as errors

dictConfig(LOGGING)
logger = logging.getLogger('bkleaner')


def initialize_parser():
    description = 'Change stylesheets of ebooks in EPUB format'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('path', type=str, nargs='+',
                        help='Path to files to transform')
    parser.add_argument('-s', type=str, dest='scheme', required=True,
                        help='Transformation scheme', choices=schemes.keys())
    return parser


if __name__ == '__main__':
    parser = initialize_parser()
    args = parser.parse_args()

    try:
        scheme = schemes[args.scheme]
    except KeyError:
        logger.error('Unknown scheme: {0}'.format(args.rules))
        exit(errors.SCHEME_NOT_FOUND)
    tr = Transformer(scheme)
    if args.path:        
        for p in args.path:
            logger.info('Opening {0}'.format(p))
            try:
                f = ZipFile(p, 'r')
            except FileNotFoundError:
                logger.error('File not found: {0}'.format(p))
                exit(errors.FILE_NOT_FOUND)
            infos = f.infolist()
            sf = f.open('stylesheet.css')
            logger.info('Loading stylesheet.css')
            sheet = cssutils.parseString(sf.read())
            logger.info('Applying transformations')
            tr(sheet)

            root, ext = os.path.splitext(p)
            target = root + '_clean' + ext
            logger.info('Writing cleaned book to {0}'.format(target))
            of = ZipFile(target, 'w')
            for info in infos:
                if info.filename != 'stylesheet.css':
                    of.writestr(info, f.read(info))
                else:
                    of.writestr(info, sheet.cssText)
            f.close()
            of.close()
