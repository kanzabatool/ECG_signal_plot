# ECG_signal_plot


##Execution
- Run file dist/program/program.exe
```
Linux:
$ ./dist/program/program
```

## Build
```
$ pyinstaller --add-data "data:data" lib/program.py
```


## Development
```
$ pip install -r requirements.txt
```


## Behaviour

- First window plots the data
- Second window plots the data with slider
- Third window removes the noisy data from the ECG 