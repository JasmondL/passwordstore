#!/usr/local/bin/python3

import argparse


def init_command(args):
    pass

def ls_command(args):
    pass

def show_command(args):
    pass

def find_command(args):
    pass

def insert_command(args):
    pass

def edit_command(args):
    pass

def generate_command(args):
    pass

def delete_command(args):
    pass

def rename_command(args):
    pass

def copy_command(args):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    init_parser = subparsers.add_parser('init')
    init_parser.set_defaults(func=init_command)
    init_parser.add_argument('--path', '-p', type=str, dest='path', default=None)
    init_parser.add_argument('gpg-id', type=str, metavar='gpg-id'
                             nargs='+', dest="gpg_id", required=True)

    ls_parser = subparsers.add_parser('ls', 
                                      aliases=['list', 'show'])
    ls_parser.set_defaults(func=ls_command)
    ls_parser.add_argument('subfolder', type=str)

    find_parser = subparsers.add_parser('find',
                                      aliases=['search'])
    find_parser.set_defaults(func=find_command)
    find_parser.add_argument('pass-names', type=str, metavar='pass-names', 
                             nargs='+', dest="pass_names", required=True)

    #TODO: Implement last
    #grep_parser.set_defaults(func=grep_command)
    #grep_parser.add_argument('pass-names', type=str, metavar='pass-names', 
    #                         nargs='+', dest="pass_names", required=True)

    insert_parser = subparsers.add_parser('insert',
                                      aliases=['add'])
    insert_parser.set_defaults(func=insert_command)
    insert_parser.add_argument('--echo', '-e', type=str, dest='echo', default=None)
    insert_parser.add_argument('--multiline', '-m', type=str, dest='echo', default=None)
    insert_parser.add_argument('--force', '-f', action='store_true')
    insert_parser.add_argument('pass-name', dest='pass_name', type=str, required=True)

    edit_parser = subparsers.add_parser('edit')
    edit_parser.set_defaults(func=edit_command)
    edit_parser.add_argument('pass-name', dest='pass_name', type=str, required=True)

    generate_parser = subparsers.add_parser('generate')
    generate_parser.set_defaults(func=generate_command)
    generate_parser.add_argument('--no-symbols', '-n', action='store_true')
    generate_parser.add_argument('--clip', '-c',  action='store_true')
    generate_parser.add_argument('--in-place', '-i', action='store_true')
    generate_parser.add_argument('--force', '-f', action='store_true')
    generate_parser.add_argument('pass-name', dest='pass_name', type=str, required=True)
    generate_parser.add_argument('pass-length', dest='pass_length', type=int)

    delete_parser = subparsers.add_parser('delete',
                                      aliases=['rm','remove'])
    delete_parser.set_defaults(func=delete_command)
    delete_parser.add_argument('--in-place', '-i', action='store_true')
    delete_parser.add_argument('--force', '-f', action='store_true')
    delete_parser.add_argument('pass-name', dest='pass_name', type=str, required=True)

    rename_parser = subparsers.add_parser('rename',
                                      aliases=['mv'])
    rename_parser.set_defaults(func=rename_command)
    rename_parser.add_argument('--force', '-f', action='store_true')
    rename_parser.add_argument('old-path', dest="old_path", type=str, required=True)
    rename_parser.add_argument('new-path', dest="new_path", type=str, required=True)

    copy_parser = subparsers.add_parser('copy',
                                      aliases=['cp'])
    copy_parser.set_defaults(func=copy_command)
    copy_parser.add_argument('--force', '-f', action='store_true')
    copy_parser.add_argument('old-path', dest="old_path", type=str, required=True)
    copy_parser.add_argument('new-path', dest="new_path", type=str, required=True)

    #TODO: Implement last
    #git_parser = subparsers.add_parser('git')


