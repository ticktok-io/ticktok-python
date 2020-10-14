# Ticktok.io Python client
![Build](https://github.com/ticktok-io/ticktok-python/workflows/Build/badge.svg)

This is the official Python client for [Ticktok.io](https://ticktok.io)

### Installation
```bash
pip install ticktok
```

### Usage
Scheduling of a simple clock
```python
ticktok = Ticktok(url, token)
ticktok.register(name='email:birthdays', schedule='every.30.seconds', send_bd_emails())
```
```python
ticktok = Ticktok(url, token)

@ticktok.listen_on(name='email:birthdays', schedule='every.30.seconds')
def send_emails_for_upcoming_birthdays():
    pass
```
Unregistering of callbacks
```python
ticktok.unregister_all() # all callbacks
ticktok.unregister(name='email:birthdays', schedule='every.30.seconds') # all callbacks for clock
ticktok.unregister(name='email:birthdays', schedule='every.30.seconds', callback=send_bd_emails()) # specific callback
```
Invoke an action on an existing clock. These are global operation and might affect other clients as well 
```python
ticktok.clock(name='event:start', schedule='every.5.minutes').tick()
ticktok.clock(name='event:provision', schedule='every.5.minutes').pause()
ticktok.clock(name='event:provision', schedule='every.5.minutes').resume()
```




