switch = {"#839496": "#657b83",
          "#657b83": "#839496",
          "#93a1a1": "#586e75",
          "#586e75": "#93a1a1",
          "#eee8d5": "#073642",
          "#073642": "#eee8d5",
          "#fdf6e3": "#002b36",
          "#002b36": "#fdf6e3"}

def help():
    print "Usage"
    print "====="
    print "\ndocutils_solarized_invert.py <infile> <outfile>"
    print "\n"


if __name__ == "__main__":

    import sys


    if len(sys.argv) < 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        help()
    else:
        infile = sys.argv[1]
        outfile = sys.argv[2]

        with open(infile) as fin:
            with open(outfile, 'w') as fout:
                for line in fin:
                    switched = []
                    for colour in switch:
                        if colour in line and not colour in switched:
                            line = line.replace(colour, switch[colour])
                            switched.append(switch[colour])
                    fout.write(line)
