# topa

topa - Top Output Python Analyzer

A command line app to analyze linux top command output.

It will shows you below information for each pid you specified:

- Total record count 
- Max Cpu
- Min Cpu
- Average Cpu
- Max Mem
- Min Mem
- Average Mem

## Install

```bash
pip install topa
```

## Usage

```bash
topa -h(--help)
```

```
Usage: topa [OPTIONS] FILENAME

  TOPA - Top Output Python Analyzer

  A python cli application to analyze standard linux top output

Options:
  -p, --pid INTEGER       The pid list to be analyzed  [required]
  -o, --out [STD|MD|PDF]  The analyze report file format  [default: STD]
  -h, --help              Show this message and exit.

```

> `MD` and `PDF` are not supported yet. 

## Sample output

```bash
topa -p 2476 top.log
```

```
   _               _ __
  | |_     ___    | '_ \  __ _
  |  _|   / _ \   | .__/ / _` |
  _\__|   \___/   |_|__  \__,_|
_|"""""|_|"""""|_|"""""|_|"""""|
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  1.0.0, by https://github.com/jwenjian/topa
```
```markdown
# Reading
Reading top.log  [####################################]  100%

# Report
## Pid = 2476
Total record count = 17261
Max CPU = 47.4%
Min CPU = 9.4%
Avg CPU = 15.69%
Max MEM = 11.1%
Min MEM = 7.4%
Avg MEM = 10.34%
```

**Note:**
1. The progress bar when reading `Reading top.log  [####################################]  100%` may not displayed if your output files are too small and topa process it too fast, this is the limitation of [click](https://click.palletsprojects.com/en/7.x/api/#utilities)
