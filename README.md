# Ticktok.io Python client
![Build](https://github.com/ticktok-io/ticktok-python/workflows/Build/badge.svg)

This is the official Python client for [Ticktok.io](https://ticktok.io)

### Installation
```bash
pip install ticktok
```

### Usage
```python
    ticktok = ticktok.client(url, token)
    


    @ticktok.listen(name='sdf', schedule='sdfsdf')
    def send_email_if_needed():
        pass
    ````

    ticktok.tick(clock(name='email:bd', schedule='every.1.days'))
    clock = ticktok.clock(name='email:bd', schedule='every.1.days').register(on_tick=lambda: send_email_if_needed())
    clock.unregister()
    
    ticktok.clock(name='sdfs', schedule='asdas').tick()
    ticktok.clock(name='sdfs', schedule='asdas').pause()
    ticktok.clock(name='sdfs', schedule='asdas').resume()

    ticktok.tag('event').create(at=date())
    ticktok.tag('event').delete()
    ticktok.tag('event').tick()


    ticktok = ticktok.client()

    ticktok.tick()

```


