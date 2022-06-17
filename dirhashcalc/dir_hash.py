#!/usr/bin/env python3
import hashlib
import sys
import os


VERSION = '0.0.1-dev'


class DirHashCalculator:
    """
    This class handles the hash calculation for a directory.

    To use it, you should make a new instance from it and pass the directory path to it's constructor:
    dir_hash_calculator = DirHashCalculator('/path/to/dir')

    Then you should use method `calc`:
    dir_hsha256 = dir_hash_calculator.calc()

    To make it shorter:
    dir_sha256 = DirHashCalculator('/path/to/dir').calc()
    """
    def __init__(self, dir_name, cli_verbose=False):
        self.main_dir = dir_name
        self.all_files = []
        self.cli_verbose = cli_verbose

    def calc_sha256(self, fname):
        """
        This method calculates sha256 for one single file.

        I need to mention that this method adds the main directory path at the beggining of the given file name.
        For example if you pass `somedir/somefile.txt` to it and main dir is `/home/parsa/my-dir`,
        it considers the file as `/home/parsa/my-dir/somedir/somefile.txt`.
        So don't pass full path to it.
        """
        fname = self.main_dir + '/' + fname
        hash_sha256 = hashlib.sha256()
        chunk_size = 167772160*3
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hash_sha256.update(chunk)
        if self.cli_verbose:
            print(fname)
        return hash_sha256.hexdigest()

    def calc(self):
        """
        This method calculates the final hash.

        It calls `load_files` at first, them starts calculating the final hash by binding hash of every single file inside of directory.
        Also file names and even empty directories effect the hash.
        """
        self.load_files()
        hash_sha256 = hashlib.sha256()
        for f in self.all_files:
            if os.path.isdir(self.main_dir + '/' + f):
                hash_sha256.update((f).encode())
            else:
                file_hash = self.calc_sha256(f)
                hash_sha256.update((f + file_hash).encode())
        return hash_sha256.hexdigest()

    def load_files(self):
        """
        This method starts loading list of all the files inside of the main directory by using method `load_items_in_dir`.
        Also after loading all of the files, it sorts them.
        So in different computers, the default sort of the files maybe different, but by sorting them, hash will not be different in different places.
        """
        self.load_items_in_dir(self.main_dir)
        self.remove_prefix_from_file_paths()
        self.all_files.sort()

    def load_items_in_dir(self, dirname):
        """
        This method gets a full directory path and lists items inside of it.
        It adds every file to property `all_files` on the object.
        Also for the subdirectories, it calls itself recursively.
        """
        items = os.listdir(dirname)
        for item in items:
            self.all_files.append(dirname + '/' + item)
            if os.path.isdir(dirname + '/' + item):
                self.load_items_in_dir(dirname + '/' + item)

    def remove_prefix_from_file_paths(self):
        """
        This method should be called after all the files added to the list using method `load_files`.
        The files added to `all_files` list have the main directory path as prefix.
        It removes this prefix from all of them. So the hash does not depend to the location of the main directory,
        Only location of the subdirectories are important.
        """
        i = 0
        while i < len(self.all_files):
            self.all_files[i] = self.all_files[i][len(self.main_dir)+1:]
            i += 1


def main(argv):
    if len(argv) <= 0:
        print('Usage: dir_hash [path-to-directory]')
        print('     Option -v|--verbose: If you use this option, program logs the files that it is calculating hash of them. So you can track the process.')
        sys.exit()

    show_directory_name_before_hash = len(argv) > 1

    for arg in argv:
        if arg[0] != '-':
            if os.path.isdir(arg):
                dir_hash_calculator = DirHashCalculator(arg, cli_verbose=('-v' in argv or '--verbose' in argv))
                if show_directory_name_before_hash:
                    print(arg + ': ', end='')
                print(dir_hash_calculator.calc())
            else:
                print('Error: "'+arg+'" does not exist or is not a directory', file=sys.stderr)


if __name__ == '__main__':
    main(sys.argv[1:])



