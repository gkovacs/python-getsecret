import yaml
from os.path import expanduser, isfile

def getsecret(key):
  secrets = {}
  if isfile('.getsecret.yaml'):
    secrets = yaml.load(open('.getsecret.yaml'), loader=yaml.SafeLoader)
  elif isfile(expanduser('~/.getsecret.yaml')):
    secrets = yaml.load(open(expanduser('~/.getsecret.yaml')))
  else:
    raise FileNotFoundError('cannot find .getsecret.yaml')
  if key not in secrets:
    raise ValueError('.getsecret.yaml does not contain key ' + key)
  return secrets[key]
