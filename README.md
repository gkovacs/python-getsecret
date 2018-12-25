# getsecret

Reads credentials from a file `.getsecret.yaml`

## Install

```
pip install getsecret
```

## Using

Create a file `.getsecret.yaml`. It should be in YAML format. An example follows:

```
username: foobar
password: supersecret
```

Now you can access those variables in your code as follows:

```
from getsecret import getsecret
username = getsecret('username')
password = getsecet('password')
```

Now the values of username and password are the ones specified in `.getsecret.yaml` (foobar and supersecret, respectively).

The file `.getsecret.yaml` can be located in the working directory (`./.getsecret.yaml`), or at the user's home directory (`~/.getsecret.yaml`)

## Author

[Geza Kovacs](https://github.com/gkovacs)

## License

MIT

## Related

[getsecret npm package](https://www.npmjs.com/package/getsecret) for javascript on browser/nodejs
